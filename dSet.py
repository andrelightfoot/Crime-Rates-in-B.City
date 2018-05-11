import pandas as pd
import numpy as np

df = pd.read_csv('BPD_Part_1_Victim_Based_Crime_Data_Small.csv')
questions = {1:'How many Neighborhoodsare in the dataset?'}
answers = {}

# Make function to ask question(q), and print answer(a)
def q_and_a(q,a):
    quest_num = q
    ans_num = a
    print(questions[q])
    print('The answer is: {}'.format(answers[a]))

#Answer 1:
answers[1] = len(df["Neighborhood"])
q_and_a(1,1)

