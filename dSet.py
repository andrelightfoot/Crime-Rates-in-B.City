import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import time
import seaborn as sns

df = pd.read_csv('BPD_Part_1_Victim_Based_Crime_Data_Small.csv')

# Function for Q&A's
questions = {1:'How many Neighborhoods are in the dataset?', 2:'How many of each crime reported?', 3:'Number of crimes per hour'}
answers = {}

# Make function to ask question(q), and print answer(a)
def q_and_a(q,a):
    quest_num = q
    ans_num = a
    print(questions[q])
    print('The answer is: {}'.format(answers[a]))

answers[1] = len(df.Neighborhood.unique()) #This will give you a count of all the unique values
answers[2] = df.Description.value_counts() #How many of each crime reported 



# SHOW NUMBER OF CRIMES PER HOUR

# Creates head of time series of dataframe (format: H:M:S)
crime_hours = df['CrimeTime']

# Splits the time series by ':'
split = crime_hours.str.split(':')

# Converts split into timedelta object and rounds to the hour
split_dt = pd.to_timedelta(crime_hours)
rounded_hours = split_dt.dt.floor('H')
plot_hours = rounded_hours / np.timedelta64(1, 'h')

# Initializes/creates plot
plotit = sns.countplot(x=plot_hours ,data=df)
plt.title('Number of Crimes per TimeStamp')
plt.xlabel('Time of Crime')
plt.ylabel('Number of Crimes')
plt.tight_layout()
plt.show(plotit)