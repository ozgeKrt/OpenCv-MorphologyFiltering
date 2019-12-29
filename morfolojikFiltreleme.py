import cv2
import numpy as np
#kendi kameramız için 0, usb takılı kamera 1, video varsa "video.mp4"
kamera = cv2.VideoCapture(0)  

dusuk = np.array([88,50,50])
yuksek = np.array([130,255,255])

while True:
    ret, kare = kamera.read()

    hsv = cv2.cvtColor(kare, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv, dusuk, yuksek)

    maskelenenAlan = cv2.bitwise_and(kare, kare, mask = mask)

    kernel = np.ones((5,5),np.uint8)

    erosion = cv2.erode(mask, kernel, iterations = 1)

    diolation = cv2.dilate(mask, kernel, iterations = 1)

    opening = cv2.morphologyEx(mask,cv2.MORPH_OPEN, kernel)

    closing = cv2.morphologyEx(mask,cv2.MORPH_CLOSE, kernel)
    

    cv2.imshow("normal görüntü", kare)

    cv2.imshow("mask", mask)

    cv2.imshow("maskelenen alan", maskelenenAlan)
    
    cv2.imshow("erosion", erosion)

    cv2.imshow("diolation", diolation)
    
    cv2.imshow("opening", opening)

    cv2.imshow("closing", closing)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
kare.release()
cv2.destroyAllWindows()