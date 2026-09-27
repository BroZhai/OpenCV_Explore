import cv2
import numpy as np

# 利用'局部教堂'图 和 '整体教堂'图 之间的'相似特征', 进行匹配

church = cv2.imread('church.jpg');
church_part = cv2.imread('church_part.jpg');

# 这个orb可以简单理解成一个'特征提取机', 这里先对其创建 & 初始化
orb = cv2.ORB_create();

# 提取 '整体教堂' & '局部教堂' 的特征点 + 指纹 (这个相当于"找特征": 识别纯色, 边界, 角点)
kp1, des1 = orb.detectAndCompute(church, None);
kp2, des2 = orb.detectAndCompute(church_part, None);

# 下面的操作主要就是利用'局部教堂' 的特征 + 指纹 看看和 '整体教堂'的哪些对应'特征+指纹'相似
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True); # 创建一个'暴力匹配器', 准备匹配进行'局部图' & '整体' 的特征匹配

matches = bf.match(des1,des2) # 进行'局部图' & '整体' 的特征匹配, 得出'匹配点' matches
matches = sorted(matches, key = lambda x:x.distance) # 对匹配结果按'距离'(匹配程度)排序, 距离(差距)从小到大排

# 最终画出匹配结果
matched_img = cv2.drawMatches(church, kp1, church_part, kp2, matches[:50], None)

cv2.imshow("matches", matched_img);
cv2.imwrite("matches.png", matched_img);

cv2.waitKey();