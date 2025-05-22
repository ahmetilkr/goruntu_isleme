

import cv2
from ultralytics import YOLO

# Modeli yükle
model = YOLO(r"C:\Users\ahmet\PycharmProjects\pythonProject\yolo\runs\detect\mobilnetv3\weights\best.pt")  # Eğitimli modelinizin yolunu yazın (örneğin: 'best.pt')

# Tahmin yapılacak görüntü
image_path = r"C:\Users\ahmet\Desktop\Ekran görüntüsü 2024-12-13 120957.png"  # Görüntü dosyanızın yolunu yazın

# Görüntüyü yükle
image = cv2.imread(image_path)

# Tahmin yap
results = model(image)

# Tahmin sonuçlarını ekranda göster
for result in results:
    annotated_frame = result.plot()  # Tahminleri görüntüye çizer
    cv2.imshow("Prediction", annotated_frame)
    cv2.waitKey(0)  # Bir tuşa basılmasını bekler
    cv2.destroyAllWindows()  # Pencereyi kapatır

# Tahmin sonuçlarını ekrana yazdır
print(results)
