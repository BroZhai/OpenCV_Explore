import cv2

# 这个程序我们来看看图像'特征'的提取
"""
什么是'图像特征'?
简单来说, 我们会用一个小小矩形来对图片进行检测, 观察矩形内的像素在 x, y 方向上的'变化'
因此我们可以把图像特征分为'3类' (见'特征说明图.png')
- 平面: '小矩形'在x, y 方向上变动时, 内部像素在x, y方向上 都没有任何变化/ 基本相同 (如'纯色区', 图案排布相同的区域)
- 边界: '小矩形'在x, y 方向上变动时, 内部像素在x, y方向的'其中一个方向上'变化明显 (如'水平边界'在x方向上变化不大, 但是在y方向上'变化巨大')
- 角点: '小矩形'在x, y 方向上变动时, 内部像素在x, y两个方向的'变化都明显' (如物体的'角落', 因此又被称为'角点')=
"""

cat = cv2.imread('target.jpeg');
cat_gray = cv2.cvtColor(cat, cv2.COLOR_BGR2GRAY); # 将图片转成'灰度图', 便于分析'像素在x, y 上的变化'

# 使用Shi-Tomasi 角点检测算法 对图中的'角点'进行检测
# cv2.goodFeaturesToTrack(输入灰度图Numpy数组, 最多返回多少个角点, 质量等级(0-1), 点与点之间的最小'欧式距离') 
# 会返回找到的'角点坐标集合', 一会儿用for循环去遍历拿每个'角点坐标'
## 补充: '欧式距离': 如果有两个角点距离 < 10，只保留质量更好的那个 (确定了两个角点间的距离 > 10, 和'非极大值抑制'是一个思想)
corners = cv2.goodFeaturesToTrack(cat_gray, 500, 0.1, 10);


for corner in corners:
    x, y = corner.ravel(); # 遍历拿到每个'角点坐标'
    cv2.circle(cat, (int(x), int(y)), 3, (0,0,255), -1); # 这里是之前'3.简单画画'的内容, 这里是用corners找出来的'x,y坐标', 画出半径为3的'红色实心圆'

cv2.imshow("corners", cat);
cv2.imwrite("identified_features.png", cat);

cv2.waitKey();