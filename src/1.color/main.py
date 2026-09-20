import cv2

ocv = cv2.imread('ocv.png');

# 分别提取图像的 R, G, B 三个颜色通道的'灰度图'强度信息
# 补充知识点: numpy数组的[:]表示要这个数组的'所有值', 下面的'数组排布' 参考第0个文件夹的中'bgr'打印的数组数据更好理解
# 注: 在颜色通道中, 强度越强, 灰度图越'亮'(白), 而'白色'始终都是三个颜色混合的'最强值' (255,255,255)

cv2.imshow("red_intensity", ocv[:,:,2]); # 要'所有行', '所有列' 但 '只有红色通道'的值(灰度图强度) --> 红色区域'纯白' (不考虑图片原本的'白色')
cv2.imshow("green_intensity", ocv[:,:,1]); # 同理, 绿色区域全白
cv2.imshow("blue_intensity", ocv[:,:,0]); # 蓝色区域全白

# Tips: 在不指定读取颜色的情况下, OpenCV默认用的是'BGR'读的颜色格式
# 我们也可以转成我们熟悉的RGB排布形式 [使用cv2.cvtColor()函数 和 cv2.COLOR_BGR2RGB常量]
ocv_rgb = cv2.cvtColor(ocv, cv2.COLOR_BGR2RGB);
# 这样一来, 现在ocv_rgb的[:,:,0]; 就是'红色灰度图'了, 显示的图片和上面的red_intensity应一致
cv2.imshow("rgb_r_intensity", ocv_rgb[:,:,0]);

cv2.waitKey();