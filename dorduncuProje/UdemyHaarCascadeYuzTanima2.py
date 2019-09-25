
import cv2
import os
import numpy as np
from PIL import Image



taniyici=cv2.face.LBPHFaceRecognizer_create() #cv2.face_LBPHFaceRecognizer.create()
cascadePath='face.xml'
faceCascade=cv2.CascadeClassifier(cascadePath)
yol='yuzverileri'


def resim_ve_etiketleri_al(yol):
    resim_yollari=[os.path.join(yol,f) for f in os.listdir(yol)]
    resimler=[]
    etiketler=[]
    for resim_yolu in resim_yollari:
        resim_pillow=Image.open(resim_yolu).convert('L')
        resim=np.array(resim_pillow,'uint8')
        nbr=int(os.path.split(resim_yolu)[1].split(".")[0].replace("face-",""))
        print(nbr)
        yuzler=faceCascade.detectMultiScale(resim)
        for(x,y,w,h) in yuzler:
            resimler.append((resim[y:y+h,x:x+w]))
            etiketler.append(nbr)
            cv2.imshow("Resimler eğitme",resim[y:y+h,x:x+w])
            cv2.waitKey(10)

        return  resimler,etiketler



images,labels=resim_ve_etiketleri_al(yol)
cv2.imshow("Test",images[0])
cv2.waitKey(1)
taniyici.train(images,np.array(labels))
taniyici.write('training/trainer.yml')
cv2.destroyAllWindows()