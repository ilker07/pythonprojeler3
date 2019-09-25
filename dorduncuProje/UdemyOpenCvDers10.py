
#ADAPTİF FİLTRELEMELER
'''
import cv2
import numpy as np

from  matplotlib import pyplot as plt


resim=cv2.imread('messi.jpg',0)
resim=cv2.medianBlur(resim,5)


ret,th1=cv2.threshold(resim,127,255,cv2.THRESH_BINARY)
th2=cv2.adaptiveThreshold(resim,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
th3=cv2.adaptiveThreshold(resim,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)


basliklar=["Orjinal","Resim1","Resim1","Resim1"]
resimler=[resim,th1,th2,th3]

for i in range(4):
    plt.subplot(2,2,i+1),plt.imshow(resimler[i],'gray')
    plt.title(basliklar[i])
    plt.xticks([]),plt.yticks([])

plt.show()



'''

#ADAPTİF FİLTRELEMELER



#######OTSU THRESHOLDİNG


import cv2
import numpy as np
from matplotlib import  pyplot as plt

resim=cv2.imread('messi.jpg',0)

ret1,th1=cv2.threshold(resim,127,255,cv2.THRESH_BINARY)
ret2,th2=cv2.threshold(resim,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)


blur=cv2.GaussianBlur(resim,(5,5),0)
ret3,th3=cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)


resimler=[resim,0,th1,resim,0,th2,blur,0,th3]

basliklar=['Orjinal Resim','Histagram','Basit thresholding'
           ,'Orjinal Resim','Histogram','Otsu Thresholding'
           ,'Gaussian Blur','Histogram','Otsu Thresholding']

for i in range(3):
    plt.subplot(3,3,i*3+1),plt.imshow(resimler[i*3],'gray')
    plt.title(basliklar[i*3]),plt.xticks([]),plt.yticks([])
    plt.subplot(3,3,i*3+2),plt.hist(resimler[i*3].ravel(),256)
    plt.title(basliklar[i*3+1]),plt.xticks([]),plt.yticks([])
    plt.subplot(3,3,i*3+3),plt.imshow(resimler[i*3+2],'gray')
    plt.title(basliklar[i * 3 + 2]), plt.xticks([]), plt.yticks([])

plt.show()