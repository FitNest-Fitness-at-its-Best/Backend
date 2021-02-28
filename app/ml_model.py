import torch
import os

def get_image_name(image):
    model = torch.load(os.path.join(os.getcwd(), 'app', 'weights.pth'))
    output = model.eval(image)
    print(output)
    return output
