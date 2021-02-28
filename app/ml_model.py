import torchvision
from torchvision import datasets, models, transforms
import torch
import torch.nn as nn
import os
from efficientnet_pytorch import EfficientNet
from PIL import Image


def get_image_name(image):
    model = EfficientNet.from_pretrained('efficientnet-b2')
    num_ftrs = model._fc.in_features
    model._fc = nn.Linear(num_ftrs, 40)
    # model = model.to(device)
    model.load_state_dict(torch.load(os.path.join(os.getcwd(), 'app', 'weights.pth')))
    transform = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])
    
    img = Image.open(image)
    input = transform(img)
    input = input.unsqueeze(0)
    model.eval()
    output = model(input)
    print(output)
    return output
