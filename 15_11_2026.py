import numpy as np
#Python
l1 = [10,20,30,40,50]
for i in range(len(l1)):
    l1[i] = l1[i] + 5
print(l1)
#Broadcasting
arr = np.array([10,20,30,40,50])
arr = arr+5
print(arr)
#Q1
arr1 = np.arange(12)
arr1 = arr1.reshape(3,4)
arr1 = arr1 - arr1.mean(axis = 0)
arr1 = arr1/arr1.std(axis =0)
arr1 = arr1.mean(axis = 0)