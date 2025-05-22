from ultralytics import YOLO
from PIL import Image
import torch
if __name__ == '__main__':
    print(torch.cuda.is_available())
    print(torch.cuda.get_device_name(0))
    from ultralytics import YOLO

    # Modeli yükle
    model = YOLO("yolov8n.pt")

    # Eğitim işlemini başlat
    results = model.train(data=r"C:\Users\ahmet\Desktop\arda_acelya_ds\config.yaml", epochs=200,batch=32,imgsz=704,device="cuda",optimizer="AdamW")

