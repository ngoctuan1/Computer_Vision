import cv2
import numpy as np
import argparse as arg

# constructor the argument parse and parse the arguments
ap = arg.ArgumentParser()

ap.add_argument('-i', '--image', required=True,
                help='path to input image')

ap.add_argument('-p', '--prototxt', required=True,
                help='path to Caffe "deploy" prototxt file')

ap.add_argument('-m', '--model', required=True,
                help='path to Caffe pre-trained model')
ap.add_argument('-c', '--confidence', type=float, default=0.5,
                help='minimun probability to filter wead detections')

args = vars(ap.parse_args())


# load our serialized model from disk
print('[INFO] loading model...')
net = cv2.dnn.readNetFromCaffe(args['prototxt'], args['model'])
print(net)
# load the input image and construct an input blob for the image
# by resizing to a fixed 300x300 pixels and then normalizing it
img = cv2.imread(args['image'])

h, w = img.shape[0:2]

blob = cv2.dnn.blobFromImage(cv2.resize(
    img, (300, 300)), 1.0, (300, 300), (104.0, 177.0, 123.0))

# print(blob.shape) #(1, 3, 300, 300)
# pass the bob through the network and obtain the detections and
# predictions
print('[INFO] computing object detections...')
net.setInput(blob)
detections = net.forward()

# loop over the detections
for i in range(0, detections.shape[2]):
    # extract the confidence (i.e., probability) associated
    # with the prediction
    confidence = detections[0, 0, i, 2]

    # filter out weak detections by ensuring the 'confidence'
    # is greater than the minimum confidence
    if confidence > args['confidence']:
        # compute the (x,y)-coordinates of the bounding box
        # box for the object
        box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])

        startX, startY, endX, endY = box.astype('int')

        # draw the bounding box of the face along with the associated
        # probability
        text = '{:.2f}%'.format(confidence * 100)
        y = startY - 10 if startY - 10 > 10 else startY + 10
        cv2.rectangle(img, (startX, startY), (endX, endY), (0, 255, 0), 3)
        cv2.putText(img, text, (startX, y),
                    cv2.FONT_HERSHEY_COMPLEX, 0.45, (0, 0, 255), 2)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
