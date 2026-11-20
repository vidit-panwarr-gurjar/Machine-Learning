#------------------Machine Learning------------------
import pandas as pd
from sklearn.linear_model import LogisticRegression

df = pd.read_csv("my_students.csv")
model = LogisticRegression()
X = df[["hours_studied","attendance","prev_marks"]]
y = df["passed"]

model.fit(X,y)

right = (model.predict(X) == y).sum()

print("values Checked",len(df))
print("Accuracy",round((right/len(df))*100))

print()

for i,j in zip(X.columns,model.coef_[0]):
    print(f"{i:<15} importance {j:+.3f}")