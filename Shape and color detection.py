import cv2
import numpy as np

img1 = cv2.imread('ImagePath')
kernel = np.ones((5 , 5) , np.uint8)
img = cv2.erode(img1,kernel,iterations = 1)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

                                                                    #for red

lower_red = np.array([0,100, 100])
upper_red = np.array([10, 255, 255])
maskr = cv2.inRange(hsv, lower_red, upper_red)


imR, contoursR, hierarchyR = cv2.findContours(maskr,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img,contoursR,-1, (0,255,0), 4)


for cnt in contoursR:

    approxr = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
    area = cv2.contourArea(cnt)
    #print area
    if len(approxr)==6 or len(approxr) == 3 or len(approxr) == 5:
        if area>=6401:
            print "red triangle large"
        elif area<=1972 :
            print "red triangle small"
        elif area > 1972 and area < 6400 :
            print"red triangle medium"
        cv2.drawContours(img,[cnt],0,(0,255,0),1)

    elif len(approxr) == 4:
        (x, y, w, h) = cv2.boundingRect(approxr)
        ar = w / float(h)
        if ar >= 0.95 and ar <= 1.05 :
            if area >= 11449:
                print "red square large"
            elif  area <= 3249:
                print "red square small"
            elif area < 11449 and area >3249:
                print"red square medium"
        else:
            if area >= 22149:
                print "red rectangle large"
            elif  area <= 4389:
                print "red rectangle small"
            elif area < 22149 and area > 4389:
                print"red rectangle medium"

        cv2.drawContours(img,[cnt],0,(0,0,255),1)
    elif len(approxr) > 8:
        if area >= 9171:
            print "red circle large"
        elif  area < 2643:
            print "red circle small"
        elif area < 9171 and  area > 2643:
            print"red circle medium"
        cv2.drawContours(img,[cnt],0,(0,255,255),1)


                                        # for blue


lower_blue = np.array([110, 100, 100])
upper_blue = np.array([130, 255, 255])
maskb = cv2.inRange(hsv, lower_blue, upper_blue)



imR, contoursR, hierarchyR = cv2.findContours(maskb,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img,contoursR,-1, (0,255,0), 4)


for cnt in contoursR:

    approxr = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
    area = cv2.contourArea(cnt)
    #print area
    if len(approxr)==6 or len(approxr) == 3 or len(approxr) == 5:
        if area>=6401:
            print "blue triangle large"
        elif area<=1972 :
            print "blue triangle small"
        elif area > 1972 and area < 6400 :
            print"blue triangle medium"
        cv2.drawContours(img,[cnt],0,(0,255,0),1)

    elif len(approxr) == 4:
        (x, y, w, h) = cv2.boundingRect(approxr)
        ar = w / float(h)
        if ar >= 0.95 and ar <= 1.05 :
            if area >= 11449:
                print "blue square large"
            elif  area <= 3249:
                print "blue square small"
            elif area < 11449 and area >3249:
                print"blue square medium"
        else:
            if area >= 22149:
                print "blue rectangle large"
            elif  area <= 4389:
                print "blue rectangle small"
            elif area < 22149 and area > 4389:
                print"blue rectangle medium"

        cv2.drawContours(img,[cnt],0,(0,0,255),1)
    elif len(approxr) > 8:
        if area >= 9171:
            print "blue circle large"
        elif  area < 2643:
            print "blue circle small"
        elif area < 9171 and  area > 2643:
            print"blue circle medium"
        cv2.drawContours(img,[cnt],0,(0,255,255),1)

                        # for green

lower_green = np.array([50, 50, 50])
upper_green = np.array([70, 255, 255])
maskg = cv2.inRange(hsv, lower_green, upper_green)


imR, contoursR, hierarchyR = cv2.findContours(maskg,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img,contoursR,-1, (0,255,0), 4)


