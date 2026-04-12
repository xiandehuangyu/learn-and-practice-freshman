import matplotlib.pyplot as plt
import numpy as np

array1 = np.random.randint(1, 100, 10)
print(array1)
print(array1.sum())
print(np.sum(array1))  # 求和
print(array1.mean())
print(np.mean(array1))  # 算术平均值
print(np.median(array1))  # 中位数
print(np.quantile(array1, 0.5))  # 分位数，此处为50%分位
print(array1.std())
print(np.std(array1))  # 标准差
print(array1.var())
print(np.var(array1))  # 方差
# 变异系数 array1.std()/array1.mean()
print(array1.max())
print(np.max(array1))  # 最大值
print(array1.min())
print(np.min(array1))  # 最小值
print(array1.argmax())
print(np.argmax(array1))  # 最大值索引
print(array1.argmin())
print(np.argmin(array1))  # 最小值索引
print(np.amax(array1))  # 最大值
print(np.amin(array1))  # 最小值
print(np.ptp(array1))  # 全距，即最大值-最小值
print(np.sort(array1))  # 排序
print(np.argsort(array1))  # 排序索引
print(np.unique(array1))  # 去重

plt.boxplot(array1, showmeans=True)
# 盒须图，会显示最大值，最小值，中位数，平均值，上下四分位数
plt.ylim([-20, 120])
plt.show()
# 对于高维
# 可以通过axis参数指定对哪个轴进行操作
# array2 = np.random.randint(1,100,(3,4))
# print(array2)
# print(array2.mean())
# print(array2.mean(axis=0))# 按列求平均
# print(array2.mean(axis=1))# 按行求平均
# 还有需求自行搜索或导包,如scipy的stats