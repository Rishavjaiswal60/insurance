from data import load_dataset
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd



df=load_dataset()

# sns.histplot(data=df,x='charges',kde=True)
"""there is right skewness in the data and we have to remove 
it"""
# sns.boxplot(data=df,y='charges')
"""there are oulier also we have to check for that too"""
# sns.scatterplot(data=df,x='age',y='charges',hue='smoker')
# plt.show()

'''count plot'''

# cols=['sex','smoker','region']
# for col in cols:
#     # plt.figure(figsize=(6,4))
#     # sns.countplot(data=df,x=col)
#     # plt.title(col)
#     # plt.show()
#     print(df[col].value_counts())



# plt.title("Distribution of insurance charge")

"""bar plots"""

# sns.barplot(data=df,x='smoker',y='charges')
# sns.barplot(data=df,x='sex',y='charges')
'''corsstab'''
# print(pd.crosstab(df['sex'],df['smoker']))
# print

"""pairplot"""
# sns.pairplot(df)
"""heat map"""

# sns.heatmap(df.corr(numeric_only=True),annot=True,cmap='coolwarm',fmt='.2f')
# plt.show()

# cols=['age','bmi','children','charges']

# for col in cols:
#     Q1=df[col].quantile(0.25)
#     Q3=df[col].quantile(0.75)

#     IQR=Q3-Q1

#     upper=Q3+1.5*IQR
#     lower=Q1-1.5*IQR

#     outlier=df[(df['bmi']<lower) | (df['bmi']>upper) ]
#     print(outlier[['bmi']])

print(df.info())