import plotly.plotly as py
import plotly.graph_objs as go


def histogram_stacked(*cols):
    """
    Plot a histogram with stacked traces using plotly API.

    :param cols: Variadic parameter to pass in columns for traces.
    :return: Possibly return HTML file from plotly offline.
    """
    data = []
    for c in cols:
        tempTrace = go.Histogram(x=c)
        data.append(tempTrace)
    layout = go.Layout(barmode='stack')
    fig = go.Figure(data=data, layout=layout)
    py.plot(fig, filename='emoviz stacked histogram')