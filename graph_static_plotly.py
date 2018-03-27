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


class RadarChart(object):
    """
    Radar chart visualization based on average values -> https://plot.ly/python/radar-chart/
    """

    @staticmethod
    def generate(df_list):
        """
        Generate a radar chart of emotions average for each file in df_list.
        :param df_list: List of dataframes to operate on.
        :return: HTML file of offline radar chart.
        """
        data, max_r = RadarChart.build_data_traces(df_list)
        layout = RadarChart.build_layout(max_r)
        fig = go.Figure(data=data, layout=layout)
        name = 'single' if len(df_list) is 1 else 'multi'
        return py.plot(fig, filename='plots/radar_'+name+'_'+str(time.time())+'.html')

    @staticmethod
    def build_data_traces(df_list):
        """
        Build data traces for radar chart.
        :param df_list: List of dataframes to operate on.
        :return: Data list of traces and max value for layout range.
        """
        data = []
        df_count = 1
        range_max = 0
        for df in df_list:
            curr_r = []
            curr_theta = []
            for emotion, color in EMOTIONS.items():
                curr_theta.append(emotion)
                column_avg = df.agg({emotion.lower(): 'avg'}).collect()[0][0]
                curr_r.append(column_avg)
            range_max = max(range_max, max(curr_r))
            data.append(go.Scatterpolar(
                r=curr_r,
                theta=curr_theta,
                fill='toself',
                name='Sample ' + str(df_count)
            ))
            df_count += 1
        return data, range_max

    @staticmethod
    def build_layout(range_max):
        """
        Build layout for radar chart.
        :param range_max: Largest value of all traces for setting range of radial axis.
        :return: Layout for radar chart.
        """
        layout = go.Layout(
            polar = dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, range_max]
                )
            ),
            showlegend=False
        )
        return layout


# class SinglePlot(object):
#     """
#     Class for plotting all emotions for a single participant on the same graph.
#     """
#
#     @staticmethod
#     def avg_radar_chart(df, filename):
#         my_r = []
#         my_theta = []
#         for emo, colr in EMOTIONS.items():
#             my_theta.append(emo)
#             col_avg = df.agg({emo.lower(): 'avg'}).collect()[0][0]
#             my_r.append(col_avg)
#
#         data = [go.Scatterpolar(
#             r=my_r,
#             theta=my_theta,
#             fill='toself'
#         )]
#
#         lay = go.Layout(
#             polar=dict(
#                 radialaxis=dict(
#                     visible=True,
#                     range=[min(my_r), max(my_r)]
#                 )
#             ),
#             showlegend=False
#         )
#
#         fig = go.Figure(data=data, layout=lay)
#         py.plot(fig, filename='plots/' + filename + str(time.time()))
#
#     @staticmethod
#     def histogram_stacked(*cols):
#         """
#         Plot a histogram with stacked traces using plotly API.
#
#         :param cols: Variadic parameter to pass in columns for traces.
#         :return: Possibly return HTML file from plotly offline.
#         """
#         data = []
#         for c in cols:
#             temp_trace = go.Histogram(x=c)
#             data.append(temp_trace)
#         layout = go.Layout(barmode='stack')
#         fig = go.Figure(data=data, layout=layout)
#         py.plot(fig, filename='emoviz stacked histogram')
#
#     @staticmethod
#     def line_graph(df, name):
#         data = []
#         for emotion, color in EMOTIONS.items():
#             trace = go.Scatter(x=df.time,
#                                y=df[emotion.lower()],
#                                name=emotion,
#                                line=dict(color=color))
#             trace_avg = go.Scatter(x=df.time,
#                                    y=[df.agg({emotion.lower(): 'avg'})] * df.count(),
#                                    name=emotion + ' Average',
#                                    visible=False,
#                                    line=dict(color=color, dash='dash'))
#             data.append(trace)
#             data.append(trace_avg)
#
#         updatemenus = list([
#             dict(type='buttons',
#                  active=-1,
#                  buttons=list([
#                      dict(label='Neutral',
#                           method='update',
#                           args=[{'visible': [True]},
#                                 {'title': 'Neutral High'}])
#                  ]),
#                  )
#         ])
#
#         layout = dict(title=name, showlegend=False, updatemenus=updatemenus)
#         fig = dict(data=data, layout=layout)
#         py.plot(fig, filename='update_button')
