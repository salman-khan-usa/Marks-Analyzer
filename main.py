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
        return 'A+(90)'
    elif g >= 85:
        return 'A(85)'
    elif g >= 70:
        return'B+(70)'
    elif g > 50:
        return 'C(50)'
    else:
        'F'


df['Grade'] = df['Percentage'].apply(grades)


#Subject Analysis
Average_marks = df[['Math','Physics','Chemistry','Computer']].mean()
Max_marks     = df[['Math','Physics','Chemistry','Computer']].max()
Min_marks = df[['Math','Physics','Chemistry','Computer']].min()






#Visualization
#Average marks
plt.bar(Average_marks.index,Average_marks.values,color='Blue')
plt.xlabel('Subjects')
plt.ylabel('Marks/100')
plt.title('Average Marks of Subjects')
plt.show()

#Highest Marks
plt.bar(Max_marks.index,Max_marks.values,color='purple')
plt.title('Highest Marks')
plt.xlabel('Subjects')
plt.ylabel('Marks/100')
plt.show()

#Lowest Marks
plt.bar(Min_marks.index,Min_marks.values,color='red')
plt.xlabel('Subjects')
plt.title('Lowest Marks')
plt.ylabel('Marks/100')
plt.show()

#Students Top 5 Achievers
ranking_student = df.sort_values(by='Total/400',ascending=False)
top_achievers = ranking_student.head(5)


plt.bar(top_achievers['Name'],top_achievers['Total/400'],color='Green')
plt.title('High Acheivers ')
plt.xlabel('Students')
plt.ylabel('Marks/400')
plt.show()


#Grade Distribution pie chart
grade_distrubution = df['Grade'].value_counts()


plt.pie(grade_distrubution,labels=grade_distrubution.index,autopct='%1.1f%%')
plt.title('Grade Distribution')
plt.show()


