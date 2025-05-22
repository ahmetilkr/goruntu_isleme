import cv2
import mediapipe as mp
cap=cv2.VideoCapture(0)
mpHands=mp.solutions.hands
hands=mpHands.Hands()
mpDraw=mp.solutions.drawing_utils
tipIds=[4,8,12,16,20]
while True:
    success,img=cap.read()
    img_rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results=hands.process(img_rgb)
    #print(results.multi_hand_landmarks)
    lmList=[]
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(img,handLms,mpHands.HAND_CONNECTIONS)
            for id,lm in enumerate(handLms.landmark):
                h,w,c=img.shape
                cx,cy=int(lm.x*w),int(lm.y*h)
                lmList.append([id,cx,cy])

                if id == 8:
                    cv2.circle(img, (cx, cy), 9, (255, 0, 0), cv2.FILLED)
                if id == 6:
                    cv2.circle(img, (cx, cy), 9, (0, 0, 255), cv2.FILLED)

    if len(lmList)!=0:
      fingers=[]
      #baş parmak
      if lmList[tipIds[0]][1]<lmList[tipIds[0]-1][1]:
          fingers.append(1)
      else:
          fingers.append(0)
      #4 parmak
      for id in range(1,5):
          if lmList[tipIds[id]][2]<lmList[tipIds[id]-2][2]:
              fingers.append(1)
          else:
              fingers.append(0)
      totalF=fingers.count(1)
      print(totalF)
      cv2.putText(img,str(totalF),(30,125),cv2.FONT_HERSHEY_PLAIN,10,(255,0,0),8)
    cv2.imshow("img",img)
    cv2.waitKey(1)