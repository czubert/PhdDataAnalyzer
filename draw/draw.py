import plotly.graph_objects as go
import plotly.express as px


def fig_layout(fig, chart_titles=None):
    """
    Changing layout and styles
    :param template: Str, Plotly template
    :param fig: plotly.graph_objs._figure.Figure
    :param descr: Str
    :return: plotly.graph_objs._figure.Figure
    """

    a = ['Alphabet', 'Antique', 'Bold', 'D3', 'Dark2', 'Dark24', 'G10', 'Light24', 'Pastel',
    'Pastel1', 'Pastel2', 'Plotly', 'Prism', 'Safe', 'Set1', 'Set2', 'Set3', 'T10', 'Vivid',
    ]

    palette_module = getattr(px.colors, 'qualitative')
    color = getattr(palette_module, 'Plotly')

    # TODO tutaj zdefiniować jak mają wyglądać wszystkie ploty i wyrzucić możliwość wybierania czegokolwiek poza
    #  nazwami osi i tytułem
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
                          range=[0, 65000],
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



