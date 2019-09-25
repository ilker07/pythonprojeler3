
###      RESİMDEKİ YÜZLERİ BULMA  ############
'''
import cv2


resim=cv2.imread('kalabalik.jpg')  #Resmi aldık.

cascadli_yuz=cv2.CascadeClassifier('haarcascade-frontalface-default.xml')#Cascaar algoritmasını aldık.

gri_resim=cv2.cvtColor(resim,cv2.COLOR_BGR2GRAY) #resmi griye çevirdik.


yuzler=cascadli_yuz.detectMultiScale(gri_resim,1.1,4) #Gri resimdeki yüzleri Cascaar algoritmasına göre alıp yuzler ifadesine attık.


for (x_koordinati,y_koordinati,genislik,yukseklik) in yuzler: #Yuzlerde aldığımız yuzleri çizdik.(Yuzler dikdortgen içinde)
    cv2.rectangle(resim,(x_koordinati,y_koordinati),(x_koordinati+genislik,y_koordinati+yukseklik),(0,255,0),3) #Resme dikdörtgenler.



cv2.imshow("Dikdortgenli Yuzler",resim)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''
###      RESİMDEKİ YÜZLERİ BULMA  ############







##########################   KAMERADAN YÜZ BULMA     #####################################

''''

import  cv2

kamera=cv2.VideoCapture(0)
cascadli_yuz=cv2.CascadeClassifier('haarcascade-frontalface-default.xml')#Cascaar algoritmasını aldık.


while(kamera.isOpened()):

    donus,cerceve=kamera.read()

    gri_resim=cv2.cvtColor(cerceve,cv2.COLOR_BGR2GRAY)
    yuzler=cascadli_yuz.detectMultiScale(cerceve,1.6,4)

    for(x,y,gen,yuk) in yuzler:

        cv2.rectangle(cerceve,(x,y),(x+gen,y+yuk),(255,0,0),4)


    cv2.imshow("Yuzler",cerceve)

    if cv2.waitKey(25)  & 0xFF==ord('q') :
        break




kamera.release()
cv2.destroyAllWindows()

'''

##########################   KAMERADAN YÜZ BULMA     #####################################



#######                   KAMERA DAN YÜZ VE GÖZ TESPİTİ     #################################33

import cv2
cascadli_yuz=cv2.CascadeClassifier('haarcascade-frontalface-default.xml')#Cascaar algoritmasını aldık.
cascadli_goz=cv2.CascadeClassifier('haarcascade-eye.xml')#Cascaar algoritmasını aldık.

kamera=cv2.VideoCapture(0)


while True:

    donus,cerceve=kamera.read()
    gri_resim=cv2.cvtColor(cerceve,cv2.COLOR_BGR2GRAY)
    yuzler=cascadli_yuz.detectMultiScale(gri_resim,1.6,4)
    for x,y,gen,yuk in yuzler:
        cv2.rectangle(cerceve,(x,y),(x+gen,y+yuk),(0,0,255),4)
        roi_griresim=gri_resim[y:y+yuk,x:x+gen]
        roi_renkli=cerceve[y:y+yuk,x:x+gen]
        gozler=cascadli_goz.detectMultiScale(roi_griresim)
        for(ex,ey,egen,eyuk) in gozler:
            cv2.rectangle(roi_renkli,(ex,ey),(ex+egen,ey+eyuk),(0,0,255),4)
    cv2.imshow("Goruntu",cerceve)
    if(cv2.waitKey(13) & 0xFF==ord('q')):
        break

kamera.release()
cv2.destroyAllWindows()


#######                   KAMERA DAN YÜZ VE GÖZ TESPİTİ     #################################33

####Tüm vucut tesitine bak!!!!!!!!!!!!!!!!!!!!!!!!!!!!1
#### Videodan araç tespiti !!!!!!!!!!!!!!!!