#-------------Machine Learning-------------------
#Q1
import numpy as np
import pandas as pd
a = np.arange(5,61,5)
print(a)
print(a.shape,a.dtype)
b = a.reshape(3,4)
print(a.reshape(3,4))
print(b[1])
print(b[:,-1])
#Q2
s = pd.Series([12,45,33,28,60],index = ["Mon","Tue","Wed","Thu","Fri"])
print(s.loc["Thu"])
print(s.mean())
print(np.sum(s>30))
#Q3
c = pd.read_csv("students_raw.csv")
print(c.shape,c.columns.tolist())
print(np.sum(c["hours_studied"].isna()))
print(np.sum(c["prev_marks"].isna()))
#Q4
print(np.sum(c["hours_studied"]>7))
print((c[c["hours_studied"]>7]).head(3))
#Q5






