import cv2
import sys


def convert(size, box):
    dw = 1./(size[0])
    dh = 1./(size[1])
    x = (box[0] + box[1])/2.0 - 1
    y = (box[2] + box[3])/2.0 - 1
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x, y, w, h)


def convert_filename(img_name, data_dir='ccpd_data/'):
    img = cv2.imread(data_dir+img_name)
    h, w = img.shape[:2]
    #lbl = img_name.split('/')[-1].rsplit('.', 1)[0].split('-')[-3]
    # print(lbl)
    iname = img_name.rsplit('/', 1)[-1].rsplit('.', 1)[0].split('-')

    [leftUp, rightDown] = [[int(eel) for eel in el.split('&')]
                           for el in iname[2].split('_')]

    size = (w, h)

    box = (leftUp[0], leftUp[1], rightDown[0], rightDown[1])
    bb = convert(size, box)

    res = "0 " + " ".join([str(a) for a in bb]) + '\n'
    return res


image_files = open(sys.argv[1]).read().strip().split()

for img_name in image_files:
    img_idx = img_name.split('/')[-1].split('.')[0]
    out_file = open('ccpd_data/labels/%s.txt' % (img_idx), 'w')
    res = convert_filename(img_name)
    out_file.write(res)
