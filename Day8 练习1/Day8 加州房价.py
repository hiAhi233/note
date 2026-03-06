import pandas as pd

url = "housing.csv"
df = pd.read_csv(url)

print("=== 数据前5行 ===")
print(df.head())

print("\n=== 数据基本信息（行列数、数据类型、缺失值）===")
print(df.info())

print("\n=== 数据统计描述（均值、标准差、最值等）===")
print(df.describe())

print("\n=== 查看列名 ===")
print(df.columns.tolist())

print("\n=== 查看缺失值数量 ===")
print(df.isnull().sum())

df['total_bedrooms'] = df['total_bedrooms'].fillna(df['total_bedrooms'].median())

print("\n=== 不同地区房价均值 ===")
price_by_region = df.groupby('ocean_proximity')['median_house_value'].mean()
print(price_by_region)