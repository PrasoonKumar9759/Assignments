import numpy as np

n1=np.arange(1,11)
print(n1)
print(n1.shape)
print(n1.size)
print(type(n1))

n2=np.arange(1,10).reshape(3,3)
print(n2)
print(n2.shape)
print(n2.size)
print(type(n2))


n3=np.random.rand(3,5,3)
print(n3)
print(n3.shape)
print(n3.size)
print(type(n3))