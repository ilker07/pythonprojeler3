
#########VİDEODA FİLTRELEME############


import cv2
import numpy as np


kamera=cv2.VideoCapture(0)



while(1):

    donus,cerceve=kamera.read()
    hsv=cv2.cvtColor(cerceve,cv2.COLOR_BGR2HSV) #renk filtrelemesi.
    alt_ton_kirmizi=np.array([150,30,30])#mavi:100,60,60   ve  beyaz:0,0,140  sarı:5,100,100
    ust_ton_kirmizi=np.array([190,255,255])##mavi:140,255,255  beyaz:256,60,256  sarı:40,255,255
    maskeleme=cv2.inRange(hsv,alt_ton_kirmizi,ust_ton_kirmizi)##Belirlenen renk görünmüyor ama şekli net belli.
    son_video=cv2.bitwise_and(cerceve,cerceve,mask=maskeleme)##Belirlenen renk görünür.

   #####BULANIKLAŞTIRMA

    cekirdek=np.ones((15,15),np.float32)/225 #15 piksele 15 piksellik alan,15*15=225
    duzlestirilmis=cv2.filter2D(son_video,-1,cekirdek) #-1 derinlik.
    bulaniklik=cv2.GaussianBlur(son_video,(15,15),0)
    medyan=cv2.medianBlur(son_video,15)
    iki_tarafli=cv2.bilateralFilter(son_video,15,75,75)


    #####BULANIKLAŞTIRMA


    ####EROSİON VE DİLATİON####################

    kernel=np.ones((5,5),np.uint8)
    erosion=cv2.erode(maskeleme,kernel,iterations=1)##gürültüyü siler
    dilation=cv2.dilate(maskeleme,kernel,iterations=1)#gürültüyü artırır.

    ####EROSİON VE DİLATİON####################


   ##OPENİNG VE CLOSİNG######
    opening=cv2.morphologyEx(maskeleme,cv2.MORPH_OPEN,kernel)
    closing=cv2.morphologyEx(maskeleme,cv2.MORPH_CLOSE,kernel)

    ##OPENİNG VE CLOSİNG######

    ###SOBEL###########

    laplacian=cv2.Laplacian(cerceve,cv2.CV_64F)
    sobelX = cv2.Sobel(cerceve, cv2.CV_64F,1,0,ksize=5)##Ksize ne kadar aralıklarla yapacağını belirler.
    sobelY = cv2.Sobel(cerceve, cv2.CV_64F,0,1,ksize=5)

    #####SOBEL##############
    ###CANNY KENAR TESPİTİ###########

    kenarlar=cv2.Canny(cerceve,100,200)


    ###CANNY KENAR TESPİTİ###########


    cv2.imshow("Orjinal Video",cerceve)
    ''''
    cv2.imshow("Maske Video",maskeleme)
    cv2.imshow("Son Video",son_video)
    cv2.imshow("Duzlestirilmis", duzlestirilmis)
    cv2.imshow("Bulaniklik", bulaniklik)
    cv2.imshow("Medyan", medyan)
    cv2.imshow("iki_tarafli", iki_tarafli)
    '''
    #cv2.imshow("Laplacian",laplacian)
    #cv2.imshow("Sobelx",sobelX)
    #cv2.imshow("SobelY",sobelY)
    cv2.imshow("Kenarlar",kenarlar)
    if(cv2.waitKey(25) & 0xFF==ord("q")):
        break


kamera.release()
cv2.destroyAllWindows()





