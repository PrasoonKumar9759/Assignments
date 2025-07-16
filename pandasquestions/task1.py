import pandas as pd
data = pd.Series([25,30,35,40,45])
print(data)

data1=data = pd.Series([25,30,35,40,45],index=['A','B','C','D','E'])
print(data1)

print(data1.head(3))

print(data1.mean)
print(data1.median)
print(data1.std)
print(data1.var)