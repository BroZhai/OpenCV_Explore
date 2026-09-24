import cv2
import numpy as np

# 以灰度图模式打开'方块9'
square = cv2.imread("square.png");
square_gray = cv2.cvtColor(square, cv2.COLOR_BGR2GRAY);

# 截选'图案模版'
template_pattern = square_gray[34:81, 29:87];

# 使用cv2.matchTemplate()进行'模版特征匹配'
## cv2.matchTemplate(灰度图Numpy数组, 截选的'图案模版', cv2.TM_CCOEFF_NORMED)
## 补充: 上面最后一个参数'cv2.TM_CCOEFF_NORMED'是将前面两个给定的Numpy数组"标准化"后再进行比较, 了解即可
# 这里返回的cofficient
match_coefficient = cv2.matchTemplate(square_gray, template_pattern, cv2.TM_CCOEFF_NORMED);
# 
locations = np.where(match_coefficient>=0.9);

w, h = template_pattern.shape[0:2];

for p in zip(*locations[::-1]):
    x1, y1 = p[0], p[1];
    x2, y2 = x1 + w, y1 + h;
    cv2.rectangle(square, (x1,y1), (x2, y2), (0,250,125), 1); # 在原图上面做标记

cv2.imshow("square", square);

cv2.waitKey();

