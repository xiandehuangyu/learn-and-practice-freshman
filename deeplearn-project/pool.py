import torch
import torch.nn as nn
input = torch.tensor([[1,2,0,3,1],
                      [0,1,2,3,0],
                      [1,2,1,0,0],
                      [5,2,3,1,1],
                      [2,1,0,1,1]
                      ],dtype=torch.float32)
input = torch.reshape(input, (-1,1,5,5))
print(input.shape)


class  Net(nn.Module):
    def __init__(self):
        super().__init__()
        self.maxpool = nn.MaxPool2d(kernel_size=3,ceil_mode=True)

    def forward(self, x):
        x = self.maxpool(x)
        return x
    
net = Net()
output = net(input)
print(output)