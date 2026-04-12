import torch.nn as nn
import torchvision
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter

dataset = torchvision.datasets.CIFAR10(root='./dataset', train=False, transform=torchvision.transforms.ToTensor())
dataloader = DataLoader(dataset, batch_size=64)
writer = SummaryWriter('log_pool')

class Net(nn.Module):
    def __init__(self):
        super().__init__()
        self.pool = nn.MaxPool2d(kernel_size=3,ceil_mode=True)
        #非线性激活
        #self.relu = nn.ReLU()
        #self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        x = self.pool(x)
        #x = self.relu(x)
        #x = self.sigmoid(x)
        return x
    
net = Net()

temp = 0

for data in dataloader:
    img,target = data 
    writer.add_images("input", img, global_step=temp)
    writer.add_images("output", net(img), global_step=temp)
    temp += 1

writer.close()
