# The goal of this program is to analyze the crime rate of each District in the dataset

import pandas as pd
import numpy as np
from collections import Counter
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('BPD_Part_1_Victim_Based_Crime_Data_Small.csv')

# 1. Extract list of each individual District
District = df['District']#.dropna(axis=0)


# #  2. Create function to extract unique Districts, no duplicates.
# District.unique()

# 3. Function to take 'Total Incidents' column and add point to corresponding District
cnt = District.value_counts(dropna=True)
cnt_indx = (cnt.index)
cnt_vals = cnt.values
#print(cnt_indx, cnt_vals)


# for disct in District:
#     cnt[disct] +=1

# # 4. Convert into actual dict. and extract matching points
cnt_dict = dict(cnt)
keys = cnt_dict.keys()
vals = cnt_dict.values()

# # 5. Create and show plot 
fig, ax = plt.subplots()
ax.plot(keys,vals)
ax.get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))
plt.show() 

