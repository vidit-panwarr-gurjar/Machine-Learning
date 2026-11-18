import pandas as pd
import numpy as np
df = pd.read_csv("students.csv")
print(df)
print((df["prev_marks"]>75).sum())
print(df[df["passed"] == 1]["hours_studied"].mean())
df["good_attendance"] = df["prev_marks"] >= 60
print(df.nunique())
