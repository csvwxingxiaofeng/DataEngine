import numpy as np
from pandas import Series, DataFrame
data = {'语文': [68,95,98,90,80], '数学': [65,76,86,88,90], '英语': [30,98,88,77,90]}
df1 = DataFrame(data)
df2 = DataFrame(data, index=['张飞', '关羽', '刘备', '典韦', '许诸'], columns=['语文', '数学', '英语'])
print("5名同学成绩为：\n",df2)
print('各科的平均成绩为：\n',df2.mean())
print('最小成绩：\n',df2.min())
print('最大成绩：\n',df2.max())
print('方差：\n',df2.var())
print('标准差：\n',df2.std())
df = DataFrame(data,index=['张飞', '关羽', '刘备', '典韦', '许诸'], columns=['语文', '数学', '英语'])
df["总分"] = df.sum(axis=1)
print(df["总分"] )
df1 = df.sort_values("总分", ascending=False)
print(df1)
df1["排名"] = [1,2,3,4,5]
print("总成绩排序：\n",df1)
