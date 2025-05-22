#from  preprocessing import convert_voc_to_yolo
#convert_voc_to_yolo()
#cd yolov5
#python train.py --img 320 --batch 16 --epochs 200 --data VOC.yaml --weights yolov5s.pt --workers 2

import torch
from matplotlib import pyplot as plt
import numpy as np
import cv2
import itertools
import os
model=torch.hub.load('ultralytics/yolov5','custom',path=r'C:\Users\ahmet\PycharmProjects\pythonProject\yolov5\runs\train\exp3\weights\best.pt',force_reload=True)

fig,ax=plt.subplots(2,4,figsize=(20,10))
imgs = os.listdir(r'C:\Users\ahmet\PycharmProjects\pythonProject\data\images')

for idx in itertools.product(range(2),range(4)):
    imgname=np.random.choice(imgs)
    img = cv2.imread(f'C:/Users/ahmet/PycharmProjects/pythonProject/data/images/{imgname}')

    results=model(img)
    print(np.squeeze(results.render()).shape)
    ax[idx[0],idx[1]].imshow(cv2.cvtColor(np.squeeze(results.render()),cv2.COLOR_BGR2RGB))


