import cv2
cap=cv2.VideoCapture(0,cv2.CAP_DSHOW) #video veya webcam okuma işlemi 0 yazarsan webcam dosya belirtirsen dosya
while True:
    ret,frame=cap.read()
    frame=cv2.flip(frame,1) #kameranın y ekseninde simetriği
    cv2.imshow("webcam",frame)
    if cv2.waitKey(1) & 0xFF ==ord("s"):
        break


cap.release()   #işlem tamamlanınca kamerayı serbest bırak
cv2.destroyAllWindows()