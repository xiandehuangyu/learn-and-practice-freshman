import numpy as np

array1 = np.array([1,2,3,4,5])
array2 = np.array([[1,2,3],[4,5,6]])
array3 = np.arange(0,20,2)
array4 = np.linspace(-1,1,11)
array5 = np.logspace(1,10,num=10,base=2)
array6 = np.fromstring('1 2 3 4 5',dtype=int,sep=' ')
def fib(how_many):
    a, b = 0, 1
    for _ in range(how_many):
        a, b = b, a + b
        yield a
gen = fib(20)
array7 = np.fromiter(gen,dtype=int)
array8 = np.random.rand(5)#0-1之间,如果要指定范围，可以用np.random.uniform(low, high, size)
array9 = np.random.randint(1, 100, 10)#左闭右开
array10 = np.random.normal(50,10, 10)#正太分布
array11 = np.random.choice([1,2,3,4,5], 10)#从给定的1-5中随机抽取10个
array12 = np.random.permutation(10)#随机排列10个
array13 = np.random.shuffle(array12)#将array12随机打乱
array14 = np.random.rand(3,4)#3行4列的随机数
array15 = np.random.randint(1, 100, (3, 4, 5))#三维数组
array16 = np.zeros((3,4))#全0
array17 = np.ones((3,4))#全1
array18 = np.eye(3)#对角线为1，其余为0
array19 = np.diag([1,2,3])#对角线为1，其余为0
array20 = np.full((3,4),10)#全10
#array21 = plt.imread('guido.jpg')#读取图片，获得对应三维数组
array22 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
#.size 获得元素个数
print(array22.size)
#.shape 获得维度
print(array22.shape)
#.ndim 获得维数
print(array22.ndim)
#.dtype 获得数据类型
print(array22.dtype)
#.itemsize 获得每个元素的字节数
print(array22.itemsize)
#.nbytes 获得整个数组的字节数
print(array22.nbytes)
#当列表做索引操作即可
print(array22[2])
print(array22[0][0])
print(array22[-1][-1])
#特殊,用逗号分隔，达到同时限制
print(array22[0:2,1])
#可以用数组做索引操作,会将分别对应位置的元素组成一个新的数组
print(array22[[0,2],[1,2]])
#布尔索引
print(array22>5)
print(array22[array22>5])