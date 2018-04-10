#%%
import numpy as np
import pandas as pd

# load data by pandas
path = '0926WT_analysis.xlsx'
data = pd.ExcelFile(path)
sheetname = data.sheet_names
print(sheetname)

# extract data from the excel file
data_events = data.parse(sheetname[0])
data_events = pd.DataFrame(data_events) # convert to dataframe
data_steps = data.parse(sheetname[1])
data_steps = pd.DataFrame(data_steps)
data_seg = data.parse(sheetname[2])
data_seg = pd.DataFrame(data_seg)

# show data
data_seg.head(5)
print(data_seg.shape[0])
data_events.head(5)
data_steps.head(5)

# check data dimension
x = 1
for i in range(data_seg.shape[0]):
    print(x)
    x += 1
for i in range(data_seg.shape[0]):
    print(i)
print(data_seg.shape[0])

# combine segment data and steps

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

"""
import matplotlib.pyplot as plt
fig 
plt_1 = plt.subplot(1,1,figsize(5,5))
plt_1.plot(data_merge['X Coord'], data_merge['Y Coord'])
fig
"""

from ggplot import *
P1 = ggplot(aes(x= 'X Coord', y = 'Y Coord'), data=data_merge) + \
    geom_path()
P1.show()


#%%
# Plotly
import plotly.plotly as py
import plotly.graph_objs as go

T = data_merge['Physical Time']
x = pd.Series(data_merge['X Coord'], index = T)
y = pd.Series(data_merge['Y Coord'], index = T)
z = pd.Series(data_merge['Z Coord'], index = T)

trace = go.Scatter3d(
    x=x,y=y,z=z,
    mode = 'lines+markers',
    marker = dict(
        size=4,
        color = '#6699ff',
        opacity=0.8
    ),
    line = dict(
            color='#1f77b4',
            width=1
    )
)

data = [trace]

layout = dict(
    width=500,
    height=500,
    autosize=False,
    title='sample 01',
    scene=dict(
        xaxis=dict(
            gridcolor='rgb(255, 255, 255)',
            zerolinecolor='rgb(255, 255, 255)',
            showbackground=True,
            backgroundcolor='rgb(230, 230,230)'
        ),
        yaxis=dict(
            gridcolor='rgb(255, 255, 255)',
            zerolinecolor='rgb(255, 255, 255)',
            showbackground=True,
            backgroundcolor='rgb(230, 230,230)'
        ),
        zaxis=dict(
            gridcolor='rgb(255, 255, 255)',
            zerolinecolor='rgb(255, 255, 255)',
            showbackground=True,
            backgroundcolor='rgb(230, 230,230)'
        ),
        camera=dict(
            up=dict(
                x=0,
                y=0,
                z=1
            ),
            eye=dict(
                x=-1.7428,
                y=1.0707,
                z=0.7100,
            )
        ),
        aspectratio = dict( x=1, y=1, z=0.7 ),
        aspectmode = 'manual'
    ),
)

fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='sample_01', height = 400, validate = False)