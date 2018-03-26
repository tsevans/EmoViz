import plotly.offline as py
import plotly.graph_objs as go
import pyspark.sql as psql
import time

EMOTIONS = {'Neutral': '#000000',
            'Happy': '#F9E03D',
            'Sad': '#1560BD',
            'Angry': '#C00000',
            'Surprise': '#FF7F50',
            'Scared': '#4FCFCB',
            'Disgust': '#5B4A14'}


class SinglePlot(object):
    """
    Class for plotting all emotions for a single participant on the same graph.
    """

    @staticmethod
    def avg_radar_chart(df, filename):
        my_r = []
        my_theta = []
        for emo, colr in EMOTIONS.items():
            my_theta.append(emo)
            col_avg = df.agg({emo.lower(): 'avg'}).collect()[0][0]
            my_r.append(col_avg)

        data = [go.Scatterpolar(
            r=my_r,
            theta=my_theta,
            fill='toself'
        )]

        lay = go.Layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[min(my_r), max(my_r)]
                )
            ),
            showlegend=False
        )

        fig = go.Figure(data=data, layout=lay)
        py.plot(fig, filename='plots/'+filename+str(time.time()))


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

    @staticmethod
    def line_graph(df, name):
        data = []
        for emotion, color in EMOTIONS.items():
            trace = go.Scatter(x=df.time,
                               y=df[emotion.lower()],
                               name=emotion,
                               line=dict(color=color))
            trace_avg = go.Scatter(x=df.time,
                                   y=[df.agg({emotion.lower(): 'avg'})]*df.count(),
                                   name=emotion+' Average',
                                   visible=False,
                                   line=dict(color=color, dash='dash'))
            data.append(trace)
            data.append(trace_avg)

        updatemenus = list([
            dict(type='buttons',
                 active=-1,
                 buttons=list([
                     dict(label='Neutral',
                          method='update',
                          args=[{'visible': [True]},
                                {'title': 'Neutral High'}])
                 ]),
            )
        ])

        layout = dict(title=name, showlegend=False, updatemenus=updatemenus)
        fig = dict(data=data, layout=layout)
        py.plot(fig, filename='update_button')
