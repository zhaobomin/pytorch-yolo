import cv2
import sys

videoCapture = cv2.VideoCapture(sys.argv[1])
t = int(sys.argv[2])

# 获得码率及尺寸
fps = videoCapture.get(cv2.CAP_PROP_FPS)
size = (int(videoCapture.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(videoCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
fNUMS = videoCapture.get(cv2.CAP_PROP_FRAME_COUNT)

print('CAP_PROP_FRAME_COUNT:', fNUMS)

for i in range(t):
    for j in range(int(fps*10)):
        success, frame = videoCapture.read()  # 获取下一帧
    cv2.imwrite('img-%d.png' % i, frame)  # 显示


videoCapture.release()
