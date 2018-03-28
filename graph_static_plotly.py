import plotly.offline as py
import plotly.graph_objs as go
import time
import datetime

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
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, range_max]
                )
            ),
            showlegend=False
        )
        return layout


class HeatMap(object):
    """
    Heat map visualization based on each timestamp -> https://plot.ly/python/heatmaps/
    """

    @staticmethod
    def generate(single_df, stnum):
        """
        Generate a heat map of emotions by time .
        :param single_df: Dataframe to operate on.
        :param stnum: Student ID number for graph naming.
        :return: HTML file of offline radar chart.
        """
        data = HeatMap.build_data_traces(single_df)
        layout = HeatMap.build_layout(single_df.count(), stnum)
        fig = go.Figure(data=data, layout=layout)
        return py.plot(fig, filename='plots/data_'+stnum+'_heatmap_single_'+str(time.time())+'.html')

    @staticmethod
    def build_data_traces(df):
        """
        Build data traces for heat map.
        :param df: Dataframe to operate on.
        :return: Data list to place in heatmap.
        """
        value_map = []
        for emotion, color in EMOTIONS.items():
            col = df.select(emotion.lower()).rdd.flatMap(lambda x: x).collect()
            value_map.append(col)
        time_list = df.select('time').rdd.flatMap(lambda x: x).collect()
        data = [go.Heatmap(
            z=value_map,
            x=time_list,
            y=list(EMOTIONS.keys()),
            colorscale='Jet'
        )]
        return data

    @staticmethod
    def build_layout(num_ticks, stnum):
        """
        Build layout for heat map.
        :param num_ticks: Largest value of all traces for setting range of radial axis.
        :param stnum: Student ID number for graph naming.
        :return: Layout for heat map.
        """
        layout = go.Layout(
            title='Student '+stnum+' Emotions By Millisecond',
            xaxis=dict(ticks='', nticks=num_ticks/225, title='Time'),  # Divide by 225 to put ~40 ticks on axis, all 9000 don't fit
            yaxis=dict(ticks='', title='Emotion')
        )
        return layout
