import cv2
import numpy as np
from google.colab.patches import cv2_imshow

def gamma_donusturme(src, gamma):

    gamma_kuvveti = 1 / gamma

    table = [((i / 255) ** gamma_kuvveti) * 255 for i in range(256)]

    table = np.array(table, np.uint8)

    return cv2.LUT(src, table)


gorsel = cv2.imread('gorsel.png')

gamma_gorsel1 = gamma_donusturme(gorsel, 3.0)

gamma_gorsel2 = gamma_donusturme(gorsel, 4.0)

gamma_gorsel3 = gamma_donusturme(gorsel, 5.0)



cv2.putText(gamma_gorsel1, "g={3.0}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)
cv2.putText(gamma_gorsel2, "g={4.0}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)
cv2.putText(gamma_gorsel3, "g={5.0}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)


cv2_imshow(np.hstack((img,gamma_gorsel1,gamma_gorsel2,gamma_gorsel3)))