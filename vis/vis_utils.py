import base64

import plotly.express as px
import plotly.io as pio
import streamlit as st
import pandas as pd
import peakutils


def trim_spectra(df):
    # trim raman shift range
    min_, max_ = int(float(df.index.min())), int(float(df.index.max())) + 1
    min_max = st.slider('Custom range', min_value=min_, max_value=max_, value=[min_, max_])
    min_rs, max_rs = min_max  # .split('__')
    min_rs, max_rs = float(min_rs), float(max_rs)
    mask = (min_rs <= df.index) & (df.index <= max_rs)
    return df[mask]


def choose_template():
    """
    Choose default template from the list
    :return: Str, chosen template
    """
    template = st.selectbox(
        "Chart template",
        list(pio.templates), index=6, key='new')

    return template


def get_chart_vis_properties():
    palettes = {
        'qualitative': ['Alphabet', 'Antique', 'Bold', 'D3', 'Dark2', 'Dark24', 'G10', 'Light24', 'Pastel',
                        'Pastel1', 'Pastel2', 'Plotly', 'Prism', 'Safe', 'Set1', 'Set2', 'Set3', 'T10', 'Vivid',
                        ],
        'diverging': ['Armyrose', 'BrBG', 'Earth', 'Fall', 'Geyser', 'PRGn', 'PiYG', 'Picnic', 'Portland', 'PuOr',
                      'RdBu', 'RdGy', 'RdYlBu', 'RdYlGn', 'Spectral', 'Tealrose', 'Temps', 'Tropic', 'balance',
                      'curl', 'delta', 'oxy',
                      ],
        'sequential': ['Aggrnyl', 'Agsunset', 'Blackbody', 'Bluered', 'Blues', 'Blugrn', 'Bluyl', 'Brwnyl', 'BuGn',
                       'BuPu', 'Burg', 'Burgyl', 'Cividis', 'Darkmint', 'Electric', 'Emrld', 'GnBu', 'Greens', 'Greys',
                       'Hot', 'Inferno', 'Jet', 'Magenta', 'Magma', 'Mint', 'OrRd', 'Oranges', 'Oryel', 'Peach',
                       'Pinkyl', 'Plasma', 'Plotly3', 'PuBu', 'PuBuGn', 'PuRd', 'Purp', 'Purples', 'Purpor', 'Rainbow',
                       'RdBu', 'RdPu', 'Redor', 'Reds', 'Sunset', 'Sunsetdark', 'Teal', 'Tealgrn', 'Turbo', 'Viridis',
                       'YlGn', 'YlGnBu', 'YlOrBr', 'YlOrRd', 'algae', 'amp', 'deep', 'dense', 'gray', 'haline', 'ice',
                       'matter', 'solar', 'speed', 'tempo', 'thermal', 'turbid',
                       ]
    }

    col1, col2, col3 = st.columns(3)

    with col1:
        palette_type = st.selectbox("Type of color palette", list(palettes.keys()), 0)
    with col2:
        palette = st.selectbox("Color palette", palettes[palette_type], index=0)
        if st.checkbox('Reversed', False):
            palette = palette + '_r'
    with col3:
        template = choose_template()

    palette_module = getattr(px.colors, palette_type)
    palette = getattr(palette_module, palette)

    return palette, template


