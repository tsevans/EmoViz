import plotly.plotly as py
import plotly.graph_objs as go
from plotly.tools import FigureFactory as ff
import time

import pandas as pd
import time as tm

EMOTIONS = ['Neutral', 'Happy', 'Sad', 'Angry', 'Surprise', 'Scared', 'Disgust']


class SinglePlot(object):

    # TODO: Problem, data file too large for free plotly subscription...
    @staticmethod
    def radar_chart(df):
        print('Generating animated radar chart:')

        # Create figure for animation
        figure = {
            'data': [],
            'layout': {},
            'frames': []
        }

        print('Filling layout...')

        # Fill layout attributed for figure
        figure['layout']['polar'] = {'radialaxis': {'visible': True, 'range': [0, 60]}}
        figure['layout']['showlegend'] = False
        figure['layout']['sliders'] = {
            'args': [
                'transition', {
                    'duration': 400,
                    'easing': 'cunic-in-out'
                }
            ],
            'initialvalue': '00:00:00.000',
            'plotlycommand': 'animate',
            'values': df.select('time').collect(),  # TODO: Check if this is the correct way to get the time column
            'visible': True
        }
        figure['layout']['updatemenus'] = [
            {
                'buttons': [
                    {
                        'args': [None, {'frame': {'duration': 500, 'redraw': False},
                                        'fromcurrent': True,
                                        'transition': {'duration': 300, 'easing': 'quadratic-in-out'}}],
                        'label': 'Play',
                        'method': 'animate'
                    },
                    {
                        'args': [[None], {'frame': {'duration': 0, 'redraw': False}, 'mode': 'immediate',
                                          'transition': {'duration': 0}}],
                        'label': 'Pause',
                        'method': 'animate'
                    }
                ],
                'direction': 'left',
                'pad': {'r': 10, 't': 87},
                'showactive': False,
                'type': 'buttons',
                'x': 0.1,
                'xanchor': 'right',
                'y': 0,
                'yanchor': 'top'
            }
        ]

        slider_dict = {
            'active': 0,
            'yanchor': 'top',
            'xanchor': 'left',
            'currentvalue': {
                'font': {'size': 20},
                'prefix': 'Time:',
                'visible': True,
                'xanchor': 'right'
            },
            'transition': {'duration': 300, 'easing': 'cubic-in-out'},
            'pad': {'b': 10, 't': 50},
            'len': 0.9,
            'x': 0.1,
            'y': 0,
            'steps': []
        }

        print('Making data...')

        # Make data
        for row in df.collect():
            data_row_list = go.Scatterpolar(
                r=[row.neutral, row.happy, row.sad, row.angry, row.surprise, row.scared, row.disgust],
                theta=EMOTIONS,
                fill='toself'
            )
            figure['data'].append(data_row_list)

        print('Making frames...')

        # Make frames
        count = 0

        for t in df.select('time').collect():
            if count % 750 != 0:
                count += 1
                continue

            print('Working on timestamp:', t.time)
            frame = {'data': [], 'name': t.time}
            for row in df.collect():
                data_row_list = go.Scatterpolar(
                    r=[row.neutral, row.happy, row.sad, row.angry, row.surprise, row.scared, row.disgust],
                    theta=EMOTIONS,
                    fill='toself'
                )
                frame['data'].append(data_row_list)

            figure['frames'].append(frame)
            slider_step = {
                'args': [
                    [t.time],
                    {'frame': {'duration': 300, 'redraw': False},
                     'mode': 'immediate',
                     'transition': {'duration': 300}}
                ],
                'label': t.time,
                'method': 'animate'}
            slider_dict['steps'].append(slider_step)
            count += 1

        figure['layout']['sliders'] = [slider_dict]

        print('Plotting...')

        py.create_animations(figure, filename='radardemolitsquad'+str(time.time()))
