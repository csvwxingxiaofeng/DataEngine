import pandas as pd
# 导入数据
data = pd.read_csv("car_complain.csv")
# print(data.head(10))

# 数据预处理
data1=data.drop('problem',axis=1).join(data['problem'].str.get_dummies(","))#拆分Problem
# print(data1.head(10))

# 数据清洗，别名合并
def f(x):
    x = x.replace("一汽-大众","一汽大众")
    return x

# 品牌投诉总数
data1['brand'] = data1['brand'].apply(f)
df = data1.groupby(['brand'])['id'].agg(['count']).sort_values('count', ascending = False)
df.reset_index(inplace=True)
print("品牌投诉总数，从大到小排序\n",df)

# 车型投诉总数
df1 = data1.groupby(['car_model'])['id'].agg(['count']).sort_values('count', ascending = False)
df1.reset_index(inplace=True)
print("车型投诉总数，从大到小排序\n",df1)

# 品牌的平均车型投诉
df2 = data1.groupby(['brand','car_model'])['id'].agg(['count'])
df2.reset_index(inplace=True)
# print(df2)
df2 = df2.groupby(['brand']).mean().sort_values('count', ascending = False)
df2.reset_index(inplace=True)
print("品牌的平均车型投诉，从大到小排序\n",df2)
