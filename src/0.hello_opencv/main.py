import cv2
print(f"当前使用的OpenCV的版本是: {cv2.getVersionString()}");

# 图片的读取
niko = cv2.imread("Niko.png"); # cv2.imread() 函数会返回一个 Numpy数组对象, 默认会以BGR的三原色通道进行读取
night = cv2.imread("nightcore.jpg", cv2.IMREAD_GRAYSCALE); # 指定以'灰度图'的方式进行读取

# 这里返回的Numpy数组对象有三个数据(维度): (高度, 长度, 颜色通道数)
print(f"niko变量的数据类型是: {type(niko)}"); # numpy.ndarray
print(niko.shape);
print(night.shape); # 发现'颜色通道'消失了

# 展示所读取的图片 cv2.imshow('Windows窗口名称', Numpy数组对象)
# 注: '窗口名称'用中文会乱码 :|
cv2.imshow('Niko', niko); 
cv2.imshow('Logo', night);

cv2.waitKey(); # 上面'图片显示'的操作是瞬间的, 我们这里加一个'等待键盘输入'让进程卡住, 从而"一直显示图片"