import torchvision
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter

test_data = torchvision.datasets.CIFAR10(root='./dataset', train=False,transform=torchvision.transforms.ToTensor())
test_loader = DataLoader(dataset=test_data, batch_size=10, shuffle=True, num_workers=0,drop_last=True)
writer = SummaryWriter("logs")
step = 0
for data in test_loader:
    imgs, targets = data
    writer.add_images("test_images",imgs,step)
    step = step + 1
writer.close()