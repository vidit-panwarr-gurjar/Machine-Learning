
import numpy as np 
a = np.array([10,20,30])

print(np.where(a > 15,1,0))
a = a.reshape(-1,1)
print(a)
#Random Numbers
b = np.random.randint(0,100,5)
print(b)
#1
arr = np.arange(10,101,10)
print(arr)
print(arr.shape)
print(arr.dtype)
print(arr.reshape(2,5))
#2
temps = np.array([28.5,31.2,35.8,29.1,33.4,27.9, 36.2, 30.0, 34.7, 26.3])
a = temps > 30
print(np.sum(a))
print(a.mean())
print(temps[(temps > 28) & (temps < 35)])
#3
arr1 = np.arange(1,17).reshape(4,4)
print(arr1)
print("*************")
print(arr1[2:3])
print(arr1[:,3])
print("--------------------------")
print(arr1[2:4,2:4])
#4
rng = np.random.default_rng(7)
m = rng.integers(10,100,(5,3)).astype(float)
print(rng)
print(m)
a = (m-m.mean(axis=0))/m.std(axis = 0)
print(a.mean(axis = 0))
print(a.std(axis = 0))
#5
marks = np.array([38, 72, 45, 19, 88, 40, 61, 29, 95, 55])
a=(np.where(marks >= 40, 1 , 0))
print(a, np.sum(a))
print((np.sum(a)/marks.size) * 100)
#6
scores = np.array([[78, 85, 62],
                   [90, 71, 88],
                   [55, 64, 70],
                   [82, 93, 79]])
print(scores.sum(axis = 1))
print(scores.mean(axis = 0))
abc = scores.sum(axis = 1)
abx = scores.mean(axis = 0)
print(np.argmax(abc))
print(np.argmin(abx))