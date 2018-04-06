#%%
import numpy as np
import pandas as pd

path = '0926WT_analysis.xlsx'

#data = pd.read_excel(path)
#print(data.head(3))

data = pd.ExcelFile(path)
sheetname = data.sheet_names
print(sheetname)
print(sheetname[2])

data_seg = data.parse('Segments')
data_seg = pd.DataFrame(data_seg)
type(data_seg)
data_seg.head(5)


x = 0
for i in data_seg:
    x += 1
    print(x)



