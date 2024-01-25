import numpy as np

print(np.__version__)
a = np.array([1, 2, 6, 4])
print(a)
b = np.zeros((3, 2))  # 全0
c = np.ones((3, 2))  # 全1
print(b)
print(c)
bsize = b.shape
print(bsize)  # 3行2列
d_up = np.arange(3, 7)  # i=3,i<7,i++
print(d_up)
jian_ju = np.linspace(0, 10, 4)  # 开头到结尾,一共4个数,开头结尾都包含
print(jian_ju)
# 创建数组默认64位的浮点数类型
change = np.array([1.1, 2.2, 6.4])
print(change)
change = change.astype(int)  # 可以用astype变成int型
print(change)
