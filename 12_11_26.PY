#1
import numpy as np
a = np.arange(5,51,5)
print(a)
b=a.reshape(2,5)
print(b.shape,b.ndim,b.dtype)

#2
marks = np.array([45,82,67,91,38,74,59,88])
print(marks[marks >= 60].size)
print(marks[marks >= 60].mean())
print(marks[(marks >= 60) & (marks < 80)])