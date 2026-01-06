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
df['Grade'] = df['Percentage'].apply(lambda x : 'A+' if x > 85 else 'A'  )
print(df)

