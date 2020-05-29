import scipy.misc
import scipy.ndimage.filters as flt
from PIL import Image
import numpy as np

noisy = Image.open('images/train.jpg').convert('L')

kernel_grayscale = np.ones((5, 5)) / 25
kernel_color = np.ones((5, 5, 1)) / 25
kernel_img = Image.fromarray(flt.convolve(noisy, kernel_grayscale))
kernel_color = Image.fromarray(flt.convolve(Image.open('images/train.jpg'), kernel_color))

minimum = flt.minimum_filter(noisy, size=5, footprint=None, output=None, mode='reflect', cval=0.0, origin=0)
maximum = flt.maximum_filter(noisy, size=5, footprint=None, output=None, mode='reflect', cval=0.0, origin=0)
median = flt.median_filter(noisy, size=5, footprint=None, output=None, mode='reflect', cval=0.0, origin=0)

minimum_img = Image.fromarray(minimum)
maximum_img = Image.fromarray(maximum)
median_img = Image.fromarray(median)

minimum_img.show()
maximum_img.show()
median_img.show()
kernel_img.show()
kernel_color.show()