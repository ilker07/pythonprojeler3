##RESİMDEKİ İSTENEN NESNEYİ BULMA########################
'''
import  cv2
import numpy as np

resim=cv2.imread('ana-resim.jpg')
gri_resim=cv2.cvtColor(resim,cv2.COLOR_BGR2GRAY)

bulunacak_nesne=cv2.imread('template.jpg',0)

genislik,yukseklik=bulunacak_nesne.shape[::-1]  ##19 ve 22  print(bulunacak_nesne.shape) Böyle de yazılabilir.


kaynak=cv2.matchTemplate(gri_resim,bulunacak_nesne,cv2.TM_CCOEFF_NORMED)

esik_deger=0.8

lokasyon=np.where(kaynak>esik_deger)


for nokta in zip(*lokasyon[::-1]):

    cv2.rectangle(resim,nokta,(nokta[0]+genislik,nokta[1]+yukseklik),(0,255,0),2)


cv2.imshow('Nesneler',resim)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
##RESİMDEKİ İSTENEN NESNEYİ BULMA########################


####istenen resmi ön plana çıkarma#####

import cv2
import numpy as np
from  matplotlib import pyplot as pl

resim=cv2.imread('messi.jpg')
maske=np.zeros(resim.shape[:2],np.uint8)

arka_plan=np.zeros((1,65),np.float64)
on_plan=np.zeros((1,65),np.float64)

dikdortgen=(100,25,200,300)##koordinatlar.x,y  diğer 2 parametre o noktadan ne kadar gidileceği
cv2.grabCut(resim,maske,dikdortgen,arka_plan,on_plan,5,cv2.GC_INIT_WITH_RECT)

maske2=np.where((maske==2)|(maske==0),0,1).astype('uint8')

resim=resim*maske2[:,:,np.newaxis]

pl.imshow(resim)
pl.colorbar()
pl.show()

####istenen resmi ön plana çıkarma#####