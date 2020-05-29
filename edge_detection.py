import cv2
from skimage import img_as_int, img_as_ubyte
from PIL import Image
import scipy.ndimage.filters as flt
import numpy as np

img_gray = img_as_int(cv2.imread('images/palm.jpg', 0))
sobel_vertical = np.array([
    [0, 0, 0],
    [0, 0, 0],
    [-0.5, 0, 0.5]
])
edged_img = Image.fromarray(flt.convolve(img_gray, sobel_vertical))
sobel_horizontal = sobel_vertical.T
edged_img_v = Image.fromarray(flt.convolve(img_gray, sobel_horizontal))

img_gray = cv2.imread('images/palm.jpg', 0)

sobel_x = cv2.Sobel(img_gray, -1, 1, 0, ksize=5)
sobel_y = cv2.Sobel(img_gray, -1, 0, 1, ksize=5)
sobel_x_img = Image.fromarray(sobel_x)
sobel_y_img = Image.fromarray(sobel_y)

edged_img.show()
edged_img_v.show()
sobel_x_img.show()
sobel_y_img.show()
