import torch
from torchvision import datasets
from torchvision.transforms import ToTensor, Lambda

ds = datasets.FashionMNIST(
    root="data",
    train=True,
    download=True,
    transform=ToTensor(),
    # Lambda变换，定义了一个函数来将整数转换为one-hot编码张量
    # 它首先创建一个大小为10的零张量（数据集中的标签数量）并调用scatter_，根据索引y将值更改为1
    target_transform=Lambda(
        lambda y: torch.zeros(10, dtype=torch.float).scatter_(dim=0, index=torch.tensor(y), value=1))
)

#REsize操作
from PIL import Image
from torchvision import transforms
img = Image.open('/Users/huaniaofengyue/Desktop/DSC_8866.JPG')
resize = transforms.Resize((500))
img_resize = resize(img)
img_resize.show()

#裁剪
img = Image.open('/Users/huaniaofengyue/Desktop/DSC_8866.JPG')
centercrop = transforms.CenterCrop((400, 1000))  # (Height,Width)
img_centercrop = centercrop(img)
img_centercrop.show()

img = Image.open('/Users/huaniaofengyue/Desktop/DSC_8866.JPG')
centercrop = transforms.CenterCrop(400)
img_centercrop = centercrop(img)
img_centercrop.show()

#随机裁剪
from PIL import Image
from torchvision import transforms

img = Image.open('/Users/huaniaofengyue/Desktop/DSC_8866.JPG')
randomcrop = transforms.RandomCrop((400, 500))
for i in range(5):
    img_randomcrop = randomcrop(img)
    img_randomcrop.show()