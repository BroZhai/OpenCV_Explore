import cv2
import numpy as np

# 以灰度图模式打开'方块9'
square = cv2.imread("square.png");
square_gray = cv2.cvtColor(square, cv2.COLOR_BGR2GRAY);

# 截选'图案模版'
template_pattern = square_gray[29:87, 34:81];

# 使用cv2.matchTemplate()进行'模版特征匹配' (.matchTemplate()只支持'灰度图'/单通道输入)
## cv2.matchTemplate(灰度图Numpy数组, 截选的'图案模版', cv2.TM_CCOEFF_NORMED)
## 补充: 上面最后一个参数'cv2.TM_CCOEFF_NORMED'是将前面两个给定的Numpy数组"标准化"后再进行比较, 了解即可
"""
匹配过程: 利用给定的'图案模版大小'创建一个'扫描框', 将这个'扫描框'放在原图中的'每个组标点'进行扫描 (又叫"滑动匹配"), 得出各个'扫描框'(匹配区) 和 '给定模版'的相似度
最终返回一个'Numpy二维数组', 即是下面的'match_coefficient'
其中包含了'扫描框'在原图中'每个x,y坐标'的'扫描框'匹配得分
e.g., score = match_coefficient[34, 94]; ==> 扫描框在原图 (34, 94)坐标处, 与'模版图'的相似程度(分数, 区间为 -1.0 - 1.0)
"""

match_coefficient = cv2.matchTemplate(square_gray, template_pattern, cv2.TM_CCOEFF_NORMED);
print(f"扫描框在原图中(34,94)处和模版的匹配程度为: {match_coefficient[94,34]} 分");

locations = np.where(match_coefficient>=0.9);

w, h = template_pattern.shape[:2];

for p in zip(*locations[::-1]):
    x1, y1 = p[0], p[1];
    x2, y2 = x1 + w, y1 + h;
    cv2.rectangle(square, (x1,y1), (x2, y2), (0,250,125), 1); # 在原图上面做标记

cv2.imshow("square", square);

cv2.waitKey();

