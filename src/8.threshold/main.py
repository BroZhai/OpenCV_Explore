import cv2

# 阈值这个东西, 本质上和PS'调整图层'中的'阈值'效果是一样的: 规定一个'像素标准值', 随后对图像的每个像素进行'非黑即白'的分割 (和Canny算法保留'强边缘'的算法类似)
gray_pupu = cv2.imread("pupu.jpg", cv2.IMREAD_GRAYSCALE); # 以灰度图模式读取奇怪小猫
gray_keyboard = cv2.imread("keyboard.jpg", cv2.IMREAD_GRAYSCALE); # 灰度图

# 使用常规的cv2.threshold()来对图片进行'阈值分割'
# cv2.threshold(灰度图, 设定阈值, 最大像素(通常就是255), CV.THRESH_BINARY)
ret, pupu_binary = cv2.threshold(gray_pupu, 144, 255, cv2.THRESH_BINARY);
# 返回的两个数值: ret: 实际使用的阈值(144), pupu_binary: 黑白二值化后的图像 (二维数组, 外层有1024个数组(行), 内层有1536个元素(行中的像素值))
# 因为已经是'二值图'了, '行'中的每一个像素就是 0 或 255 的像素值
# print({pupu_binary.shape});
# print(len(pupu_binary))

ret, keyboard_binary =  cv2.threshold(gray_keyboard, 21, 255, cv2.THRESH_BINARY); # 这个图比较特殊, 图片有'亮区' 和'暗区', 导致不能找到一个'大一统'的阈值, 要么太亮, 要么太暗 (一会儿解决这个问题)
keyboard_binary_adaptive = cv2.adaptiveThreshold(gray_keyboard, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2);


# 分区'自适应'阈值算法
## 对于一些图片来说, 图片的不同区域'亮度信息'不一样, 因此每个区域的'亮度阈值'其实也应该是不一样的, 而不是用一个'大一统'的阈值
## 在opencv中, 它就给我们提供了这种 '分区亮度自适应'的阈值算法 --> cv2.adaptiveThreshold()

cv2.imshow("threshold_pupu", pupu_binary);
cv2.imshow("threshold_keyboard", keyboard_binary); # 可以看到直接用'大一统'阈值的效果要么太亮, 要么太暗 (原图问题, 没法修)
cv2.imshow("adaptive_threshold_keyboard", keyboard_binary_adaptive); # 可以看到整个图片以一个'均匀亮度'的形式读取了 (以'数字2键'为例, 前者过亮看不到, 后者每个数字都能清晰看到)
cv2.imwrite("threshold_pupu.png", pupu_binary);
cv2.imwrite("adaptive_threshold_keyboard.png", keyboard_binary_adaptive);
cv2.imwrite("threshold_keyboard.png", keyboard_binary);


cv2.waitKey();