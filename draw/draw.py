import plotly.graph_objects as go


def fig_layout(template, fig, chart_titles=None, plots_colorscale=None):
    """
    Changing layout and styles
    :param template: Str, Plotly template
    :param fig: plotly.graph_objs._figure.Figure
    :param descr: Str
    :return: plotly.graph_objs._figure.Figure
    """
    if chart_titles == None:
        xaxis = (r'Raman Shift [cm <sup>-1</sup>]')
        yaxis = (r'Intensity [au]')
        title = (r'Raman Spectrum')
        chart_titles = {'x': xaxis, 'y': yaxis, 'title': title}

    # TODO tutaj zdefiniować jak mają wyglądać wszystkie ploty i wyrzucić możliwość wybierania czegokolwiek poza
    #  nazwami osi i tytułem
    fig.update_layout(showlegend=True,
                      template=template,
                      colorway=plots_colorscale,
                      paper_bgcolor='rgba(255,255,255,255)',
                      # plot_bgcolor='rgba(255,255,255,255)',
                      width=900,
                      height=550,
                      xaxis=dict(
                          title=f"{chart_titles['x']}",
                          linecolor="#777",  # Sets color of X-axis line
                          showgrid=False,  # Removes X-axis grid lines
                          linewidth=2.5,
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
                      ),
                      title={
                          'text': chart_titles['title'],
                          'y': 0.9,
                          'x': 0.5,
                          'xanchor': 'center',
                          'yanchor': 'top'},

                      legend=go.layout.Legend(x=0.5, y=0 - .4, traceorder="normal",
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
    fig.update_traces(hovertemplate=None)
    fig.update_layout(hovermode="x")
    return fig



