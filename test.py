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