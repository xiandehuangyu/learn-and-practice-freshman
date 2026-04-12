import numpy as np

# numpy数组跟一个数值运算,对应运算会作用到每一个元素
array1 = np.arange(1, 10)
print(array1 + 10)
print(array1 * 10)
# numpy数组和数组运算要求形状相同(不同的机制下面弄)
# 运算会作用于对应元素
# 一元函数会作用在每个元素
# 例np.sqrt(array1)
# abs/fabs 绝对值
# sqrt 平方根
# square 平方
# exp
# log log10 log2
# sign 符号函数
# sin/cos/tan 三角函数
# arcsin/arccos/arctan 反三角函数
# sinh/cosh/tanh 双曲函数
# ceil floor 向上/下取整
# rint round 四舍五入
# 二元函数参数是两个数组,会对对应元素进行运算
# 例np.maximum(array1, array2)
# add/substract/multiply/divide/power/mod/floor_divide 加减乘除幂取模整除
# allclose 检查元素是否几乎相等
# maximum/fmax/minimum/fmin 最大/最小值
# dot 矩阵乘法
# vdot 向量点乘
# inner/outer 内积/外积
# cross 向量叉乘
# intersect1d/union1d/setdiff1d/setxor1d 交集/并集/差集/对称差集
# 其它常用的
# copy 拷贝
# sort 排序
# unique 去重
# split/hsplit/vsplit 分割
# stack/hstack/vstack 堆叠
# concatenate 连接
# append/insert 插入(前者指定末尾，后者可指定位置)
# argwhere/flatnonzero 非零元素位置/非零元素值
# extract/select/where 按指定条件抽取或处理元素
# flip 翻转
# fromregex 从字符串中解析数组
# repeat 重复
# tile 平铺
# roll 移位
# resize 调整大小
# place/put 放置/替换元素
# partition 分割