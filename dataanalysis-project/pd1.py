import pandas as pd
import numpy as np

ser1 = pd.Series(data=[120,380,250,360],index=['一季度','二季度','三季度','四季度'])
print(ser1)
ser2 = pd.Series({'一季度': 320, '二季度': 180, '三季度': 300, '四季度': 405})
print(ser2)
ser1+=10
print(ser1)
print(ser1+ser2)
#既可以用索引查数据，又可以像字典一样查
print(ser1['一季度'])
print(ser1.iloc[0])#直接用索引会有提示ser1[0]
#依旧可以切片
print(ser1[1:3])
print(ser2['二季度':'四季度'])
#也可以布尔索引
print(ser1[ser1>300])
#也可以花式索引
print(ser1.iloc[[0,2]])
ser2[['二季度','四季度']]=400,500
print(ser2)
#以下是常用方法和属性
print(ser2.dtype)                    # 数据类型
print(ser2.hasnans)                  # 有没有空值
print(ser2.index)                    # 索引
print(ser2.values)                   # 值
print(ser2.is_monotonic_increasing)  # 是否单调递增
print(ser2.is_unique)                # 是否每个值都独一无二
print(ser2.count())   # 计数
print(ser2.sum())     # 求和
print(ser2.mean())    # 求平均
print(ser2.median())  # 找中位数
print(ser2.max())     # 找最大
print(ser2.min())     # 找最小
print(ser2.std())     # 求标准差
print(ser2.var())     # 求方差