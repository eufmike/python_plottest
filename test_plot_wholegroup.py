#%%
import numpy as np
import pandas as pd
from imp import reload 
from my_package import data_processing
reload(data_processing)

#%%
# load data by pandas
path = '0926WT_analysis.xlsx'
data = pd.ExcelFile(path)
sheetname = data.sheet_names
print(sheetname)

#%%
# extract data from the excel file
data_events = data.parse(sheetname[0])
data_events = pd.DataFrame(data_events) # convert to dataframe
data_steps = data.parse(sheetname[1])
data_steps = pd.DataFrame(data_steps)
data_seg = data.parse(sheetname[2])
data_seg = pd.DataFrame(data_seg)

#%%
# show data
data_seg.head(5)
print(data_seg.shape[0])
data_events.head(5)
data_steps.head(5)

#%%
# check data dimension
x = 1
for i in range(data_seg.shape[0]):
    print(x)
    x += 1
for i in range(data_seg.shape[0]):
    print(i)
print(data_seg.shape[0])

#%%
# combine segment data and steps
combined_data = data_processing.combine_seg_step(data_seg, data_steps)
# print(combined_data)
# print(combined_data.shape)
combined_data.describe()

#%%
dir()
del data_processing
dir()

#%%
# plot 2D graph
'''
import matplotlib.pyplot as plt

P1 = plt.plot(combined_data['X Coord'], combined_data['Y Coord'])
P1.show()
'''

#%%
# plot 2D graph in bokeh
import bokeh.plotting as bk
import bokeh.palettes
import itertools

# output to static HTML file
bk.output_file('xy.html')

# create object list
object_ID = combined_data['object ID']
object_ID = np.unique(object_ID)
print(object_ID)

# create cycle palette
color_palette = np.unique(bokeh.palettes.Paired[12])
colors = itertools.cycle(color_palette)

# create a plot
p = bk.figure(title = 'x-y location', x_axis_label= 'x coord', y_axis_label= 'y coord')
for m, color in zip(object_ID, colors):
    print(m)
    temp_data = combined_data.loc[combined_data['object ID'] == m]
    
    p.scatter(x = temp_data['X Coord'], y = temp_data['Y Coord'], fill_color = color, \
                line_color = 'black', \
                line_width = 0.5
    )
                   
    p.line(x = temp_data['X Coord'], y = temp_data['Y Coord'], color = '#07357f')

#p.scatter(source = combined_data, x = 'X Coord', y = 'Y Coord', color = 'object ID', \
#          fill_color = color_palette)
bk.show(p)

'''
from ggplot import *
P1 = ggplot(aes(x= 'X Coord', y = 'Y Coord'), data=data_merge) + \
    geom_path(aes(group = TrackID.y, color = TrackID.y))
P1.show()
'''

#%%
# plot 3D graph in Plotly
import plotly.plotly as py
import plotly.graph_objs as go
import bokeh.palettes
import itertools

# create object list
object_ID = combined_data['object ID']
object_ID = np.unique(object_ID)
print(object_ID)

# create cycle palette
color_palette = np.unique(bokeh.palettes.Paired[12])
colors = itertools.cycle(color_palette)

data = []
# make trace data
for m, color in zip(object_ID, colors):
    print(m)
    temp_data = combined_data.loc[combined_data['object ID'] == m]
    T = temp_data['Physical Time']
    x = pd.Series(temp_data['X Coord'])
    x.index = T
    y = pd.Series(temp_data['Y Coord'])
    y.index = T
    z = pd.Series(temp_data['Z Coord'])
    z.index = T

    trace = go.Scatter3d(
        x=x,y=y,z=z,
        mode = 'lines+markers',
        marker = dict(
            size=4,
            color = color,
            opacity=0.8
        ),
        line = dict(
            color='#1f77b4',
            width=1
        )
    )
    data.append(trace)

print(data)

layout = dict(
    width=1024,
    height=1024,
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
        aspectratio = dict( x=1, y=1.11, z=0.175),
        aspectmode = 'manual'
    ),
)

fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='sample_01', height = 400, validate = False)

#%%
import plotly.offline as pyoffline
#py.offline.init_notebook_mode()

pyoffline.plot(fig)