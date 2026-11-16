
import numpy as np 
a = np.array([10,20,30])

print(np.where(a > 15,1,0))
a = a.reshape(-1,1)
print(a)
#Random Numbers
b = np.random.randint(0,100,5)
print(b)
