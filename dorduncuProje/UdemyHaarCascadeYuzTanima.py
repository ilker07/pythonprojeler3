

import cv2
kamera=cv2.VideoCapture(0)

detector=cv2.CascadeClassifier('face.xml')

i=0

offset=50

kisiId=input("ID Bilgisi girin:")
while True:
    donus,cerceve=kamera.read()
    griton=cv2.cvtColor(cerceve,cv2.COLOR_BGR2GRAY)
    yuzler=detector.detectMultiScale(griton,scaleFactor=1.3,minNeighbors=5,minSize=(100,100),flags=cv2.CASCADE_SCALE_IMAGE)

    for (x,y,gen,yuk) in yuzler:
        i+=1
        cv2.imwrite("yuzverileri/face-"+kisiId+"."+str(i)+".jpg",griton[y-offset:y+yuk+offset,x-offset:x+offset+gen])
        cv2.rectangle(cerceve,(x-offset,y-offset),(x+offset+gen,y+offset+yuk),(255,0,0),2)
        cv2.waitKey(100)

    if i>20:
        kamera.release()
        cv2.destroyAllWindows()
        break
