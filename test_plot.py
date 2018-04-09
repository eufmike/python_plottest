#%%
import numpy as np
import pandas as pd

path = '0926WT_analysis.xlsx'

#data = pd.read_excel(path)
#print(data.head(3))

data = pd.ExcelFile(path)
sheetname = data.sheet_names
print(sheetname)

data_events = data.parse(sheetname[0])
data_events = pd.DataFrame(data_events)
data_steps = data.parse(sheetname[1])
data_steps = pd.DataFrame(data_steps)
data_seg = data.parse(sheetname[2])
data_seg = pd.DataFrame(data_seg)

data_seg.head(5)
print(data_seg.shape[0])

data_events.head(5)
data_steps.head(5)

x = 1
for i in range(data_seg.shape[0]):
    print(x)
    x += 1

print(data_seg['Step IDs'][0])
data_seg_1 = data_seg['Step IDs'][0]
data_seg_1 = data_seg_1.split(sep = ',')
print(len(data_seg_1))

idx = list(range(len(data_seg_1)))
data_step1 = pd.DataFrame(data_seg_1,index = idx, columns= ['Step ID'])
data_step1.dtypes

data_step1['Step ID'] = pd.to_numeric(data_step1['Step ID']) ## change type!!!!!
##data_step1.dtypes
##data_steps.dtypes

data_merge = pd.merge(data_step1, data_steps, on='Step ID')
data_merge
data_merge.dtypes


import matplotlib.pyplot as plt
fig 
plt_1 = plt.subplot(1,1,figsize(5,5))
plt_1.plot(data_merge['X Coord'], data_merge['Y Coord'])
fig

from ggplot import *
P1 = ggplot(aes(x= 'X Coord', y = 'Y Coord'), data=data_merge) + \
    geom_path()
P1.show()


#%%
# Plotly
import plotly.plotly as py
import plotly.graph_objs as go

T = data_merge['Physical Time']

x = data_merge['X Coord']
y = data_merge['Y Coord']
z = data_merge['Y Coord']

trace1 = go.Scatter3d(
    x=x,
    y=y,
    z=z,
    mode='markers',
    marker=dict(
        size=12,
        line=dict(
            color='rgba(217, 217, 217, 0.14)',
            width=0.5
        ),
        opacity=0.8
    )
)
data = [trace1]
layout = go.Layout(
    margin = dict(
        l=0,
        r=0,
        b=0,
        t=0
    )
)
fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='simple-3d-scatter')