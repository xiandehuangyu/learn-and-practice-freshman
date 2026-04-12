from torch import nn
from torch.nn import Conv2d,MaxPool2d,Flatten,Linear#,Sequential

class Net(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = Conv2d(3,32,5,padding=2)
        self.pool1 = MaxPool2d(2)
        self.conv2 = Conv2d(32,32,5,padding=2)
        self.pool2 = MaxPool2d(2)
        self.conv3 = Conv2d(32,64,5,padding=2)
        self.pool3 = MaxPool2d(2)
        self.flatten = Flatten()
        self.linear1 = Linear(1024,64)
        self.linear2 = Linear(64,10)

        """
        self.module1 = Sequential(
            Conv2d(3,32,5,padding=2),
            MaxPool2d(2),
            Conv2d(32,32,5,padding=2),
            MaxPool2d(2),
            Conv2d(32,64,5,padding=2),
            MaxPool2d(2),
            Flatten(),
            Linear(1024,64),
            Linear(64,10)
            )
        """

    def forward(self,x):
        x = self.conv1(x)
        x = self.pool1(x)
        x = self.conv2(x)
        x = self.pool2(x)
        x = self.conv3(x)
        x = self.pool3(x)
        x = self.flatten(x)
        x = self.linear1(x)
        x = self.linear2(x)
        """
        x = self.module1(x)
        """
        return x
    
net = Net()
print(net)