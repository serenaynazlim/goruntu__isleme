import cv2
import numpy as np
from google.colab.patches import cv2_imshow

gorsel = cv2.imread('gorsel.png')

gorsel_negatif = 255 - gorsel

cv2_imshow(np.hstack((gorsel,gorsel_negatif)))