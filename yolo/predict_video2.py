import cv2
import os
import numpy
from ultralytics import YOLO
import time
import torch

model_path = r"C:\Users\ahmet\PycharmProjects\pythonProject\yolo\runs\detect\train2\weights\best.pt"
#cap = cv2.VideoCapture(r"C:\Users\ahmet\PycharmProjects\pythonProject\yolo\videolar\Kayıt 2024-09-20 203535.mp4")
#cap = cv2.VideoCapture(r"C:\Users\ahmet\PycharmProjects\pythonProject\yolo\videolar\iki_ucak.mp4")
#cap = cv2.VideoCapture(r"C:\Users\ahmet\PycharmProjects\pythonProject\yolo\videolar\tek_ucak.mp4")
cap = cv2.VideoCapture(r"C:\Users\ahmet\PycharmProjects\pythonProject\yolo\videolar\VID-20241005-WA0004~3.mp4")
#cap = cv2.VideoCapture(r"C:\Users\ahmet\PycharmProjects\pythonProject\yolo\videolar\VID-20241005-WA0009.mp4")
#cap = cv2.VideoCapture(r"C:\Users\ahmet\PycharmProjects\pythonProject\yolo\videolar\VID-20241005-WA0010.mp4")
#cap = cv2.VideoCapture(r"C:\Users\ahmet\PycharmProjects\pythonProject\yolo\videolar\VID-20241005-WA0011.mp4")

model=YOLO(model_path)
prev_frame_time=0
new_frame_time=0
while True:
    success, frame =cap.read()
    if success == False:
        print("çalışmadı")
        break
    else:
        new_frame_time=time.time()
        frame=cv2.resize(frame,(1080,720))
        height, width, _ =frame.shape
        frame=cv2.rectangle(frame,((width//4),(height//10)),((width*3//4,height*9//10)),(0,255,255),2)
        results=model.predict(frame , stream=True)
        for result in results:
            boxes = result.boxes
            for box in boxes:
              print(box.conf)
              print(box.xyxy)
              print(box.cls)
              x1,y1,x2,y2=box.xyxy[0]
              x1, y1, x2, y2=int(x1),int(y1),int(x2),int(y2)

              accuracy=int(box.conf[0]*100)

              if x2-x1>=width*5/100 or y2-y1>=height*5/10:
                 cv2.rectangle(frame,(x1,y1),(x2,y2),(0,0,255),2)
              else:
                 cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

              cv2.putText(frame,f"fixed wing UAV={accuracy}",(x1,y1-10),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),1)

              cv2.circle(frame,(width//2,height//2),4,(0,0,0),thickness=-1)
              cv2.circle(frame,((x1+x2)//2,(y1+y2)//2),4,(0,0,0),thickness=-1)
              cv2.line(frame, (width // 2, height // 2), ((x1 + x2) // 2, (y1 + y2) // 2), (0, 0, 0), thickness=2)
    fps=1/(new_frame_time-prev_frame_time)
    cv2.putText(frame, f"fps={fps}", ((width // 4 + 5), (height // 10 + 35)), cv2.FONT_HERSHEY_SIMPLEX, 1,(0, 0, 0), 1)
    cv2.imshow("pencere",frame)

    cv2.waitKey(1)

cap.release()
cv2.destroyAllWindows()



