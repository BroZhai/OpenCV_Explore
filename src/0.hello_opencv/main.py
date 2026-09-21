import cv2
print(f"当前使用的OpenCV的版本是: {cv2.getVersionString()}");

# 图片的读取
niko = cv2.imread("Niko.png"); # cv2.imread() 函数会返回一个 Numpy数组对象, 默认会以BGR的三原色通道进行读取
# 等价于 niko = cv2.imread("Niko.png", cv2.IMREAD_COLOR / 1)
night = cv2.imread("nightcore.jpg", cv2.IMREAD_GRAYSCALE); # 指定以'灰度图'的方式进行读取 (cv2.IMREAD_GRAYSCALE 也被写作 '0')
# 还有一种情况,图片是png, 包含ALpha透明通道, 此时用 "-1" 或 cv2.IMREAD_UNCHANGED 读取 (cv2.imread("xxx.png", -1))

bgr = cv2.imread("bgr.png");

# 这里返回的Numpy数组是个'三维数组':
# 第0维(最外层列表): 像素所处行数 (总元素数为'图像高')
# 第1维(中间列表): 像素所处列数 (总元素数为'图像长')
# 第2维(最内部列表): 这个像素的BGR通道 (注意不是'RGB'!)

print(f"niko变量的数据类型是: {type(niko)}"); # numpy.ndarray
print(niko.shape);
print(night.shape); # 发现'颜色通道'消失了

print(bgr);
"""
3x2 BGR图片底层3维数组排列:
[ # 第0维度: 包含 2 个数组(元素), 说明'图片高度'为2px
	[ # 这里为'第一行' (进入第1维度: 包含3个数组(元素), 说明'图片长度'为3px / 有3列)
		[204, 72, 63], # 第一行第一列的像素BGR通道信息 (204, 蓝色最强, 蓝)
  		[76, 177, 34], # 第一行第二列像素 (绿)
  		[36, 28, 237]  # 第一行第三列像素 (红)
	],

 	[ # 第二行
		[204, 72,  63], # 第二行第一列像素 (蓝)
		[76, 177,  34], # 第二行第二列像素 (绿)
		[36,  28, 237]  # 第二行第三列像素 (红)
	]
]

"""


# 展示所读取的图片 cv2.imshow('Windows窗口名称', Numpy数组对象)
# 注: '窗口名称'用中文会乱码 :|
cv2.imshow('Niko', niko); 
# cv2.imshow('Logo', night);

cv2.waitKey(); # 上面'图片显示'的操作是瞬间的, 我们这里加一个'等待键盘输入'让进程卡住, 从而"一直显示图片"