import cv2

# 直接读取'钟表'的灰度图
img = cv2.imread("clock.png", cv2.IMREAD_GRAYSCALE);

# 使用高斯二阶导cv2.Laplacian()来查找边缘
edge_1 = cv2.Laplacian(img, cv2.CV_64F); # 使用64位浮点类型(cv2.CV_64F)来存储 Laplacian计算出的结果

# 使用canny算法(目前最好的解决方案), 设置'边缘阈值'来判断 & 细化'结实的'边缘
edge_2 = cv2.Canny(img, 100, 150); # 设定边缘阈值在 (100 - 150), >150的为'结实边缘', <100的不算边缘, 介于100-150的再看(弱边缘)

cv2.imshow("Original Image", img);
cv2.imshow("Laplacian", edge_1);
cv2.imshow("Canny", edge_2); # 效果简直薄纱高斯二阶导 XD

cv2.imwrite("Laplacian_Edge.png", edge_1);
cv2.imwrite("Canny_Edge.png", edge_2);

cv2.waitKey();