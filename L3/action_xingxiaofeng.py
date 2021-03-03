from sklearn.cluster import KMeans
from sklearn import preprocessing
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import metrics

def K_means(train_data, k): #使用KMeans聚类,训练聚类模型
    kmeans = KMeans(n_clusters=k, random_state=0)  # 建立模型对象
    kmeans.fit(train_data)  # 训练聚类模型
    return kmeans

data = pd.read_csv("./car_data.csv", encoding='gbk')
# print(data.shape)
# print(data.head())

# 处理训练集
train_x = data[["人均GDP", "城镇人口比重", "交通工具消费价格指数", "百户拥有汽车量"]]
# 规范化到 [0,1] 空间
min_max_scaler = preprocessing.MinMaxScaler()
train_x = min_max_scaler.fit_transform(train_x)
# print(train_x)
# print(train_x.shape)
# 通过手肘法和轮廓系数法，确定K值
sse = []
for k in range(2, 10):
    # kmeans算法
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(train_x)
    # 计算inertia簇内误差平方和
    sse.append(kmeans.inertia_)
x = range(2, 10)
plt.xlabel('K')
plt.ylabel('SSE')
plt.plot(x, sse, 'o-')
plt.show()

scores = []  # 存放轮廓系数
for k in range(2, 10):
    # kmeans算法
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(train_x)
    predict_y = kmeans.predict(train_x)  # 预测聚类模型
    scores.append(metrics.silhouette_score(train_x, predict_y, metric='euclidean'))
x = range(2, 10)
plt.xlabel('K')
plt.ylabel('scores')
plt.plot(x, scores, 'o-')
plt.show()
# # 选定K=5，训练聚类模型，预测聚类模型，得到聚类结果
kmeans = K_means(train_x,5)
# 合并聚类结果，插入到原数据中
result = pd.concat((data, pd.DataFrame(kmeans.labels_)), axis=1)
result.rename({0: "聚类结果"}, axis=1, inplace=True)
print(result)
