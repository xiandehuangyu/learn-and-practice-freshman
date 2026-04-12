import numpy as np

a = np.array([[1,3],[4,6]])
print(np.linalg.det(a))
#numpy和linalg模块中一些常用的线性代数相关函数
#diag	以一维数组的形式返回方阵的对角线元素或将一维数组转换为方阵（非对角元素元素为0）
#matmul	矩阵乘法运算
#trace	计算对角线元素的和
#norm	求矩阵或向量的范数
#det	计算行列式的值
#matrix_rank	计算矩阵的秩
#eig	计算矩阵的特征值（eigenvalue）和特征向量（eigenvector）
#inv	计算非奇异矩阵（ n 阶方阵）的逆矩阵
#pinv	计算矩阵的摩尔-彭若斯（Moore-Penrose）广义逆
#qr	QR分解（把矩阵分解成一个正交矩阵与一个上三角矩阵的积）
#svd	计算奇异值分解（singular value decomposition）
#solve	解线性方程组Ax=b，其中A是一个方阵
#lstsq	计算 Ax=b 的最小二乘解
A = np.array([[1, 2, 1], [3, 7, 2], [2, 2, 1]])
b = np.array([8, 23, 9]).reshape(-1, 1)
print(np.linalg.matrix_rank(A))
print(np.linalg.matrix_rank(np.hstack((A, b))))
print(np.linalg.solve(A, b))#表示解分别为1，2，3
#多项式
p1 = np.poly1d([3, 2, 1])
p2 = np.poly1d([1, 2, 3])
print(p1)
print(p2)
#获取系数print(p1.coefficients)
#print(p2.coeffs)
#带入x求多项式的值
print(p1(2))
#p1.deriv() 求导
#p1.integ() 积分
#根
print(p1.roots)
print(np.roots(p1.coefficients))
"""
如果使用numpy.polynomial模块的Polynomial类来表示多项式对象
from numpy.polynomial import Polynomial

p3 = Polynomial((2, 3, 1))
print(p3)           # 输出多项式
print(p3(3))        # 令x=3，计算多项式的值
print(p3.roots())   # 计算多项式的根
print(p3.degree())  # 获得多项式的次数
print(p3.deriv())   # 求导
print(p3.integ())   # 求不定积分
"""