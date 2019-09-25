
#####CANYY İLE KENAR TESPİTİ##############
'''
import  cv2
from matplotlib import pyplot as plt
import numpy as np


resim=cv2.imread('messi.jpg',0)##gri resim

kenarlar=cv2.Canny(resim,300,300)


plt.subplot(121),plt.imshow(resim,cmap='gray')
plt.title('Resim'),plt.xticks([]),plt.yticks([])


plt.subplot(122),plt.imshow(kenarlar,cmap='gray')
plt.title('Kenarlar'),plt.xticks([]),plt.yticks([])

plt.show()
'''
#####CANYY İLE KENAR TESPİTİ##############


import  cv2
import  numpy as np
from  matplotlib import pyplot as plt

resim=cv2.imread('messi.jpg')
ilk,ilk1=cv2.threshold(resim,127,255,cv2.THRESH_BINARY)
ret,thresh1=cv2.threshold(resim,127,255,cv2.THRESH_BINARY_INV)
ret2,thresh2=cv2.threshold(resim,127,255,cv2.THRESH_TRUNC)
ret3,thresh3=cv2.threshold(resim,127,255,cv2.THRESH_TOZERO)
ret4,thresh4=cv2.threshold(resim,127,255,cv2.THRESH_TOZERO_INV)


basliklar=['Orjinal','BINARY','BINARY INV','TRUNC','TOZERO','TOZERO INV']
resimler=[resim,ilk1,thresh1,thresh2,thresh3,thresh4]

for i in range(0,6):
    plt.subplot(2,3,i+1),plt.imshow(resimler[i],'gray')
    plt.title(basliklar[i])
    plt.xticks([]),plt.yticks([])

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()

