

#####DERS 39 A TEKRAR BAKKKKKK




####RESİM EŞLEŞTİRME######

import  cv2
import matplotlib.pyplot as pyl

resim_aranacak=cv2.imread('kucuk-resim.JPG',0)
resim_buyuk=cv2.imread('buyuk-resim.JPG',0)

orb=cv2.ORB_create()

anahtar1,hedef1=orb.detectAndCompute(resim_aranacak,None)
anahtar2,hedef2=orb.detectAndCompute(resim_buyuk,None)


bf=cv2.BFMatcher(cv2.NORM_HAMMING,crossCheck=True)

eslesmeler=bf.match(hedef1,hedef2)

eslesmeler=sorted(eslesmeler,key=lambda x:x.distance)

son_resim=cv2.drawMatches(resim_aranacak,anahtar1,resim_buyuk,anahtar2,eslesmeler[:10],None,flags=2)

pyl.imshow(son_resim)
pyl.show()


