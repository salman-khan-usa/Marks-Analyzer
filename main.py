import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Marks-Analyzer/marks.csv')
print(df)
print(df.info())

#Total Marks For each student
df['Total/400'] = df[['Physics','Chemistry','Math','Computer']].sum(axis=1)

#Percentage for each student
df['Percentage'] = df['Total/400']/400*100

#Adding Grade
def grades(g):
    
    if g >= 90:
        return 'A+'
    elif g >= 85:
        return 'A'
    elif g >= 75:
        return'B+'
    elif g > 50:
        return 'C'
    else:
        'F'


df['Grade'] = df['Percentage'].apply(grades)
print(df)

