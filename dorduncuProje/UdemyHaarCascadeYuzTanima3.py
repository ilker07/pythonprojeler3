

import cv2

taniyici=cv2.face.LBPHFaceRecognizer_create()

taniyici.read('training/trainer.yml')
cascadePath="face.xml"
faceCascade=cv2.CascadeClassifier(cascadePath)
yol="yuzverileri"

kamera=cv2.VideoCapture(0)


while True:
    donus,cerceve=kamera.read()
    griton=cv2.cvtColor(cerceve,cv2.COLOR_BGR2GRAY)
    yuzler=faceCascade.detectMultiScale(griton,scaleFactor=1.2,minNeighbors=5)
    for(x,y,w,h) in yuzler:

        tahminEdilenKisi,conf=taniyici.predict(griton[y:y+h,x:x+w])
        cv2.rectangle(cerceve,(x-10,y-10),(x+w+10,y+10+h),(255,0,0),2)
        if(tahminEdilenKisi==1):
            tahminEdilenKisi="Ilker Aykut"

        elif(tahminEdilenKisi==2):
            tahminEdilenKisi="Baska biri"

        else:
            tahminEdilenKisi="Daha başka biri"


        fontFace=cv2.FONT_HERSHEY_SIMPLEX
        fontScale=1
        fontColor=(255,255,255)
        cv2.putText(cerceve,str(tahminEdilenKisi),(x,y+h),fontFace,fontScale,fontColor)
        cv2.imshow("Resim",cerceve)
        cv2.waitKey(10)
