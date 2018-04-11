#%%
import numpy as np
import pandas as pd

a1 = {
    'name' : ['Mike', 'Shiauhan', 'Zoey'],
    'height' : [186, 151, 94]
}
a2 = {
    'name' : ['Oriole'],
    'height': [163]
}

a1 = pd.DataFrame(a1)
a2 = pd.DataFrame(a2)

print(a1)
print(a2)


weight = pd.DataFrame(data={'weight': [205, 130, 28]})

#a1['weight'] = pd.Series(weight, index = a1.index)
a3 = pd.concat([a1, weight], axis = 1)

print(a3)

#%%
import bokeh as bk
import itertools

color_palette = bk.palettes.Set3[9]
colors = itertools.cycle(color_palette)
print(colors)

object_IDs = [1, 2, 3, 4, 5, 3, 3, 2]
object_ID = np.unique(object_IDs)
print(object_ID)

for m, color in zip(object_ID, colors):
    print(m)
    print(color)

import plotly.plotly as py
import plotly.graph_objs as go

'''
data = []
temp_data = combined_data.loc[combined_data['object ID'] == 1]
T = temp_data['Physical Time']
x = pd.Series(temp_data['X Coord'])
x.index = T
y = pd.Series(temp_data['Y Coord'])
y.index = T
z = pd.Series(temp_data['Z Coord'])
z.index = T

trace1 = go.Scatter3d(
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
print(trace1)

temp_data = combined_data.loc[combined_data['object ID'] == 2]
T = temp_data['Physical Time']
x = pd.Series(temp_data['X Coord'])
x.index = T
y = pd.Series(temp_data['Y Coord'])
y.index = T
z = pd.Series(temp_data['Z Coord'])
z.index = T

trace2 = go.Scatter3d(
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
print(trace2)

data = [trace1, trace2]
print(data)
type(data)
'''