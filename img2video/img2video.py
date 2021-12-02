import cv2
import os

# configs
img_dir = "path to image dir"
num = 21
fps = 30
img = cv2.imread(os.path.join(img_dir, '0.jpg'))
h, w = img.shape[0:2]
size = (w, h)

# video_writer
video = cv2.VideoWriter('demo.mp4', cv2.VideoWriter_fourcc(*'mp4v'), fps, size)

# params introduction
"""
参数1 即将保存的文件路径
参数2 VideoWriter_fourcc为视频编解码器
    fourcc意为四字符代码（Four-Character Codes），顾名思义，该编码由四个字符组成,下面是VideoWriter_fourcc对象一些常用的参数,注意：字符顺序不能弄混
    cv2.VideoWriter_fourcc('I', '4', '2', '0'),该参数是YUV编码类型，文件名后缀为.avi 
    cv2.VideoWriter_fourcc('P', 'I', 'M', 'I'),该参数是MPEG-1编码类型，文件名后缀为.avi 
    cv2.VideoWriter_fourcc('X', 'V', 'I', 'D'),该参数是MPEG-4编码类型，文件名后缀为.avi 
    cv2.VideoWriter_fourcc('T', 'H', 'E', 'O'),该参数是Ogg Vorbis,文件名后缀为.ogv 
    cv2.VideoWriter_fourcc('F', 'L', 'V', '1'),该参数是Flash视频，文件名后缀为.flv
    cv2.VideoWriter_fourcc('m', 'p', '4', 'v')    文件名后缀为.mp4
参数3 为帧播放速率
参数4 (width,height)为视频帧大小
"""

for i in range(num):
    img_path = os.path.join(img_dir, str(i)+'.jpg')
    img = cv2.imread(img_path)
    print(img.shape)
    video.write(img)

video.release()
