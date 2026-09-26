import cv2
import numpy as np
from matplotlib import pyplot as plt

# 使用'分层'(Segmentation) 将硬币 和 背景区分出来, 输出为不同颜色的图层
""" 
大致思路: 
1. 将原图搞点高斯模糊, 便于一会儿的'分层'
2. 将原图的'x,y'信息全部丢掉, 直接用个'一维数组'顺序表示原图的'每个像素' (暂且称为'像素序列')
3. 设定一些K-means的参数, 让其在'像素序列'中找到'指定分层'中'有代表的点' (如分了两个层, 一个层的代表是'白色背景', 另一个层的代表是'棕色硬币', K-Mean算法会慢慢推出'这两个代表的特征' & 对'像素序列'的每个像素'分类打标签')
4. 依据K-means给每个像素'打好的标签', 还原其'代表颜色'(center[label.flatten()]), 随后再使用'原图的shape'(原图空间信息) 来 将'标签色图'还原成原图 (得到原图大小的'分层图')
"""

# 使用的'聚类算法'是 K-means clustering, 简单来说就是 先随便标几个'代表', 从'代表'向四周辐射找'类似的同类'聚在一起
## 每次更新后的(扩大)区域会"重新选代表", 直至'代表选不动' (找到'中心代表'了)为止

# 读图 & 应用高斯模糊滤波器
coins = cv2.imread("coins.jpg");
print(f"coins.shape为{coins.shape}, 其总像素数为: {(coins.reshape(-1, 3).shape[0])}");
blured_coins = cv2.GaussianBlur(coins, (7,7), 0); # 使用高斯模糊(7x7的处理小模版, 模糊半径sigma=0 指的是让opencv自动帮你算 XD)

# 将图片变成'像素点云' (将每个像素的'BGR'值全部提取出来, 不再关心其x,y坐标(丢掉空间特征), 于是下方便用了coins.reshape(-1,3)来"摘出所有像素")
# 一会要用的kmeans算法只能能读 (总计像素数, 通道数) 这种shape, 所以这里要将原来的彩图reshape转化 
vectorized = coins.reshape(-1,3);
vectorized = np.float32(vectorized);

segment_layers = 2; # 定义'分层数'
# 定义一个'停止条件'(元组), 用于告诉一会儿的K-means 到什么程度可以停
## (停止的'条件类型'(可有多个, 用'+'相连), 最大迭代次数, 精度阈值)
"""
在K-means算法中, 算法的每一轮都会找一个'新的核心代表', 而这其中
最大迭代次数: 这个'找新代表'的过程最多重复发生几次?
精度阈值: 每次代表发生变动时, 统计'上一个代表'和 本轮准到的'新代表'之间的'距离'变动了多少 (如果 变动距离 < 精度阈值, 视为'原地踏步', 可以停止了 XD)
"""
stop_criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0); # 使用'精度阈值' + '最大迭代次数', 最大10次迭代, 精度阈值设为1

# 正式使用 OpenCV k-means 方法开始找'核心代表', 会返回3个变量
"""
- ret: 聚类的整体'紧不紧密'
- label: 每个像素属于'哪一类'
- center: 每一类的最终'代表颜色'是什么 ()
"""
ret, label, center = cv2.kmeans(vectorized, segment_layers, None, stop_criteria, 10, cv2.KMEANS_RANDOM_CENTERS);
print(len(label)); # 每个像素都有一个独立的标签
# print(label[8*150+40]); # 第8行第40列的像素为'棕色'(标签0), 而第8行41列的像素为'白色'(标签1) [★我们就用这个检测出来的'0/1标签'来还原'原图']
# print(center); # 标签0的代表色: [ 65.17441 90.087425 105.69899 ];  标签1的代表色: [227.31425  233.84793  232.54248 ]

res = center[label.flatten()]; # 将所有的'已分类标签' 全部砸成一个一维数组 ([[1], [1], [0], [0], [1], ...] --> [1,1,0,0,1,...])
# 再展平'标签数组'后, 直接将其用在center中, 去到对应的'代表颜色'(将所有的'标签值'变成了'具体代表颜色'值), 最终得到赋值给左侧的res变量; 这样左边的res就是一连串的'像素值'了 (没有x,y 空间信息)

# 既然 res 没有空间信息, 那么我们直接以'原图的shape'为参考, 将res"照原图分布"不就完了?
segmented_map = res.reshape((coins.shape)); # 使用原图的shape(185,150,3)参数 将 'res'二项标签色数组 进行重构 (还原成'原图大小'的segment图)
result = segmented_map.astype(np.uint8); # cv2.imwrite() 和 cv2.imshow() 要求数组的'数据类型'必须是'uint8', 进行强制类型转换

# 最终输出显示 & 保存 分层图
cv2.imshow("result",result);
cv2.imwrite("segmented_coins.png", result);

cv2.waitKey();