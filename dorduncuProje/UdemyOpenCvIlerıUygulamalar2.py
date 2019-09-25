

import  cv2

arka_plan=cv2.createBackgroundSubtractorMOG2()

kamera=cv2.VideoCapture('video.avi')
arac_sayisi=0

minArea=2600
while True:

    donus,cerceve=kamera.read()
    maske=arka_plan.apply(cerceve,None,0.02)
    erode=cv2.erode(maske,None,iterations=4)
    moments=cv2.moments(erode,True)
    cv2.line(cerceve,(40,0),(40,176),(255,0,0),2)
    cv2.line(cerceve,(55,0),(55,176),(255,0,0),2)
    cv2.line(cerceve,(0,50),(320,50),(255,0,0),2)
    cv2.line(cerceve,(0,65),(320,65),(255,0,0),2)

    cv2.line(cerceve,(100,0),(100,176),(0,255,255),2)
    cv2.line(cerceve,(115,0),(115,176),(0,255,255),2)

    cv2.line(cerceve,(0,105),(320,105),(0,255,255),2)
    cv2.line(cerceve,(0,130),(320,130),(0,255,255),2)

    if moments['m00']>minArea:
        x=int(moments['m10']/moments['m00'])
        y=int(moments['m01'] / moments['m00'])

        if(x>40 and x<55 and y>50 and y<65):
            arac_sayisi +=1
            print("Üstten geçti"+str(arac_sayisi))
        elif (x>102 and x<110 and y>105 and y<130):
            arac_sayisi+=1
            print("Alttan geçti"+str(arac_sayisi))
    cv2.putText(cerceve,'Sayi:%r'%arac_sayisi,(200,30),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)


    cv2.imshow('Video',cerceve)
    cv2.imshow('Maske',maske)
    key=cv2.waitKey(25)
    if key==ord('q'):
        break



kamera.release()
cv2.destroyAllWindows()


