import cv2
import numpy as np
# print(cv2.__version__)

# 灰白哈基米任务
cat = cv2.imread('cat.jpg', 1) # colorful, BGR 等效于 cv2.imread('cat.jpg', cv2.IMREAD_COLOR_BGR)
# image = cv2.imread('cat.jpg', 0) # gray-scale 也可用 cv2.IMREAD_GRAYSCALE
# image = cv2.imread('cat.png', -1) # unchanged, e.g., png带'透明背景'的用这个读

gray_cat = cv2.cvtColor(cat, cv2.COLOR_BGR2GRAY);
cv2.imshow("gray cat", gray_cat);

cv2.imwrite('gray_cat.jpg', gray_cat);
cv2.waitKey();