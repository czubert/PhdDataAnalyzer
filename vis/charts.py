import streamlit as st

from draw import draw


def show_charts(figs, chart_titles, normalized):
    """
    Neat function for plotting charts on the left side.

    Elements of fig type are simply drawn.
    For elements of type list or tuple creates inner loop - first element is
    drawn and the rest is hidden in beta_expander

    Args:
        figs (list): list of figures to plot (might be nested)
        :param figs: list of dataframes
        :param normalized: bool
        :param chart_titles: dict

    """
    for fig in figs:
        if isinstance(fig, (list, tuple)):
            f = fig[0]
            draw.fig_layout(f, chart_titles, normalized)
            st.plotly_chart(f, use_container_width=True, theme=None, normalized=normalized)

            with st.expander('Detailed view'):
                for f in fig[1:]:
                    draw.fig_layout(f, chart_titles, normalized)
                    st.plotly_chart(f,
                                    use_container_width=True,
                                    theme=None)
        else:
            draw.fig_layout(fig, chart_titles=chart_titles, normalized=normalized)

            st.plotly_chart(fig,
                            use_container_width=True,
                            theme=None)
