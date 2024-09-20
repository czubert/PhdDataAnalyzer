import streamlit as st

from draw import draw


def show_charts(figs, chart_titles):
    """
    Neat function for plotting charts on the left side.

    Elements of fig type are simply drawn.
    For elements of type list or tuple creates inner loop - first element is
    drawn and the rest is hidden in beta_expander

    Args:
        figs (list): list of figures to plot (might be nested)
        plots_color: color scale for plotly
        template: plotly template

    """
    for fig in figs:
        if isinstance(fig, (list, tuple)):
            f = fig[0]
            draw.fig_layout(f)
            st.plotly_chart(f, use_container_width=True, theme=None)

            with st.expander('Detailed view'):
                for f in fig[1:]:
                    draw.fig_layout(f)
                    st.plotly_chart(f,
                                    use_container_width=True,
                                    theme=None)
        else:
            draw.fig_layout(fig,
                            chart_titles=chart_titles)

            st.plotly_chart(fig,
                            use_container_width=True,
                            theme=None)
