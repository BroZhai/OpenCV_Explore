import cv2
import numpy as np

# 利用'局部教堂'图 和 '整体教堂'图 之间的'相似特征', 进行匹配

church = cv2.imread('church.jpg');
church_part = cv2.imread('church_part.jpg');

# 这个orb可以简单理解成一个'特征提取机', 这里先对其创建 & 初始化
orb = cv2.ORB_create();

# 提取 '整体教堂' & '局部教堂' 的特征点 + 指纹
kp1, des1 = orb.detectAndCompute(church, None);
kp2, des2 = orb.detectAndCompute(church_part, None);

cv2.imshow();

cv2.waitKey();