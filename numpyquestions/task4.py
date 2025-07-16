import numpy as np

n1=np.arange(1,13)
print(n1)


n2=n1.reshape(4,3)
print(n2)

n3=n1.reshape(2,2,3)
print(n3)

n4=n3.T
print(n4)
print(n4.shape)

