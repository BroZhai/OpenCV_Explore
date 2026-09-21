import cv2
import numpy as np # 会使用numpy来'创建画布' (创建'三维矩阵')

# 简单玩转一下cv2内置的'画画'功能 (画线段, 形状, 以及简单文字)

canvas = np.zeros([300, 300, 3], dtype=np.uint8); # 创建一个宽 & 高都是300的画布, 颜色通道为3 (dtype限定每个数值的类型是'无符号8位整数', 范围0-255)
# cv2.line()画线: (numpy数组对象(创建的画板), (x,y起始坐标), (x,y终点坐标), (线段B, G, R颜色), 线条粗细)
cv2.line(canvas, (200,150), (250, 250), (0,0,255), 3);

# cv2.rectangle(numpy数组对象, (x,y终点坐标), (线段B, G, R颜色), 线条粗细))
# Tips: 这里的'线条粗细'可以填'-1', 表示"实心填充"
cv2.rectangle(canvas,(30,100),(130,200), (255,0,0), 2);
cv2.rectangle(canvas,(150,100),(250,150), (0,255,0), -1);

# cv2.circle(numpy数组对象, (x,y圆心坐标), 半径, (线段B, G, R颜色), 线条粗细))
cv2.circle(canvas, (50,50), 35, (125,125,0), 3);

# cv2.putText(numpy数组对象, "文字内容", 文字左下角坐标, 字体序号, 字体缩放倍率, (字体B, G, R), 字体粗细);
cv2.putText(canvas, "Welcome to OpenCV!", (10,40), 0, 1, (255,255,255), 2);

cv2.imshow("drawing_canvas", canvas);
cv2.imwrite("drawing_canvas.png", canvas);

cv2.waitKey();