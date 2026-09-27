import cv2
import numpy as np

# 研究一下图像的'形态学' (腐蚀 & 膨胀操作)

# 首先读王小桃灰度图
img_gray = cv2.imread("base.jpg", cv2.IMREAD_GRAYSCALE);

# 使用以176为阈值获得'王小桃'的二值图 (cv2.THRESH_BINARY_INV 表示阈值"取反", 原来白变黑, 黑变白, 好观察'膨胀' & '腐蚀'的变化)
used_thresh, binary = cv2.threshold(img_gray, 176, 255, cv2.THRESH_BINARY_INV);

# 创建一个用于'腐蚀' & '膨胀' 的 kernel卷积 (特征: 元素全是'1'的卷积), 这里用 np.ones()创建一个 5x5 的'全1'卷积, 元素单位为uint8
kernel = np.ones((5,5), np.uint8);

# 使用 cv2.erode() / cv2.dilate() 对图片腐蚀 / 膨胀
## 语法 cv2.erode (灰度图/二值图, 卷积内核, (可选参数) iteration=重复处理次数); cv2.dilate()和前面的使用语法一致
erosion_img = cv2.erode(binary, kernel);
flatten_img = cv2.dilate(binary, kernel);


cv2.imwrite("binary.png", binary);
cv2.imwrite("erosion.png", erosion_img); # 可以观察到图片内容的'边边'被腐蚀了
cv2.imwrite("flatten.png", flatten_img); # 图片内容的'边边'膨胀了

cv2.waitKey();