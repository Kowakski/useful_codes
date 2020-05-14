'''
从视频当中获取图片
'''
import cv2

videoCapture = cv2.VideoCapture()
videoCapture.open(r"D:\PRIV\Mydata\privdata\VID_20181110_131824.mp4")

fps = videoCapture.get(cv2.CAP_PROP_FPS)
frames = videoCapture.get(cv2.CAP_PROP_FRAME_COUNT)
#fps是帧率，意思是每一秒刷新图片的数量，frames是一整段视频中总的图片数量。
print("fps=",fps,"frames=",frames)

j=527    #从这个号开始编号
interval = 5   #间隔这么多张采集一张
for i in range(j*interval, j*interval + int(frames)):
    # print( "{} {} {}".format( j*interval, j*interval+int( frames ) , i) )
    ret,frame = videoCapture.read()
    if i%interval == 0:
        cv2.imwrite(r"D:\PRIV\Mydata\privdata\image\%06d.jpg"%(i/interval),frame)
        # print( "index {}".format( i/interval ) )