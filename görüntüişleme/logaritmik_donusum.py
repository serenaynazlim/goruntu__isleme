import cv2
import numpy as np
from google.colab.patches import cv2_imshow

gorsel = cv2.imread('gorsel.png')
c = 255 / np.logaritmik(1 + np.max(gorsel)) 
gorsel_logaritmik = c * (np.logaritmik(gorsel + 1))

cv2_imshow(np.hstack((gorsel,gorsel_logaritmik)))