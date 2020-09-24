import sys
import cv2
from model_yolo import yolo_model
from PIL import Image


cfg = 'weights/yolo/yolov3.cfg'
weights = 'weights/yolo/yolov3.weights'
names = 'weights/yolo/coco.names'

cfg = 'weights/yolov3_hat/yolov3_hat.cfg'
weights = 'weights/yolov3_hat/yolov3_hat.weights'
names = 'weights/yolov3_hat/yolov3_hat.names'


if __name__ == '__main__':

    img = cv2.imread(sys.argv[1])

    net = yolo_model.yolo_net(weights, cfg, clss_path=names)
    boxes = net.predict(img)
    print(boxes)
    imgout = net.draw_boxes(img, boxes)
    cv2.imwrite('docs/test/imgout.jpg', imgout)
