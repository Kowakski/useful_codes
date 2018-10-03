import cv2

videoCapture = cv2.VideoCapture()
videoCapture.open(r"D:\PRIV\useful_codes\dinasor2.mp4")

fps = videoCapture.get(cv2.CAP_PROP_FPS)
frames = videoCapture.get(cv2.CAP_PROP_FRAME_COUNT)
#fps是帧率，意思是每一秒刷新图片的数量，frames是一整段视频中总的图片数量。
print("fps=",fps,"frames=",frames)

j=235
for i in range(int(frames)):
    ret,frame = videoCapture.read()
    if i%5 == 0:
        cv2.imwrite(r"D:\PRIV\useful_codes\imgs\tyrannosaurus%d.jpg"%j,frame)
        j = j+1