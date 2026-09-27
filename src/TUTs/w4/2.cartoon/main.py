import cv2

# 任务: 把图片变得'卡通化' (模糊之后给部分边缘"加黑")

def cartoonize_image(img):
    # INSERT YOUR CODE HERE

    # 将图像转成灰度图
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY);
    # 应用均值滤波 平均模糊照片 (去噪点)
    gray_img = cv2.medianBlur(gray_img, 7)

    # 使用'高斯二阶导'滤波, 一键给图片(进一步)去噪 & 查找边缘
    edges = cv2.Laplacian(gray_img, cv2.CV_8U, ksize=5)
    # 精确化(细化)找到的'边缘' (非极值抑制)
    ret, mask = cv2.threshold(edges, 80, 255, cv2.THRESH_BINARY_INV)
    cv2.imshow('mask', mask) # 此时的 mask 就已经是'加粗'的边缘了


    sigma_color = 220
    sigma_space = 220
    size = 15

    # 使用BilateralFilter滤波器对原图进行处理 (效果: 保留图中'边缘'的同时, 模糊'内容区域')
    ## 这一步是将'原图'作为 'base底图', 简单模糊一下后准备 和 mask(加粗边缘图层)进行混合
    filtered_img = cv2.bilateralFilter(img, size, sigma_color, sigma_space)
    # cv2.imshow('filtered_img', filtered_img)

    # 利用cv2.bitwise_and()方法将 'base底图' 和 '加粗边缘图' 进行混合
    merged_img = cv2.bitwise_and(filtered_img, filtered_img, mask=mask)

    return merged_img; # 返回最终'混合好'的图
    # pass


if __name__ == "__main__":
    img = cv2.imread("tst3.jpg")
    cartoon_img = img.copy()
    result = cartoonize_image(cartoon_img)
    cv2.imshow('original', img)
    cv2.imshow('cartoonized', result)
    cv2.waitKey(0)
