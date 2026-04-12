import torch
import torchvision
from torch.utils.tensorboard import SummaryWriter
from torch.utils.data import DataLoader

dataset = torchvision.datasets.CIFAR10(root='./dataset', train=False, download=False, transform=torchvision.transforms.ToTensor())
dataloader = DataLoader(dataset=dataset, batch_size=64)

class Net(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(in_channels=3, out_channels=6, kernel_size=3, stride=1, padding=0)
    
    def forward(self, x):
        x = self.conv1(x)
        return x

net = Net()

step = 0
writer = SummaryWriter('logs')
for data in dataloader:
    imgs,target = data
    output = net(imgs)
    writer.add_images('inputs', imgs, step)
    output = torch.reshape(output, (-1, 3, 30, 30))
    writer.add_images('outputs', output, step)
    step = step + 1
