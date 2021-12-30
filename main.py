import random
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import pandas as pd
df=pd.read_csv('data.csv')
#print(df)
#fig=px.bar(x=height_data,y=count)
score_data=df['math score']
#print(height_data)
#print(count)
#fig=px.bar(x=height_data,y=count)
mean=statistics.mean(score_data)
median=statistics.median(score_data)
mode=statistics.mode(score_data)
standard_deviation=statistics.stdev(score_data)
print(mean)
print(median)
print(mode)
print(standard_deviation)
first_stdev_start,first_stdev_end=mean-standard_deviation,mean+standard_deviation
second_stdev_start,second_stdev_end=mean-(2*standard_deviation),mean+(2*standard_deviation)
third_stdev_start,third_stdev_end=mean-(3*standard_deviation),mean+(3*standard_deviation)

fig=ff.create_distplot([score_data],['RESULT'],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode='lines',name='MEAN'))
fig.add_trace(go.Scatter(x=[first_stdev_start,first_stdev_start],y=[0,0.17],mode='lines',name='STANDARD DEVIATION 1 START'))
fig.add_trace(go.Scatter(x=[first_stdev_end,first_stdev_end],y=[0,0.17],mode='lines',name='STANDARD DEVIATION 1 END'))

fig.add_trace(go.Scatter(x=[second_stdev_start,second_stdev_start],y=[0,0.17],mode='lines',name='STANDARD DEVIATION 2 START'))
fig.add_trace(go.Scatter(x=[second_stdev_end,second_stdev_end],y=[0,0.17],mode='lines',name='STANDARD DEVIATION 2 END'))

fig.add_trace(go.Scatter(x=[third_stdev_start,third_stdev_start],y=[0,0.17],mode='lines',name='STANDARD DEVIATION 3 START'))
fig.add_trace(go.Scatter(x=[third_stdev_end,third_stdev_end],y=[0,0.17],mode='lines',name='STANDARD DEVIATION 3 END')) 

list_of_data_in_first_stdev=[result for result in score_data if result>first_stdev_start and result<first_stdev_end]
list_of_data_in_second_stdev=[result for result in score_data if result>second_stdev_start and result<second_stdev_end]
list_of_data_in_third_stdev=[result for result in score_data if result>third_stdev_start and result<third_stdev_end]
print(len(list_of_data_in_first_stdev))
print(len(list_of_data_in_second_stdev))
print(len(list_of_data_in_third_stdev))
print('PERCENTAGE OF DATA IN FIRST STDEV',len(list_of_data_in_first_stdev)/len(score_data)*100)
print('PERCENTAGE OF DATA IN SECOND STDEV',len(list_of_data_in_second_stdev)/len(score_data)*100)
print('PERCENTAGE OF DATA IN THIRD STDEV',len(list_of_data_in_third_stdev)/len(score_data)*100)
fig.show()