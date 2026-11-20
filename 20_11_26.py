#----------------------Machine Learning----------------------
import pandas as pd
from sklearn.linear_model import LogisticRegression

df = pd.read_csv("my_students.csv")
X = df[["hours_studied","attendance","prev_marks"]]
y = df["passed"]

model = LogisticRegression()
model.fit(X,y)

correct = (model.predict(X) == y).sum()

print("students checked :", len(df))
print("model got right :", correct)
print("Accuracy :",  round(correct/len(df)*100 ,1),"%")

print()
for i,j in zip(X.columns, model.coef_[0]):
    print(f" {i:>15} importance = {j:+.3f}")   
