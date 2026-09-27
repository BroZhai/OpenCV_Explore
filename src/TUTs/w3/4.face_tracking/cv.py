import cv2

# 对视频中的人脸进行追踪
"""
大致思路:
1. 读取OpenCV提前训练好的'人脸判断标准'
2. 对视频中的'每一帧'进行人脸识别 (特征匹配), 画'匹配框'
3. 将'匹配框'画在视频的每一帧后, 最后输出视频
"""

# 读取一个'人脸长什么样'的数据集 (人脸检测模版)
faceCascade = cv2.CascadeClassifier("./haarcascades/haarcascade_frontalface_default.xml");

# use camera
# video_capture = cv2.VideoCapture(0)

# 载入'输入视频'
video_capture = cv2.VideoCapture('input.mp4')
fourcc = cv2.VideoWriter_fourcc(*'mp4v') # 设置'输入 & 输出视频'的编码格式 (确保在读入和输出时一致)
out = cv2.VideoWriter('output.mp4',fourcc, 20.0, (160,112)) # 输出'输出视频'的'输出模版' (输出名称, 编码格式, 输出码率, 输出视频大小);
# 这里的out就相当于一个'带输出序列' (和输入视频的参数一致), 准备被各种'处理的画面帧'填满

# 逐帧循环处理
while True:
    # 
    ret, frame = video_capture.read()
    if frame is None: # 没有读到'下一帧' (视频读完了)
        break # 退出
    
    # 人脸识别 & 画框 部分
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # 将当前输入帧转成'灰度图'
    faces = faceCascade.detectMultiScale(gray, 1.3, 5) # 使用'人脸检测模版'对当前中的'人脸'进行识别
    # 对于每个'成功检测到人脸'的画面, 返回的faces对象 即为 '匹配框' (匹配框x坐标, y坐标, 框长度, 框高度)

    # 将当前帧中的'人脸匹配框'画出来 (这里的'匹配框'可能有多个, 所以调用for循环 反复画"邻近匹配框")
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # 画完框后, 将当前'处理好的帧'写到'输出序列'(out)中
    ## 细节: out输出序列在创建时就'已经是一个视频'了, 但是没有任何'帧', 这里我们就把'内容'一帧帧的从后面插进去 (写视频内容的操作就在此)
    out.write(frame)

# 释放视频'读取序列' & '输出序列' (释放资源)
video_capture.release()
out.release()


cv2.waitKey();


