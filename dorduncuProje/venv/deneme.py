

import  cv2


kamera=cv2.VideoCapture(0)


while True:

    ret,kare=kamera.read()

    cv2.imshow("Video",kare)

    if cv2.waitKey(25) & 0xFF ==ord('q'):
        break



kamera.release()
cv2.destroyAllWindows()