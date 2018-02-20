import plotly.graph_objs as go
import plotly.offline as ply
import pandas as pd
import plotly.figure_factory as FF

#read data
df =pd.read_csv('P01 AR Emotion by millisecond.csv')

data_table=FF.create_table(df.head())


#later, we could ask client to pick the arguments which he wants to see from a gui; then plot the graph
trace1 = go.Scatter(x=df['time'],y=df['neutral'],mode ='lines',name='neutral')
trace2 = go.Scatter(x=df['time'],y=df['happy'],mode ='lines',name='happy')
trace3 = go.Scatter(x=df['time'],y=df['sad'],mode ='lines',name='sad')
trace4 = go.Scatter(x=df['time'],y=df['angry'],mode ='lines',name='angry')
trace5 = go.Scatter(x=df['time'],y=df['surprise'],mode ='lines',name='surprise')
trace6 = go.Scatter(x=df['time'],y=df['scared'],mode ='lines',name='scared')
trace7 = go.Scatter(x=df['time'],y=df['disgust'],mode ='lines',name='disgust')

layout=go.Layout(title='Emoviz',showlegend=True)

fig=go.Figure(data=[trace1,trace2,trace3,trace4,trace5,trace6,trace7],layout=layout)

ply.plot(fig,filename='simple_plot.html')
