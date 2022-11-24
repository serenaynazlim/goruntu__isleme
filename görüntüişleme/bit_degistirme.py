import cv2
import numpy as np
from matplotlib import pyplot as plot
from google.colab.patches import cv2_imshow

# Resmi yükleme
gorsel = cv2.imread('gorsel.png',cv2.IMREAD_GRAYSCALE)

gorsel8=gorsel/(255/8)
gorsel16=gorsel/(255/16)
gorsel24=gorsel/(255/24)

cv2.putText(gorsel8, "bit=8", (15, 45), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (220, 220, 220), 3)
cv2.putText(gorsel16, "bit=16", (15, 45), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (220, 220, 220), 3)
cv2.putText(gorsel24, "bit=24", (15, 45), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (220, 220, 220), 3)

cv2_imshow(np.hstack((gorsel,gorsel8,gorsel16,gorsel24)))

plot_org=plot.hist(gorsel.ravel(),256,[0,256]);
plot_8=plot.hist(gorsel8.ravel(),256,[0,256]);
plot_16=plot.hist(gorsel16.ravel(),256,[0,256]);
plot_24=plot.hist(gorsel24.ravel(),256,[0,256]);