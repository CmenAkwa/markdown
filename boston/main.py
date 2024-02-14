import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt
from pylab import mpl

data = pd.read_csv('housing.csv')
print(data.shape)
print(data.head())
data = (data - data.mean()) / data.std()  # 标准差规范法,mean是算平均数，std是标准差函数,进行归一化处理解决量纲问题
print(data.head())
cols = data.shape[1]  # 为shape的y坐标,就是14,14列
train_x = data.iloc[0:400, 0:cols - 1]  # 前400行,前13列x
train_y = data.iloc[0:400, cols - 1:cols]  # 最后一列为y
test_x = data.iloc[400:505, :cols - 1]
test_y = data.iloc[400:505, cols - 1:cols]


class linearRegression:

    def __init__(self, alpha, times, l):
        self.alpha = alpha
        self.times = times
        self.l = l

    # 损失函数
    def CostFunction(self, x, y, w):
        inner = np.power(y - (w * x.T).T, 2)
        return np.sum(inner) / (2 * len(x))

    # 正则化损失函数
    def regularizedcost(self, x, y, w):
        reg = (self.l / (2 * len(x))) * (np.power(w, 2).sum())
        return self.CostFunction(x, y, w) + reg

    def fit(self, x, y):
        x = np.matrix(x.values)
        y = np.matrix(y.values)
        x = np.insert(x, 0, 1, axis=1)
        # 创建权重向量W
        self.w_ = np.zeros(x.shape[1])
        # 损失列表,用来保存每次迭代后的损失值
        self.loss_ = []

        # 进行迭代,在迭代过程中,计算损失值,调整权重值,使损失值下降。
        for i in range(self.times):
            # 计算正则化损失函数值：
            loss = self.regularizedcost(x, y, self.w_)
            # 加入到损失列表
            self.loss_.append(loss)
            # 根据步长调整权重w
            self.w_ = self.w_ - (self.alpha / len(x)) * (self.w_ * x.T * x - y.T * x) - (
                    self.alpha * self.l / len(x)) * self.w_

    def predict(self, x):
        x = np.asarray(x)
        x = np.insert(x, 0, 1, axis=1)
        result = np.dot(x, self.w_.T)
        return result


mpl.rcParams["font.sans-serif"] = ["SimHei"]
alpha = 0.001
times = 10000
l = 0
lr = linearRegression(alpha, times, l)
lr.fit(train_x, train_y)
MSE = lr.loss_
RMSE = list(map(lambda num: num, lr.loss_))
result = lr.predict(test_x)
plt.figure(figsize=(10, 10))
plt.plot(result, "ro-", label="预测值")
plt.plot(test_y.values, "go-", label="真实值")  # pandas读取时serise类型，我们需要转为ndarray
plt.title("线性回归预测-梯度下降")
plt.xlabel("样本序号")
plt.ylabel("预测房价")
plt.legend()
plt.show()
