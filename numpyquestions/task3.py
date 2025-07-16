import numpy as np


n1=np.random.randint(1,20,size=5)
print(n1)

n2=np.random.randint(1,20,size=5)
print(n2)

print(n1+n2)
print(n1-n2)
print(n1*n2)
print(n1/n2)


print(n1.dot(n2))


print(n1.mean)
print(np.median(n1))
print(np.var(n1))
print(np.std(n1))

print(np.max(n2))
print(np.argmax(n2))

print(np.min(n2))
print(np.argmin(n2))
