'''
def detect_img(yolo):
    while True:
        img = input('Input image filename:')
        try:
            image = Image.open(img)
        except:
            print('Open Error! Try again!')
            continue
        else:
            r_image = yolo.detect_image(image)
            r_image.show()
    yolo.close_session()
'''
import glob
def detect_img(yolo):
    path = "D:\VOCdevkit\VOC2007\JPEGImages\*.jpg"
    outdir = "D:\\VOCdevkit\VOC2007\SegmentationClass"
    for jpgfile in glob.glob(path):
        img = Image.open(jpgfile)
        img = yolo.detect_image(img)
        img.save(os.path.join(outdir, os.path.basename(jpgfile)))
    yolo.close_session()