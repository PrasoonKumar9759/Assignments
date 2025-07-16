import numpy as np


n1=np.random.randint(10,50,size=15)
print(n1)

n2=n1[n1>25]
print(n2)

n3=np.copy(n1)
n3[n3>30]=0
print(n3)

divisible_by_count=np.sum(n1%5==0)
print(divisible_by_count)

