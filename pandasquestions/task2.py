import pandas as pd

data={
    'Name':['Alice','Bob','Carol','David','Eve'],
    'Age':[20,22,19,21,20],
    'Gender':['Female','Male','Female','Male','Female'],
    'Marks':[85,78,92,74,88]
}
df=pd.DataFrame(data)
print(df)

print(df.head(2))

print(df.columns.tolist())

print(df.dtypes)

print(df.describe(include='all'))

df['Passed']=df['Marks']>=80
print(df)