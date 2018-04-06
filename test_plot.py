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
pd.to_numeric(data_step1) ## change type!!!!!
data_step1.dtypes
data_steps.dtypes

data_merge = pd.merge(data_step1, data_steps, on='Step ID')
data_merge
