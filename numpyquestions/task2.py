import numpy as np

data=[i for i in range(10,100,10)];

n1=np.array(data)
print(n1)


q1=n1[:3]
q2=n1[::2]
q3=n1[::-1]
print(q1)
print(q2)
print(q3)

