import cv2
import numpy as np

# flag = cv2.COLOR_BGR2RGB # Change colorspace BGR->RGB 
flag = cv2.COLOR_BGR2GRAY
# flag = cv2.COLOR_BGR2HSV
gray_cat = cv2.cvtColor(cat, flag)

# cv2.imshow('Hajimi', cat)
# cv2.imshow('Hajimi', gray_cat)

coin_img = cv2.imread('coins.jpg')
coin_img = cv2.GaussianBlur(coin_img, (7,7), 0)

# each row is now a vector in the 3-D space of RGB
vectorized = coin_img.reshape(-1, 3)
# convert the unit8 values to float (cv2.kmeans requirement)
vectorized = np.float32(vectorized)

## k-means algorithm
# define stopping criteria
segments = 2;
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0);

# OpenCV k-means function
ret, label, center = cv2.kmeans(vectorized, segments, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS);

cv2.show("segemented label", label);
# assign every pixel with a color based on the label map
res = center[label.flatten()];
# reshape to image size
segmented_map = res.reshape((coin_img.shape));
result = segmented_map.astype(np.uint8);
cv2.imshow('segemented coins', result);

# 显示图片
# cv2.imshow('Blurred Coins', coin_img)

# 等待按键，再关闭窗口
cv2.waitKey(0)
cv2.destroyAllWindows()

