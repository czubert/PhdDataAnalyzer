import plotly.graph_objects as go
import plotly.express as px
import streamlit


def fig_layout(fig, chart_titles=None, normalized=False):
    """
    Changing layout and styles
    :param normalized:
    :param chart_titles: Str
    :param fig: plotly.graph_objs._figure.Figure
    :return: plotly.graph_objs._figure.Figure
    """
    y_range = [0, 63000]
    if normalized == True:
        y_range = [0, 1]

    fig.update_layout(hovermode="x",
                      showlegend=True,
                      paper_bgcolor='rgba(255,255,255,255)',
                      plot_bgcolor='rgba(255,255,255,255)',
                      width=900,
                      height=550,

                      xaxis=dict(
                          title=f"{chart_titles['x']}",
                          linecolor="#444",  # Sets color of X-axis line
                          showgrid=False,  # Removes X-axis grid lines
                          linewidth=2.0,
                          showline=True,
                          showticklabels=True,
                          ticks='outside',
                      ),

                      yaxis=dict(
                          title=f"{chart_titles['y']}",
                          linecolor="#777",  # Sets color of Y-axis line
                          showgrid=True,  # Removes Y-axis grid lines
                          linewidth=1.5,
                          gridwidth=1.8,
                          range=y_range,
                      ),

                      title={
                          'text': chart_titles['title'],
                          'y': 0.9,
                          'x': 0.5,
                      },

                      font=dict(
                          family="Courier New, monospace",
                          size=18,
                          color="black",

                      ),

                      legend=go.layout.Legend(x=0.5,
                                              y=0 - .4,
                                              traceorder="normal",
                                              font=dict(
                                                  family="sans-serif",
                                                  size=13,
                                                  color="black",

                                              ),
                                              bgcolor="#fff",
                                              bordercolor="#ccc",
                                              borderwidth=0.4,
                                              orientation='h',
                                              xanchor='auto',
                                              itemclick='toggle',
                                              )),
    # plain hover
    fig.update_traces(hovertemplate=None,
                      line={'width': 3},
                      )

    return fig


#  TODO sprawdzić, czy to nie przez to wywala się teraz multi kolumnowy wykres
# Adding traces, spectrum line design
def add_traces_single_spectra(df, fig, x, y, name):
    fig.add_traces(
        [go.Scatter(y=df.reset_index()[y],
                    x=df.reset_index()[x],
                    name=name,
                    line=dict(
                        width=3.5,  # Width of the spectrum line
                        color='#1c336d'  # color of the spectrum line
                        # color='#6C9BC0'  # color of the spectrum line
                    ),
                    )])
    return fig


def add_traces(df, fig, x, y, name, col=None):
    fig.add_traces(
        [go.Scatter(y=df.reset_index()[y],
                    x=df.reset_index()[x],
                    name=name,
                    line=dict(
                        width=3.5,
                    ),
                    )])
    return fig
