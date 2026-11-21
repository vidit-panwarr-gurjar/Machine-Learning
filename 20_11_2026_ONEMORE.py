import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
df = pd.read_csv("my_students.csv")
df_bad = df.copy()

rng = np.random.default_rng(42)
df_bad["bad_attendance"] = rng.integers(40,101,len(df_bad))

model_bad = LogisticRegression()

X_bad = df_bad[["hours_studied","attendance","prev_marks"]]
y_bad = df_bad["passed"]

model_bad.fit(X_bad,y_bad)

for i,j in zip(X_bad.columns,model_bad.coef_[0]):
    print(i,j)
