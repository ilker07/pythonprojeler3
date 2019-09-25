

import numpy as np



liste=np.array([[1,2,3],[4,5,6]])
##a=np.zeros((3,4))  3 satır 4 sütun 0 oluşsturur.

##b=np.ones((3,4))


#c=np.arange(10,50,5) ##10 dan başlayıp 50 ye kadar (50 dahil değil) 5 er 5 er sayıları yazaar.Liste yapar.
#d=np.linspace(10,50,20) ##10 dan başlayıp 50 ye kadar (50 dahil )20 tane  sayı yazaar.Liste yapar.

tahmin=np.random.random((5,5)) ## 5 e 5 lik 0 ile 1 arasında sayılar üretir.
toplam=tahmin.sum()
maks=tahmin.max()
mini=tahmin.min()

ilk_sutun_toplam=tahmin.sum(axis=0)



array=np.array([1,2,3,4,5])

ters_array=array[::-1]
#print(ters_array)


#print(liste[1,2])##satır,sutun

#print(liste[:,1])##tüm satırlarda 1 .sütun
#print(liste)
#print(liste[1,0:2])##1 satırı al.sütundada 0 dan 2 ye kadar (2 dahil değil)




array2=np.array([[1,2,3],[4,5,6],[7,8,9]])

a=array2.ravel()
print(a)

b=a.reshape((3,3))
print(b)

arrayT=b.T
print(arrayT)

##array_vertical_birlestri=np.vstack((liste1,liste2)) horizontal hstack.
