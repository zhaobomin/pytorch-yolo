import sys
import cv2
from model_yolo import yolo_model
from PIL import Image


cfg = 'weights/yolov3_hat/yolov3_hat.cfg'
weights = 'weights/yolov3_hat/yolov3_hat.weights'
names = 'weights/yolov3_hat/yolov3_hat.names'

cfg = 'weights/yolov4/yolov4-sam-mish.cfg'
weights = 'weights/yolov4/yolov4-sam-mish.weights'
names = 'weights/yolov4/coco.names'


cfg = 'weights/yolov3/yolov3.cfg'
weights = 'weights/yolov3/yolov3.weights'
names = 'weights/yolov3/coco.names'


cfg = 'weights/yolov4/yolov4.cfg'
weights = 'weights/yolov4/yolov4.weights'
names = 'weights/yolov4/coco.names'

img_size = 608

if __name__ == '__main__':

    img = cv2.imread(sys.argv[1])

    net = yolo_model.yolo_net(weights, cfg, img_size=img_size, clss_path=names)
    boxes = net.predict(img)
    print(boxes)
    imgout = net.draw_boxes(img, boxes)
    cv2.imwrite('docs/test/imgout.jpg', imgout)
