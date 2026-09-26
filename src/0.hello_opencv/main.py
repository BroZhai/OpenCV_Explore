import cv2
import numpy as np
print(f"当前使用的OpenCV的版本是: {cv2.getVersionString()}");

# 图片的读取
niko = cv2.imread("Niko.png"); # cv2.imread() 函数会返回一个 Numpy数组对象, 默认会以BGR的三原色通道进行读取
# 等价于 niko = cv2.imread("Niko.png", cv2.IMREAD_COLOR / 1)
night = cv2.imread("nightcore.jpg", cv2.IMREAD_GRAYSCALE); # 指定以'灰度图'的方式进行读取 (cv2.IMREAD_GRAYSCALE 也被写作 '0')
# 还有一种情况,图片是png, 包含ALpha透明通道, 此时用 "-1" 或 cv2.IMREAD_UNCHANGED 读取 (cv2.imread("xxx.png", -1))

bgr = cv2.imread("bgr.png");

# 这里返回的Numpy数组是个'三维数组':
# 第0维(最外层列表): 像素所处行数 (总元素数为'图像高', y)
# 第1维(中间列表): 像素所处列数 (总元素数为'图像长', x)
# 第2维(最内部列表): 这个像素的BGR通道 (注意不是'RGB'!)

print(f"niko变量的数据类型是: {type(niko)}"); # numpy.ndarray

# (★)读取的'图片对象'(Numpy ndarray) 常用属性 & 方法
## .shape 图片的'尺寸信息', 返回一个'元组'即表示'图片(高, 长, 通道数)' (如果已经是'灰度图'的话则不会有'通道数')
print(f"niko.png的高度为: {niko.shape[0]}, 长度为: {niko.shape[1]}")
print(f"使用直接调用.shape属性得元组表示: {niko.shape}"); # 

## .size 图片的 高 x 长 x 通道数 (其实就是.shape中的所有元素相乘)
print(f"图片niko.size 的值为(高x长x通道数): {niko.size}, 其中 高x长 的总像素数为: {niko.shape[0] * niko.shape[1]}");

## .ndim 看图片的'维度' (灰度图=2, 彩图=3)
print(f"niko.png的维度为{niko.ndim}") # BGR彩图, 3
print(f"night.jpg的维度为{night.ndim}") # 读的时候用的就是灰度图, 2

## .copy() 创建一个完全独立的'深拷贝' (在新的内存区域放'复制的图像', 视为一个'独立对象')
independent_night = night.copy(); # 对independent_night的任何修改都不会原来的影响到原来的'night'

## .flatten() 将图像自身(多维数组) 全部展开成'一维数组'
print(bgr.flatten());

## .reshape() 
# 详情见 ./hello_numpy中的研究例子
## 在opencv中, 我们常用其'-1自动算'占位符来直接算某些值 (e.g., 用二维数组表示 niko彩图'每个通道'的总像素数 [B通道总像素集合, G通道总像素集合, R通道总像素集合])
# 思路: 我们知道niko.shape(彩图)是个三维数组(见下方'bgr'示例), 高900, 长1200, 3个通道
# 我们要将前面的'高' 和 '长'两个数组展开成'一个数组', 而后面的'3通道'不变(突破口)
# 给定'3个通道', 二维数组就'只差一个值', 所以可以直接用'-1'表示差的那个值, 让Numpy自己算

print(f"niko.shape: {niko.shape}"); # niko.shape = (900, 1200, 3);
conbined_niko = niko.reshape(-1,3); # 这里reshape()后的niko变成了二维数组, 具体展开如下所示
"""
conbined_niko.shape (H*W, 通道数3); 前面的h*w用上面的'-1'算出来的 (900*1200)
conbined_niko.shape = (900*1200, 3) = (1080000, 3); 
"""
print(f"niko.reshape后的conbined_niko.shape: {conbined_niko.shape}"); # (1080000, 3)
print()




print('=======================================');

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