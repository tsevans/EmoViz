import plotly.plotly as py
import plotly.graph_objs as go


EMOTIONS = ['Neutral', 'Happy', 'Sad', 'Angry', 'Surprise', 'Scared', 'Disgust']


class SinglePlot(object):

    @staticmethod
    def histogram_stacked(*cols):
        """
        Plot a histogram with stacked traces using plotly API.

        :param cols: Variadic parameter to pass in columns for traces.
        :return: Possibly return HTML file from plotly offline.
        """
        data = []
        for c in cols:
            temp_trace = go.Histogram(x=c)
            data.append(temp_trace)
        layout = go.Layout(barmode='stack')
        fig = go.Figure(data=data, layout=layout)
        py.plot(fig, filename='emoviz stacked histogram')