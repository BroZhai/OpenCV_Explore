import cv2

# 对图像裁剪的原理其实很简单, 就是只取'指定范围内'的'像素坐标值'
# 得益于imread()返回的对象是个Numpy对象, 我们可以很方便的'直接操作'数组' (原理是截取数组的'部分')

niko = cv2.imread("niko.jpeg", cv2.COLOR_BGR2RGB); # 直接以RGB形式打开
cropped_niko = niko[65:450, 40:571]; # 裁剪原图的 纵坐标65-385(选区高), 横坐标40-571(选区长)

cv2.imshow("image_to_be_saved", cropped_niko);

# 输出图片
cv2.imwrite("cropped_niko.png", cropped_niko);

cv2.waitKey();