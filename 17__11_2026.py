#----------Pandas------------------
import pandas as pd
print(pd.__version__)
series = pd.Series([85,60,70,80])
print(series)
abc = {
    "City":["Sharanpur","Merrut","Noida","LA"],
    "State":["UP","UP","UP","California"],
    "Population":["Goatedd","mid+","mid","80"]
}
df = pd.DataFrame(abc)
print(df)
print(df.shape)
print(df.dtypes)
df1 = pd.read_csv("students.csv")
print(df1.head())
print(df1.info)
print(df1.describe)