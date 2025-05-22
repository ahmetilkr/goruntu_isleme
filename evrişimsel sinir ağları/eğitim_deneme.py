from ultralytics import YOLO
from PIL import Image
model=YOLO('yolov8n.pt')
im1=Image.open("elon.jpg")
sonuc=model.predict(source=im1,save=True)
#sonuc=model.predict(source=0,show=True)
#sonuc=model.predict(source='adam.mp4',show=True) #nesne algılaması yaparak sonuçları döndürür
import os
import shutil



