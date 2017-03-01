#a test script for a aniface cascade classification,using a classifier
#from nagadomi

import cv2
import os.path

def aniface(img, classifier):
    if not os.path.isfile(classifier):
        raise RuntimeError("%s: not found!" % classifier)

    cascade = cv2.CascadeClassifier(classifier)
    if cascade.empty() is  True:
        raise RuntimeError("Cascade Classifier load failed\n")
    else:
        print "Cascade Classifier load successfully\n"

    image = cv2.imread(img)
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image_gray = cv2.equalizeHist(image_gray)
    param = [1.01, 1, (100, 100)]
    #scaleFactor:spend more time ,more sensitive,but high risk of
    #false positive result if this param is small
    #minNeighbors:high reduplicative result if this param is too small
    #minSize:min size of face in your image
    faces = cascade.detectMultiScale(image_gray,
                                     scaleFactor = param[0],
                                     minNeighbors = param[1],
                                     minSize = param[2])

    if len(faces) > 0:
        print "find :", len(faces), "faces\n"
        print "scaleFactor:", param[0], "minNeighbors:",param[1],"minSize:",param[2]
        print "\n"
        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x,y), (x+w, y+h), (0,0,255),2)

        cv2.imshow('detected result', image)
        cv2.waitKey(0)
    else:
        print "can not find ani face in %s" %img


if __name__ == '__main__':

    imagepath =  'E:/python/aniface/ll.jpg'
    classifier = 'E:/python/aniface/lbpcascade_animeface.xml'
    aniface(imagepath, classifier)
