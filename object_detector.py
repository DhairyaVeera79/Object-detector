from __future__ import print_function
import numpy as np
import cv2

image = cv2.imread("path of image",1)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (11, 11), 0)
edged = cv2.Canny(blurred, 30, 250)

(cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

print("No of switches: {}".format(len(cnts)))
coins = image.copy()
cv2.drawContours(coins, cnts, -1, (0, 255, 0), 2)
cv2.waitKey(0)
a=0
for c in cnts:
    a+=1
    M = cv2.moments(c)
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])
    print("coordinates of switch "+str(a)+": "+str(cX)+", "+str(cY))
    cv2.circle(image, (cX, cY), 7, (0,0,255), -1)
    cv2.putText(image, str(a), (cX - 20, cY - 20),
    cv2.exiFONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

cv2.imshow("Image", image)
cv2.waitkey(0)
