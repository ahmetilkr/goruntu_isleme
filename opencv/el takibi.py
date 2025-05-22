import cv2
import time
import mediapipe as mp
cap=cv2.VideoCapture(0)
mpHand=mp.solutions.hands #solutions meadipipe kütüphanesinin içindeki bir namespace hands ise solutions altındaki bir modül
hands=mpHand.Hands() #hands adında bir nesne oluşturduk
mpDraw=mp.solutions.drawing_utils
while True:
    success,img=cap.read()
    img_rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results=hands.process(img_rgb) #el analizine başladık ve el nesnesini resultsa aktardık

    print(results.multi_hand_landmarks) #elin özelliklerini yazdırdık
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks: #results.multi_hand_landmarks genel olarak ele ait özellikleri tutar
            mpDraw.draw_landmarks(img,handLms,mpHand.HAND_CONNECTIONS) #bir çizme fonksiyonu ilk parametre hangi foto üzerinde olacağo
            #ikinci hangi noktalar üçüncü ise noktaların birbirine çizgi ile bağlanması gerektiğini söyler

            for id,lm in enumerate(handLms.landmark): #handLms.landmark  elin işaret noktalarını ulaşmak için kullanılır
                h,w,c=img.shape
                cx,cy=int(lm.x*w),int(lm.y*h)
                print(lm)

                if id==0:
                    cv2.circle(img,(cx,cy),9,(255,0,0),cv2.FILLED)


    cv2.imshow("img",img)
    cv2.waitKey(1)