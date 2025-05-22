import math
import cv2
import os
import numpy
import time
from ultralytics import YOLO
import cv2


#model_path = r"C:\Users\ASUS\runs\detect\train2\weights\last.pt"
#model_path = r"C:\Users\ASUS\runs\detect\train5\weights\last.pt"
#model_path = r"models\last_50_epoch.pt"
model_path = r"C:\Users\ahmet\PycharmProjects\pythonProject\yolo\runs\detect\train2\weights\best.pt"
#model_path = r"C:\Users\ahmet\PycharmProjects\pythonProject\yolo\runs\detect\mobilnetv3-v11n\weights\best.pt"
#model_path = r"C:\Users\ahmet\PycharmProjects\pythonProject\yolo\runs\detect\mobilenetv3-v8n\weights\best.pt"
#model_path = r"C:\Users\ahmet\PycharmProjects\pythonProject\yolo\runs\detect\mobilenetv3-v5n\weights\best.pt"

prev_frame_time = 0
new_frame_time = 0
#cap = cv2.VideoCapture(r"C:\Users\ahmet\PycharmProjects\pythonProject\yolo\videolar\Kayıt 2024-09-20 203535.mp4")
#cap = cv2.VideoCapture(r"C:\Users\ahmet\PycharmProjects\pythonProject\yolo\videolar\iki_ucak.mp4")
#cap = cv2.VideoCapture(r"C:\Users\ahmet\PycharmProjects\pythonProject\yolo\videolar\tek_ucak.mp4")
cap = cv2.VideoCapture(r"C:\Users\ahmet\PycharmProjects\pythonProject\yolo\videolar\VID-20241005-WA0004~3.mp4")
#cap = cv2.VideoCapture(r"C:\Users\ahmet\PycharmProjects\pythonProject\yolo\videolar\VID-20241005-WA0009.mp4")
#cap = cv2.VideoCapture(r"C:\Users\ahmet\PycharmProjects\pythonProject\yolo\videolar\VID-20241005-WA0010.mp4")
#cap = cv2.VideoCapture(r"C:\Users\ahmet\PycharmProjects\pythonProject\yolo\videolar\VID-20241005-WA0011.mp4")

model = YOLO(model_path)

while True:
    succesess ,img = cap.read()


    img = cv2.resize(img,(1080,720))

    if succesess == True: # eğer veri gelmiyorsa dögüyü kır

      #istenilen formatta hedef vuruş alanı (sağdan soldan %25 , yukarıdan ve aşağıdan %10 olacak fark olacak şekilde)
      height, width, _ = img.shape
      rect_width = int(width * 0.50)  # Yatayda %50
      rect_height = int(height * 0.80)  # Dikeyde %80
      top_left = (int((width - rect_width) / 2), int((height - rect_height) / 2))  # Ortalamak için
      bottom_right = (top_left[0] + rect_width, top_left[1] + rect_height)
      cv2.rectangle(img, top_left, bottom_right, (0, 255, 255), 2)

      #ZERO DİVİSON ERROR
      #new_frame_time = time.time()
      #fps = 1 / (new_frame_time - prev_frame_time)
      #prev_frame_time = new_frame_time
      #cv2.putText(img, f"FPS ={int(fps)}", (30, 30), cv2.FONT_HERSHEY_COMPLEX, 0.7, (255, 0, 0), thickness=2)       #nesne tespit kısmı
      results = model.predict(img, stream=True)
      for r in results:
          boxes = r.boxes
          for box in boxes:

               x1, y1, x2, y2 = box.xyxy[0]
               x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
               w, h = x2 - x1, y2 - y1

               # tespit edilen nesne etrafında kare çizimi
               cv2.rectangle(img,(x1, y1),(x1+w, y1+h),(0,0,255),2)

               # tespit edilen nesnenin kordinatları ve güvenirlik sonucu
               conf = math.ceil((box.conf[0]*100)) / 100

               bbox =[x1,y1,w,h]

               #güvenirlirk sonucu ekrana yazımı
               cv2.putText(img, f"fixed wing UAV= {conf}", (x1, y1-5), cv2.FONT_HERSHEY_COMPLEX, 0.6, (0,0,255),thickness=1)


               cx, cy = x1+w//2, y1+h//2
               cv2.circle(img,(cx,cy),5,(0,0,0),cv2.FILLED)

               #ekranın tam ortasının kordinatalrı
               height, width, _ = img.shape
               center_x = width // 2
               center_y = height // 2
               cv2.circle(img,(center_x,center_y),5,(0, 0, 0),cv2.FILLED)

               #nesne ile ekranın ortası arasında çizgi
               cv2.line(img,(cx,cy),(center_x,center_y),(0,0,0),2)

      cv2.imshow("Image", img)
    else: break
    if cv2.waitKey(1) & 0xFF == ord("q"): break




