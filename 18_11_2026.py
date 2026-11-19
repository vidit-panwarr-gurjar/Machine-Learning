import pandas as pd
import numpy as np
#q1
series = pd.Series([340,285,410,190],index = ["Mon","Tue","Wed","Thu"])
print(series)
print(series["Wed"])
print(series.mean(),series.max())
#q2
table = {
    "Player":["Rohit","Virat","Gill","Pant"],
    "team":["MI","RCB","GT","DC"],
    "Runs":[4200,6100,2800,3100],
    "Average":[31.5,48.2,44.9,35.6]
}
df1 = pd.DataFrame(table)
print(df1)
print(df1.dtypes)
#q3
df = pd.read_csv("students.csv")
print(df.shape)
print(df.head(3),df.tail(2))
#q4
print(df.info())
#q5
print(df.describe())
#q6
print(df["prev_marks"])
print(type(df["prev_marks"]).__name__)
print(type(df[["prev_marks"]]).__name__)
print(df[["hours_studied","prev_marks"]].head(3))
#7
marks = pd.DataFrame(
    {
        "name":["Aarav","Priya","Rohit","Sneha"],
        "Maths":[88,74,91,66]
    },index = [2,0,3,1]
)
print(marks.loc[0])
print(marks.iloc[0])
print(marks.loc[2,"name"])
print(marks.iloc[2,0])
l1 = [10,90,80,45,76,100]
l2 = []
for i in l1:
    if i > 75:
        l2.append(i)
print(l2)
m = df["hours_studied"]>8
print(np.sum((df["hours_studied"]>8)))
