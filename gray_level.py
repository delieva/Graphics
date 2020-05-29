from PIL import Image
import numpy as np
from numpy import array

im = array(Image.open('images/pizza.JPG').convert('L'))

def clamp(img, start_end):
    min_, max_ = start_end
    range_ = max_ - min_
    img = np.asarray(range_ / 255 * img + min_).astype(np.uint8)
    return img

clamp_image = Image.fromarray(clamp(im, (100, 200)))
clamp_image = clamp_image.rotate(270)
clamp_image.show()