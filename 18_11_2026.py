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


