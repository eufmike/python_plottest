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

c1 = a1.append(a2, ignore_index = True)
print(c1)
