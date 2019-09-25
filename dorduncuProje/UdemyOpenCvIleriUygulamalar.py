

#### HAREKET ALGILAMA

'''
import cv2
from datetime import datetime


def farkImaj(r0,r1,r2):

    fark1=cv2.absdiff(r2,r1)
    fark2=cv2.absdiff(r1,r0)
    return  cv2.bitwise_and(fark1,fark2)


esik_deger=140000
kamera=cv2.VideoCapture(0)

pencereIsmi="Hareket Algılayıcı"
cv2.namedWindow(pencereIsmi)


t_eksi=cv2.cvtColor(kamera.read()[1],cv2.COLOR_BGR2GRAY)
t=cv2.cvtColor(kamera.read()[1],cv2.COLOR_BGR2GRAY)
t_arti=cv2.cvtColor(kamera.read()[1],cv2.COLOR_BGR2GRAY)


zamanKontrol=datetime.now().strftime('%Ss') #Saniye Ss

while True:
    cv2.imshow(pencereIsmi,kamera.read()[1])
    if(cv2.countNonZero(farkImaj(t_eksi,t,t_arti)) >esik_deger and  zamanKontrol!=datetime.now().strftime('%Ss')):
        farkResim=kamera.read()[1]
        cv2.imwrite(datetime.now().strftime('%Y%m%d_%Hh&Mm%Ss%f')+'.jpg',farkResim)
    zamanKontrol = datetime.now().strftime('%Ss')  # Saniye Ss
    t_eksi=t
    t=t_arti
    t_arti=cv2.cvtColor(kamera.read()[1],cv2.COLOR_BGR2GRAY)
    key=cv2.waitKey(10)
    if key==27:
        cv2.destroyWindow(pencereIsmi)
        break

'''
#### HAREKET ALGILAMA

#### HAREKET ARKAPLAN FİLTRELEME

import  cv2
kamera=cv2.VideoCapture('video1.avi')
arka_plan_cikartma=cv2.createBackgroundSubtractorMOG2()

while True:
    donus,cerceve=kamera.read()
    maskeleme=arka_plan_cikartma.apply(cerceve)
    cv2.imshow('Maskeleme',maskeleme)
    cv2.imshow('Orijinal',cerceve)
    k=cv2.waitKey(25) & 0xFF
    if k==27:
        break

kamera.release()
cv2.destroyAllWindows()

#### HAREKET ARKAPLAN FİLTRELEME