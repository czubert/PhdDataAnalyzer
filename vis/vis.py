import pandas as pd
import peakutils
import plotly.express as px
import streamlit as st

import constants
# noinspection PyUnresolvedReferences
# import str_slider
from data_processing import utils, save_read
from vis import manual, sidebar, data_customisation, charts, vis_utils
from vis.vis_utils import print_widgets_separator
from draw import options as vis_opt, options


def visualisation():
    df = None
    st.write('wizualizacja')
    # # Spectrometer type `- BWTek / Renishaw / Witec / Wasatch / Teledyne
    #
    spectrometer = "BWTEK"

    # User data loader
    files = st.sidebar.file_uploader(label='Upload your data or try with ours',
                                     accept_multiple_files=True,
                                     type=['txt', 'csv'])

    # Allow example data loading when no custom data are loaded
    if not files and st.sidebar.checkbox("Load example data"):
        if spectrometer == "EMPTY":
            st.sidebar.error('First Choose Spectra type')
        else:
            files = utils.load_example_files()

    # Check if data loaded, if yes, perform actions
    if files:
        st.spinner('Uploading data in progress')
        # sidebar separating line
        print_widgets_separator(1, sidebar=True)
        df = save_read.files_to_df(files, spectrometer)

        # Select chart type
        chart_type = options.vis_options()

        # sidebar separating line
        print_widgets_separator(1, sidebar=True)

        # Select data conversion type
        spectra_conversion_type = vis_opt.convertion_opt()

        # getting rid of duplicated columns
        df = df.loc[:, ~df.columns.duplicated()]

        # columns in main view. Chart, expanders
        col_left, col_right = st.columns([5, 2])

        # Data Optimisation and plot description
        with col_right:
            normalized = False

            # # Plot settings
            plot_settings = st.expander("Plot settings", expanded=False)

            # # Plot descriptions
            with plot_settings:
                chart_titles = vis_utils.get_plot_description()

            # # Range and separation
            range_expander_name = 'Range' if chart_type in {'SINGLE', 'MS'} else 'Range and separation'
            range_expander = st.expander(range_expander_name, expanded=False)

            with range_expander:
                df = vis_utils.trim_spectra(df)

            if spectra_conversion_type != "RAW":

                # # Data Manipulation
                with st.expander("Data Manipulation", expanded=False):
                    vals = data_customisation.get_deg_win(chart_type, spectra_conversion_type, df.columns)

                    normalized = st.checkbox("Normalize")
                    # TODO w utils jest funkja, która to robi, ale chyba nigdzie nie jest wykorzystywana
                    if normalized:
                        df = (df - df.min()) / (df.max() - df.min())

        #
        # # data manipulation - raw / optimization / normalization
        #

        # Mean Spectra
        if chart_type == 'MS':
            df = df.mean(axis=1).rename('Average').to_frame()

        # Making an expander to choose spectrum from
        if chart_type == 'SINGLE':
            with col_left:
                col = st.selectbox('', df.columns)
                df = df[[col]]

        # Optimisation - polynomial baseline correction
        if spectra_conversion_type == 'OPT':
            df, baselines, baselined, flattened = vis_utils.subtract_baseline_and_smoothen(df, vals)

            baselines = pd.DataFrame(index=df.index)
            baselined = pd.DataFrame(index=df.index)
            flattened = pd.DataFrame(index=df.index)
            for col in df.columns:
                tmp_spectrum = df[col].dropna()
                tmp_spectrum = pd.Series(peakutils.baseline(tmp_spectrum, vals[col][0]), index=tmp_spectrum.index)
                baselines[col] = tmp_spectrum

                baselined[col] = df[col] - baselines[col]
                flattened[col] = baselined[col].rolling(window=vals[col][1], min_periods=1, center=True).mean()

        # Groupped spectra
        if chart_type == 'GS':
            with range_expander:
                shift = data_customisation.separate_spectra(normalized)

                shifters = [(i + 1) * shift for i in range(len(df.columns))]
                plot_df = df if spectra_conversion_type == 'RAW' else flattened
                plot_df = plot_df + shifters
                figs = [px.line(plot_df,
                                x=plot_df.index,
                                y=plot_df.columns,
                                color_discrete_sequence=constants.COLOR_DISCRETE_SEQUENCE,
                                )]

        # Mean spectra
        elif chart_type == 'MS':
            if spectra_conversion_type == 'RAW':
                plot_df = df
                figs = [px.line(plot_df,
                                x=plot_df.index,
                                y=plot_df.columns,
                                color_discrete_sequence=constants.COLOR_DISCRETE_SEQUENCE,
                                )]

            elif spectra_conversion_type == 'OPT':
                columns = ['Average', 'Baseline', 'BL-Corrected', 'Flattened + BL-Corrected']
                plot_df = pd.concat([df, baselines, baselined, flattened], axis=1)
                plot_df.columns = columns

                fig1 = px.line(plot_df,
                               x=plot_df.index,
                               y=columns[-1],
                               color_discrete_sequence=constants.COLOR_DISCRETE_SEQUENCE,
                               )

                fig2 = px.line(plot_df,
                               x=plot_df.index,
                               y=plot_df.columns,
                               color_discrete_sequence=constants.COLOR_DISCRETE_SEQUENCE,
                               )

                figs = [(fig1, fig2)]
            else:
                raise ValueError('Unknown conversion type for Mean spectrum chart')
        # 3D spectra
        elif chart_type == 'P3D':
            plot_df = flattened if spectra_conversion_type in {"OPT"} else df

            plot_df = plot_df.reset_index().melt('Raman Shift', plot_df.columns)
            fig = px.line_3d(plot_df,
                             x='variable',
                             y='Raman Shift',
                             z='value',
                             color='variable',
                             color_discrete_sequence=constants.COLOR_DISCRETE_SEQUENCE,
                             )

            camera = dict(eye=dict(x=1.9, y=0.15, z=0.2))
            fig.update_layout(scene_camera=camera,
                              width=1200, height=1200,
                              margin=dict(l=1, r=1, t=30, b=1),
                              )
            figs = [fig]
        # Single spectra
        elif chart_type == 'SINGLE':
            if spectra_conversion_type == 'RAW':
                plot_df = df
                figs = [px.line(plot_df[col]) for col in plot_df.columns]
            else:
                columns = ['Average', 'Baseline', 'BL-Corrected', 'Flattened + BL-Corrected']
                figs = []

                plot_df = pd.concat([df, baselines, baselined, flattened], axis=1)
                plot_df.columns = columns

                fig1 = px.line(plot_df,
                               x=plot_df.index,
                               y=columns[-1],
                               color_discrete_sequence=constants.COLOR_DISCRETE_SEQUENCE,
                               )
                fig2 = px.line(plot_df,
                               x=plot_df.index,
                               y=plot_df.columns,
                               color_discrete_sequence=constants.COLOR_DISCRETE_SEQUENCE,
                               )
                fig_tup = (fig1, fig2)
                figs.append(fig_tup)
        else:
            raise ValueError("Something unbelievable has been chosen")

        with col_left:
            charts.show_charts(figs,
                               chart_titles,
                               normalized=normalized)

        with col_left:
            st.markdown('')
            link = utils.download_button(plot_df.reset_index(),
                                         f'spectrum.csv',
                                         button_text='Download CSV')

            st.markdown(link, unsafe_allow_html=True)

    else:
        manual.show_manual()
