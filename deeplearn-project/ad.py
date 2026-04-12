from PIL import Image
from torchvision import transforms
from torch.utils.tensorboard import SummaryWriter

writer = SummaryWriter("logs")
image_path = "../练手数据集/train/bees_image/16838648_415acd9e3f.jpg"
img = Image.open(image_path)

trans_totensor = transforms.ToTensor()
img_tensor = trans_totensor(img)

writer.add_image("tests",img_tensor)
trans_norm = transforms.Normalize([0.5, 0.5, 0.5], [0.5, 0.5, 0.5])
img_norm = trans_norm(img_tensor)
writer.add_image("tests_norm",img_norm,2)
trans_resize = transforms.Resize((224,224))
img_resize = trans_resize(img)
img_resize_tensor = trans_totensor(img_resize)
writer.add_image("tests_resize",img_resize_tensor,0)
trans_resize2 = transforms.Resize(224)
trans_compose = transforms.Compose([trans_resize2,trans_totensor])
img_resize2 = trans_compose(img)
writer.add_image("tests_resize2",img_resize2,1)
trans_random = transforms.RandomCrop(224)
trans_compose2 = transforms.Compose([trans_random,trans_totensor])
for i in range(10):
    img_random = trans_compose2(img)
    writer.add_image("tests_random",img_random,i)
writer.close()