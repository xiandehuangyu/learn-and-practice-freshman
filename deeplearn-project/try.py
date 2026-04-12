from PIL import Image
from torch.utils.tensorboard import SummaryWriter
import numpy as np

writer = SummaryWriter("logs")
image_path = "../练手数据集/train/bees_image/16838648_415acd9e3f.jpg"
img_PIL = Image.open(image_path)
img_array = np.array(img_PIL)
writer.add_image("tests", img_array, 2, dataformats="HWC")
writer.close()