for cnt in contoursR:

    approxr = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
    area = cv2.contourArea(cnt)
    #print area
    if len(approxr)==6 or len(approxr) == 3 or len(approxr) == 5:
        if area>=6401:
            print "green triangle large"
        elif area<=1972 :
            print "green triangle small"
        elif area > 1972 and area < 6400 :
            print"green triangle medium"
        cv2.drawContours(img,[cnt],0,(0,255,0),1)

    elif len(approxr) == 4:
        (x, y, w, h) = cv2.boundingRect(approxr)
        ar = w / float(h)
        if ar >= 0.95 and ar <= 1.05 :
            if area >= 11449:
                print "green square large"
            elif  area <= 3249:
                print "green square small"
            elif area < 11449 and area >3249:
                print"green square medium"
        else:
            if area >= 22149:
                print "green rectangle large"
            elif  area <= 4389:
                print "green rectangle small"
            elif area < 22149 and area > 4389:
                print"green rectangle medium"

        cv2.drawContours(img,[cnt],0,(0,0,255),1)
    elif len(approxr) > 8:
        if area >= 9171:
            print "green circle large"
        elif  area < 2643:
            print "green circle small"
        elif area < 9171 and  area > 2643:
            print"green circle medium"
        cv2.drawContours(img,[cnt],0,(0,255,255),1)

        # for orange

lower_orange = np.array([12, 100, 100])
upper_orange = np.array([20, 255, 255])
masko = cv2.inRange(hsv, lower_orange, upper_orange)


imR, contoursR, hierarchyR = cv2.findContours(masko,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img,contoursR,-1, (0,255,0), 4)


for cnt in contoursR:

    approxr = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
    area = cv2.contourArea(cnt)
    #print area
    if len(approxr)==6 or len(approxr) == 3 or len(approxr) == 5:
        if area>=6401:
            print "orange triangle large"
        elif area<=1972 :
            print "orange triangle small"
        elif area > 1972 and area < 6400 :
            print"orange triangle medium"
        cv2.drawContours(img,[cnt],0,(0,255,0),1)

    elif len(approxr) == 4:
        (x, y, w, h) = cv2.boundingRect(approxr)
        ar = w / float(h)
        if ar >= 0.95 and ar <= 1.05 :
            if area >= 11449:
                print "orange square large"
            elif  area <= 3249:
                print "orange square small"
            elif area < 11449 and area >3249:
                print"orange square medium"
        else:
            if area >= 22149:
                print "orange rectangle large"
            elif  area <= 4389:
                print "orange rectangle small"
            elif area < 22149 and area > 4389:
                print"orange rectangle medium"

        cv2.drawContours(img,[cnt],0,(0,0,255),1)
    elif len(approxr) > 8:
        if area >= 9171:
            print "orange circle large"
        elif  area < 2643:
            print "orange circle small"
        elif area < 9171 and  area > 2643:
            print"orange circle medium"
        cv2.drawContours(img,[cnt],0,(0,255,255),1)

                        #for yellow

lower_yellow = np.array([ 21, 100, 100])
upper_yellow = np.array([ 40, 255, 255])
masky = cv2.inRange(hsv, lower_yellow, upper_yellow)



imR, contoursR, hierarchyR = cv2.findContours(masky,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img,contoursR,-1, (0,255,0), 4)


for cnt in contoursR:

    approxr = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
    area = cv2.contourArea(cnt)
    #print area
    if len(approxr)==6 or len(approxr) == 3 or len(approxr) == 5:
        if area>=6401:
            print "yellow triangle large"
        elif area<=1972 :
            print "yellow triangle small"
        elif area > 1972 and area < 6400 :
            print"yellow triangle medium"
        cv2.drawContours(img,[cnt],0,(0,255,0),1)

    elif len(approxr) == 4:
        (x, y, w, h) = cv2.boundingRect(approxr)
        ar = w / float(h)
        if ar >= 0.95 and ar <= 1.05 :
            if area >= 11449:
                print "yellow square large"
            elif  area <= 3249:
                print "yellow square small"
            elif area < 11449 and area >3249:
                print"yellow square medium"
        else:
            if area >= 22149:
                print "yellow rectangle large"
            elif  area <= 4389:
                print "yellow rectangle small"
            elif area < 22149 and area > 4389:
                print"yellow rectangle medium"

        cv2.drawContours(img,[cnt],0,(0,0,255),1)
    elif len(approxr) > 8:
        if area >= 9171:
            print "yellow circle large"
        elif  area < 2643:
            print "yellow circle small"
        elif area < 9171 and  area > 2643:
            print"yellow circle medium"
        cv2.drawContours(img,[cnt],0,(0,255,255),1)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""
blue circle large
9171.0
red  triangle large
6400.5
green rectangle large
22149.0
orange rectangle large
11449.0
yellow square large
11449.0
blue square smalll
3249.0
yellow rectangle small
4389.0
green triangle small
1972.0
red circle small
2643.5
"""
