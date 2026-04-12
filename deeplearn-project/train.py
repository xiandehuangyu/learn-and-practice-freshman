import torchvision
from torch.utils.data import DataLoader
from torch import nn
import torch
#准备数据集
train_data = torchvision.datasets.CIFAR10(root='./dataset', train=True, download=False, transform=torchvision.transforms.ToTensor())
test_data = torchvision.datasets.CIFAR10(root='./dataset', train=False, download=False, transform=torchvision.transforms.ToTensor())
#加载数据集
train_loader = DataLoader(train_data, batch_size=64)
test_loader = DataLoader(test_data, batch_size=64)
#搭建神经网络
class Net(nn.Module):
    def __init__(self):
        super().__init__()
        self.model = nn.Sequential(
            nn.Conv2d(3,32,5,1,2),
            nn.MaxPool2d(2),
            nn.Conv2d(32,32,5,1,2),
            nn.MaxPool2d(2),
            nn.Conv2d(32,64,5,1,2),
            nn.MaxPool2d(2),
            nn.Flatten(),
            nn.Linear(64*4*4,64),
            nn.Linear(64,10)
        )
    
    def forward(self, x):
        x = self.model(x)
        return x
#创建网络模型
net = Net()

#损失函数
loss_fn = nn.CrossEntropyLoss()

#优化器
learning_rate = 0.01
optimizer = torch.optim.SGD(net.parameters(), lr=learning_rate)

#设置训练网络的参数
#记录训练次数
total_train_step = 0
#记录测试次数
total_test_step = 0
#训练轮数
epoch = 10
for i in range(epoch):
    print("第{}轮训练开始".format(i+1))
    
    #训练步骤开始
    for data in train_loader:
        imgs,targets = data
        outputs = net(imgs)
        loss = loss_fn(outputs,targets)

        #优化器优化
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        total_train_step +=1
        print("第{}步训练，损失为{}".format(total_train_step,loss))
    #测试步骤开始
    total_test_loss = 0
    total_accuracy = 0
    with torch.no_grad():
        for data in test_loader:
            imgs,targets = data
            outputs = net(imgs)
            loss = loss_fn(outputs,targets)
            total_test_loss += loss
            accuracy = (outputs.argmax(1)==targets).sum()
            total_accuracy += accuracy
    print("整体测试集的损失为{}".format(total_test_loss))
    print("整体测试集的正确率为{}".format(total_accuracy/len(test_data)))

    #保存训练结果
    torch.save(net,"net_{}.pth".format(i))