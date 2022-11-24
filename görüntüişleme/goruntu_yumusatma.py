import cv2
import numpy as np
from google.colab.patches import cv2_imshow
 
gorsel = cv2.imread('gorsel.png',1) 

gorsel1 = cv2.blur(gorsel,(5,5))

gorsel2 = cv2.boxFilter(gorsel,-1,(2,2),normalize=True) 

cv2_imshow(np.hstack((gorsel1,gorsel2)))