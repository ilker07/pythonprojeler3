

##### WEB DEN RESİM ALMA  ####################

'''
import  cv2
from skimage import io

adres='https://www.google.com.tr/search?q=google&tbm=isch&source=lnms&sa=X&ved=0ahUKEwisxO-skoveAhVOpIsKHfAqD0MQ_AUIDCgD&biw=1366&bih=626&dpr=1#imgrc=w8l2lLAfM_w3vM:'

resim=io.imread(adres)
cv2.imshow("Ters olarak",resim)
cv2.imshow("Doğru olarak",cv2.cvtColor(resim,cv2.COLOR_BGR2RGB))
cv2.waitKey(0)
'''
##### WEB DEN RESİM ALMA  ####################



##### WEB DEN VİDEO ALMA  ####################

import pafy
import cv2

url='https://www.youtube.com/watch?v=Pv8u1-BT8lk'
paffy=pafy.new(url)
play=paffy.getbest(preftype="webm")

kamera=cv2.VideoCapture(play.url)

while True:
    donus,video=kamera.read()
    griton=cv2.cvtColor(video,cv2.COLOR_BGR2GRAY)
    cv2.imshow('video',video)
    cv2.imshow('gri', griton)

    if(cv2.waitKey(25) & 0xFF==ord('q')):
        break

kamera.release()
cv2.destroyAllWindows()





##### WEB DEN RESİM ALMA  ####################