def get_chart_vis_properties_vis():
    palettes = {
        'qualitative': ['Alphabet', 'Antique', 'Bold', 'D3', 'Dark2', 'Dark24', 'G10', 'Light24', 'Pastel',
                        'Pastel1', 'Pastel2', 'Plotly', 'Prism', 'Safe', 'Set1', 'Set2', 'Set3', 'T10', 'Vivid',
                        ],
        'diverging': ['Armyrose', 'BrBG', 'Earth', 'Fall', 'Geyser', 'PRGn', 'PiYG', 'Picnic', 'Portland', 'PuOr',
                      'RdBu', 'RdGy', 'RdYlBu', 'RdYlGn', 'Spectral', 'Tealrose', 'Temps', 'Tropic', 'balance',
                      'curl', 'delta', 'oxy',
                      ],
        'sequential': ['Aggrnyl', 'Agsunset', 'Blackbody', 'Bluered', 'Blues', 'Blugrn', 'Bluyl', 'Brwnyl', 'BuGn',
                       'BuPu', 'Burg', 'Burgyl', 'Cividis', 'Darkmint', 'Electric', 'Emrld', 'GnBu', 'Greens', 'Greys',
                       'Hot', 'Inferno', 'Jet', 'Magenta', 'Magma', 'Mint', 'OrRd', 'Oranges', 'Oryel', 'Peach',
                       'Pinkyl', 'Plasma', 'Plotly3', 'PuBu', 'PuBuGn', 'PuRd', 'Purp', 'Purples', 'Purpor', 'Rainbow',
                       'RdBu', 'RdPu', 'Redor', 'Reds', 'Sunset', 'Sunsetdark', 'Teal', 'Tealgrn', 'Turbo', 'Viridis',
                       'YlGn', 'YlGnBu', 'YlOrBr', 'YlOrRd', 'algae', 'amp', 'deep', 'dense', 'gray', 'haline', 'ice',
                       'matter', 'solar', 'speed', 'tempo', 'thermal', 'turbid',
                       ]
    }
    print_widget_labels('Colors')
    palette_type = st.selectbox("Type of color palette", list(palettes.keys()) + ['custom'], 0)
    if palette_type == 'custom':
        palette = st.text_area('Hexadecimal colors', '#DB0457 #520185 #780A34 #49BD02 #B25AE8',
                               help='Type space separated hexadecimal codes')
        palette = palette.split()
    else:
        palette = st.selectbox("Color palette", palettes[palette_type], index=0)
        palette_module = getattr(px.colors, palette_type)
        palette = getattr(palette_module, palette)

    if st.checkbox('Reversed', False):
        palette = palette[::-1]

    print_widgets_separator(2)
    print_widget_labels('Template')
    template = choose_template()
    print_widgets_separator(2)

    return palette, template


def get_plot_description():
    print_widget_labels('Labels')
    xaxis = st.text_input('X axis name', r'Raman Shift cm <sup>-1</sup>')
    yaxis = st.text_input('Y axis name', r'Intensity [au]')
    title = st.text_input('Title', r'')
    chart_titles = {'x': xaxis, 'y': yaxis, 'title': title}
    return chart_titles


def get_plot_description_pca():
    print_widget_labels('Labels')
    xaxis = st.text_input('X axis name', r'PC 1')
    yaxis = st.text_input('Y axis name', r'PC 2')
    title = st.text_input('Title', r'')
    chart_titles = {'x': xaxis, 'y': yaxis, 'title': title}
    return chart_titles


def print_widgets_separator(n=1, sidebar=False):
    """
    Prints customized separation line on sidebar
    """
    html = """<hr style="height:1px;
            border:none;color:#fff;
            background-color:#999;
            margin-top:5px;
            margin-bottom:10px"
            />"""

    for _ in range(n):
        if sidebar:
            st.sidebar.markdown(html, unsafe_allow_html=True)
        else:
            st.markdown(html, unsafe_allow_html=True)


def print_widget_labels(widget_title, margin_top=5, margin_bottom=10):
    """
    Prints Widget label on the sidebar and lets adjust its margins easily
    :param widget_title: Str
    """
    st.markdown(
        f"""<p style="font-weight:500; margin-top:{margin_top}px;margin-bottom:{margin_bottom}px">{widget_title}</p>""",
        unsafe_allow_html=True)


def subtract_baseline_and_smoothen(df, vals, cols_name=False):
    """
    Subtracting baseline from original df, and smoothing the curve using rolling average
    :param df: Original DataFrame
    :param vals: polynomial degree and window for rolling average both Int
    :param cols_name:  Boolean
    :return: DataFrame
    """
    baselines = pd.DataFrame(index=df.index)
    baselined = pd.DataFrame(index=df.index)
    flattened = pd.DataFrame(index=df.index)

    for col in df.columns:
        # for baseline correction in PCA module, as there are some differences in input
        col_name = col
        if cols_name:
            col_name = 'col'

        tmp_spectrum = df[col].dropna()  # trick for data with NaNs
        tmp_spectrum = pd.Series(peakutils.baseline(tmp_spectrum, vals[col_name][0]), index=tmp_spectrum.index)
        baselines[col] = tmp_spectrum

        baselined[col] = df[col] - baselines[col]
        flattened[col] = baselined[col].rolling(window=vals[col_name][1], min_periods=1, center=True).mean()

    return df, baselines, baselined, flattened
