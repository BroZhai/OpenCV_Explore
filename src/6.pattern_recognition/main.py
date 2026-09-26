import cv2
import numpy as np

# 以灰度图模式打开'方块9'
square = cv2.imread("square.png");
square_gray = cv2.cvtColor(square, cv2.COLOR_BGR2GRAY);

# 截选'图案模版'
## 注: 这里 打开图像的三维Numpy数字中, 第一个是'图像高'(y范围), 第二个是'图像长'(x范围), 不是[x, y]是[y, x]!
# 我们截取的选区为原图的 y: 29到 y: 87, x:34到 x:81, (选区 高58, 长47)
template_pattern = square_gray[29:87, 34:81]; # [原图y切割范围, 原图x切割范围], 返回一个新的'Numpy数组' (纯'模版图片')
# cv2.imshow("template_pattern", template_pattern);

# 使用cv2.matchTemplate()进行'模版特征匹配' (.matchTemplate()只支持'灰度图'/单通道输入)
## cv2.matchTemplate(灰度图Numpy数组, 截选的'图案模版', cv2.TM_CCOEFF_NORMED)
## 补充: 上面最后一个参数'cv2.TM_CCOEFF_NORMED'是将前面两个给定的Numpy数组"标准化"后再进行比较, 了解即可
"""
匹配过程: 利用给定的'图案模版大小'创建一个'扫描框', 将这个'扫描框'放在原图中的'每个组标点'进行扫描 (又叫"滑动匹配"), 得出各个'扫描框'(匹配区) 和 '给定模版'的相似度
最终返回一个'Numpy二维数组', 即是下面的'match_coefficient'
其中包含了'扫描框'在原图中'每个x,y坐标'的'扫描框'匹配得分
e.g., score = match_coefficient[94, 34]; ==> 扫描框在原图 (34, 94)坐标处, 与'模版图'的相似程度(分数, 区间为 -1.0 - 1.0)
"""
match_coefficient = cv2.matchTemplate(square_gray, template_pattern, cv2.TM_CCOEFF_NORMED);
print(f"扫描框在原图中(y:94, x:34)处和模版的匹配程度为: {match_coefficient[94,34]} 分"); # PS画出来的一个框, 理论上应该和模版'完全一样'

# 将所有的'扫描框'匹配得分 > 0.95 的 (y,x)坐标集合 过滤筛查出来 
locations = np.where(match_coefficient>=0.98);
# print(locations);

# 此处对原来的'匹配模版'(template_pattern) 只要它的'高' 和 '长' (前两个元素) (这里的'template_pattern'本身就已经是'灰度图'了, 它的.shape只有(高, 长), 所以[:2]可选)
h,w  = template_pattern.shape[:2];
# print(template_pattern.shape); 
# print(f"取出来的h: {h}, w:{w}");

# 遍历 '匹配点'起始坐标, 利用'图案模版'的长度 画出循环画出'每个匹配框' (内部匹配分数>0.95)
for p in zip(*locations[::-1]):
    # Tips: 在python中, 使用列表/元组[::-1]表示内部(表层)元素全部'顺序调转' (如 tp = ((3,4), (2,1)), tp[::-1] = ((2,1), (3,4)))
    # 这里是先把原来的'y, x'轴数据转成 'x, y'轴数据
    # 随后使用 zip函数将两个数组中的 'x,y'坐标 依次关联起来 
    # 如 array_1 = (a,b,c), array_2 = (1,2 3); zip(array_1, array_2) ==> ((a,1), (b,2), (c,3))
    # (Tips: zip需要'两个或以上的数组'作为输入以关联数据, 这里我们用'*'将location拆成'两个数组'作为给zip()作为输入)

    x1, y1 = p[0], p[1]; # 将每个匹配的(x,y)起始坐标做记录
    x2, y2 = x1 + w, y1 + h; # 利用匹配的'起始坐标' + '图按模版'的长宽 得到 '画图终点坐标' (x2, y2) --> 得到'匹配框'的完整大小 (x1至x2, y1至y2);
    cv2.rectangle(square, (x1,y1), (x2, y2), (0,250,125), 1); # 利用上面得到的两对坐标, 用矩形画出'匹配框'
    # Tips: 同一位置'附近'存在多个'类似坐标值'(多个连续的匹配框分数都 > 0.95), 所以看起来画的矩形会有点'厚' (可以在27行 调整不同的 '匹配分数' 来观察矩形的"粗细变化")

cv2.imshow("square", square);

cv2.waitKey();

