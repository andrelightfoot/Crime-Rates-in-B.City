import pandas as pd
import numpy as np

df = pd.read_csv('BPD_Part_1_Victim_Based_Crime_Data_Small.csv')
questions = {1:'How many Neighborhoods are in the dataset?', 2:'How many of each crime reported?'}
answers = {}

# Make function to ask question(q), and print answer(a)
def q_and_a(q,a):
    quest_num = q
    ans_num = a
    print(questions[q])
    print('The answer is: {}'.format(answers[a]))

answers[1] = len(df.Neighborhood.unique()) #This will give you a count of all the unique values
answers[2] = df.Description.value_counts() #How many of each crime reported
