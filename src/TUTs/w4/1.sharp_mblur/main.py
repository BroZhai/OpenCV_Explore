import cv2
import numpy as np
# 任务: 给图片分别实现'锐化' & '运动模糊'

def sharpening(img):
    # INSERT YOUR CODE HERE
    # 创建一个 '锐化'的过滤器 (二维卷积小模版)
    sharpen_kernel = np.array([[-1,-1,-1],
                                [-1,9,-1],
                                [-1,-1,-1]]);
    # 既然都有'锐化'的过滤器了, 那么我们直接用cv2.filter2D()来应用这个'过滤器'(二维卷积)不就完了
    output = cv2.filter2D(img,-1, sharpen_kernel); # 这里的'-1'指代的是'图像深度', -1 表示 '和输入原图'一样
    return output;
    pass


def motion_blur(img):
    # INSERT YOUR CODE HERE
    # 和锐化的思路类似, 我们直接手搓一个'运动模糊'卷积核(过滤器)
    """
    运动模糊一般是'只有一个方向'的, 要么水平, 要么竖直
    这里给出一个'水平运动'模糊的卷积模版
    [ 0    0    0    0    0  ]
    [ 11   11   11   11   11 ]
    [ 0    0    0    0    0  ]
    对应的创建代码如下
    """
    size = 21
    motion_blur_kernel = np.zeros((size, size))
    motion_blur_kernel[size // 2, :] = 1.0          # 中间一行全是 1
    motion_blur_kernel /= size                      # 归一化 → 每个 0.2

    blured_img = cv2.filter2D(img,-1, motion_blur_kernel);
    return blured_img;
    pass


if __name__ == "__main__":
    img = cv2.imread("tst2.jpg")
    sharp_copy = img.copy();
    blur_copy = img.copy();
    result1 = sharpening(sharp_copy)
    result2 = motion_blur(blur_copy)

    cv2.imshow('original', img)
    cv2.imshow('sharpening', result1)
    cv2.imshow('motion blur', result2)
    cv2.waitKey(0)
