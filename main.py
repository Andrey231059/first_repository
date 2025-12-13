import pandas as pd


# df = pd.read_csv('World-happiness-report-2024.csv')
df = pd.read_csv('dz.csv')
# print(df.head())
# print(df.describe())
# print(df.shape)
# print(df.isnull().sum())
#
# print(df.info())
# print(df[['Country name', 'Regional indicator']])

group_s = df.groupby('City')['Salary'].sum()
group_m = df.groupby('City')['Salary'].mean()
print(group_s)
print(group_m)