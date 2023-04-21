import cv2
import numpy as np

if __name__ == '__main__':
   def callback(*arg):
       print (arg)

cv2.namedWindow( "result" )

cap = cv2.VideoCapture(0)
hsv_min = np.array((0,40,100), np.uint8)
hsv_max = np.array((20,255,255), np.uint8)

while True:
    flag, img = cap.read()
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV )
    thresh = cv2.inRange(hsv, hsv_min, hsv_max)
    cv2.imshow('Video', img)
    cv2.imshow('result', thresh)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()