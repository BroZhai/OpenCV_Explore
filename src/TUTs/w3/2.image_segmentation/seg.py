import cv2
import numpy as np
from matplotlib import pyplot as plt

# 使用'分层'(Segmentation) 将硬币 和 背景区分出来, 输出为不同颜色的图层
# 大致思路: 1. 使用K-means clustering找到图中各种标志性的'中心点' (硬币圆心)

# 使用的'聚类算法'是 K-means clustering, 简单来说就是 先随便标几个'代表', 从'代表'向四周辐射找'类似的同类'聚在一起
## 每次更新后的(扩大)区域会"重新选代表", 直至'代表选不动' (找到'中心代表'了)为止

# 读图 & 应用高斯模糊滤波器
coins = cv2.imread("coins.jpg");
blured_coins = cv2.GaussianBlur(coins, (7,7), 0); # 使用高斯模糊(7x7的处理小模版, 模糊半径sigma=0 指的是让opencv自动帮你算 XD)

