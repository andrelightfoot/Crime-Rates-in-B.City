# The goal of this program is to analyze the crime rate of each neighborhood in the dataset

import pandas as pd
import numpy as np
from collections import Counter
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('BPD_Part_1_Victim_Based_Crime_Data_Small.csv')

# 1. Extract list of each individual neighborhood
neighborhood = df['Neighborhood']

#  2. Create function to extract unique neighborhoods, no duplicates.
neighborhood.unique()

# 3. Function to take 'Total Incidents' column and add point to corresponding Neighborhood
cnt = Counter()
for nhood in neighborhood:
    cnt[nhood] +=1

# 4. Convert into actual dict. and extract matching points
cnt_dict = dict(cnt)
keys = cnt_dict.keys()
vals = cnt_dict.values()

# 5. Create and show plot 
fig, ax = plt.subplots()
ax.plot(keys,vals)
plt.show()
# Plot is too crowded to be understood....