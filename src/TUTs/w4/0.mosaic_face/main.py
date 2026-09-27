import cv2


def mosaic_face(img):
    faceCascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml');
    gray_face = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY); 
    faces = faceCascade.detectMultiScale(gray_face, 1.3, 5);
    for (x, y, w, h) in faces:
        # cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
        # 拿到了'脸部匹配框', 就先把它裁剪出来
        print(f"选区坐标y: {y}-{y+h}, x: {x}-{x+w}, 选区高:{h}, 选区长:{w}");
        cropped_face = img[y:y+h, x:x+w];

        # 自已研究出来的'模糊方案' (有点'高斯模糊'的效果XD)
        down_scaled_face = cv2.resize(cropped_face, (10,10));
        re_upscaled_face = cv2.resize(down_scaled_face,(w,h), interpolation=cv2.INTER_NEAREST); # 马赛克关键: 这里的'插值算法'用'复制内邻'

        # 习题中的参考答案
        s = 10
        # down_scaled_face = cropped_face[::s, ::s, :]; # 对'裁剪图'的高 & 长 每隔10px只保留1px, 最后的':'留全1px中的 3个BGR 元素值
        # re_upscaled_face = cv2.resize(down_scaled_face, (w, h),interpolation=cv2.INTER_NEAREST); # 重新放大, 利用'内部已有值复制'(INNER_NEAREST)
        
        # 替换原图的'人脸部分'
        img[y:y+h, x:x+w] = re_upscaled_face;

    return img;
    pass


if __name__ == "__main__":
    img = cv2.imread("tst1.jpg")
    copied_img = img.copy();
    result = mosaic_face(copied_img)
    cv2.imshow('original', img)
    cv2.imshow('mosaic', result)
    cv2.waitKey(0)
