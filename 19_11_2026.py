#-------------Machine Learning-------------------
import numpy as np
a = np.arange(5,61,5)
print(a)
print(a.shape,a.dtype)
b = a.reshape(3,4)
print(a.reshape(3,4))
print(b[1])
print(b[:,-1])


