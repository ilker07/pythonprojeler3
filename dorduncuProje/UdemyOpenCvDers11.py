

####YAZIYI NETLEŞTİRME


import  cv2

resim=cv2.imread('sayfa.jpg')
gri_resim=cv2.cvtColor(resim,cv2.COLOR_BGR2GRAY)


gauss=cv2.adaptiveThreshold(gri_resim,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)


cv2.imshow('Gauss',gauss)

cv2.waitKey(0)
cv2.destroyAllWindows()