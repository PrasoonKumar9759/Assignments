import pandas as pd

data={
    'Name':['Alice','Bob','Carol','David','Eve'],
    'Age':[20,22,19,21,20],
    'Gender':['Female','Male','Female','Male','Female'],
    'Marks':[85,78,92,74,88]
}

df=pd.DataFrame(data)
print(df)

print(df[['Name','Marks']])


d1=df[df['Marks']>80]
print(d1)


Highest_Marks=df['Marks'].max()
print(Highest_Marks)
print(df[df['Marks']==Highest_Marks])

