import cv2

noise_img = cv2.imread("noise.png", cv2.COLOR_BGR2RGB);

# 我们来研究一下各种'滤波器' filter的使用方式

## 高斯滤波器 (高斯核)
# cv2.GaussianBlur(Numpy数组, ksize核大小(长, 宽)['小模版'矩阵大小], sigma 𝜎[模糊半径/程度], )
"""
(补充) 
1. sigma值类比: 飞在空中的'高度' (高度越高, 看到的'地面细节'越少, 反之亦然)
2. 如果simga 填 0, OpenCV会"自动帮你算"最佳sigma值, 而不是"不处理" XD
3. 高斯'小模版'的大小可以是'长方形', 所以ksize强制让我们填'小模版长 & 宽'
"""
gaussed_img1 = cv2.GaussianBlur(noise_img, (5,5), 0); # 高斯'小模版'大小为5x5, 模糊半径sigma为0 (交给OpenCV自己算)
# gaussed_img2 = cv2.GaussianBlur(noise_img, (5,5), 2);
# gaussed_img3 = cv2.GaussianBlur(noise_img, (5,5), 4);
# gaussed_img4 = cv2.GaussianBlur(noise_img, (5,5), 6);

## 中值滤波器 (Median Filter, 注意不是'均值滤波'! )
# 原理: 将'小模版'中的像素排序, 最后直接取'中位数'当结果
# cv2.medianBlur(Numpy数组, ksize'小模版大小')  [注: 对于.medianBlur(), ksize'小模版大小'只填一个数即可, OpenCV会自动转成 'A x A'的矩阵]
median_img = cv2.medianBlur(noise_img, 5);

cv2.imshow("original_noise", noise_img);
cv2.imshow("gaussed_img1", gaussed_img1); # 可以看到OpenCV自己算出来的高斯滤波'效果还ok', 但是噪点还是有点, 且'图像细节'被破坏了(模糊的'通病' XD)
cv2.imshow("median_img", median_img); # 虽然噪点去除程度比高斯明显, 但'细节损失的更多了' XD 
# cv2.imshow("gaussed_img2", gaussed_img2);
# cv2.imshow("gaussed_img3", gaussed_img3);
# cv2.imshow("gaussed_img4", gaussed_img4);

cv2.imwrite("gaussed_img.png", gaussed_img1);
cv2.imwrite("median_img.png", median_img);
cv2.waitKey();