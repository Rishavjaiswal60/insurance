import pandas as pd

def load_dataset():
    return pd.read_csv("insurance/insurance.csv")

df=load_dataset()
# print(df.head(5))
# print(df.info())
# print(df.isnull().sum())
# print(df.duplicated().sum())
df=df.drop_duplicates()
# print(df.duplicated().sum())
# print(df.describe())
# print(df.shape)
num_col=df.select_dtypes(include='number')
print(num_col.columns)


cat_col=df.select_dtypes(include='object')
print(cat_col.columns)

print(df.corr(numeric_only=True)['charges'])

print(df['charges'].skew())