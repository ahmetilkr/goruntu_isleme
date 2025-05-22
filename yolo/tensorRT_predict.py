import cv2
import time
from ultralytics import YOLO
import torch

# from ultralytics import YOLO
#
# # YOLOv8 modelini yükle (Önceden eğitilmiş veya kendi modelin olabilir)
# model = YOLO(r"C:\Users\ahmet\PycharmProjects\pythonProject\yolo\runs\detect\train2\weights\best.pt")
#
# # Modeli TensorRT formatına (.engine) dönüştür
# model.export(format="engine")

# TensorRT modeli kullanıyoruz
model_path = r"C:\Users\ahmet\PycharmProjects\pythonProject\yolo\runs\detect\train2\weights\best.engine"

cap = cv2.VideoCapture(r"C:\Users\ahmet\PycharmProjects\pythonProject\yolo\videolar\iki_ucak.mp4")

#cap = cv2.VideoCapture(r"C:\Users\ahmet\PycharmProjects\pythonProject\yolo\videolar\VID-20241005-WA0004~3.mp4")
fps_list = []
video_fps = cap.get(cv2.CAP_PROP_FPS)
prev_frame_time = time.time()
new_frame_time = 0

if not cap.isOpened():
    print("Video dosyası açılamadı.")
    exit()

# TensorRT modelini yükle
model = YOLO(model_path)

device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Model cihazı: {device}")

prev_frame_time = 0

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("Video sonlandı veya okunamadı.")
        break

    frame = cv2.resize(frame, (1200,900))
    print(frame.shape)
    height, width, _ = frame.shape
    frame = cv2.rectangle(frame, ((width // 4), (height // 10)), ((width * 3 // 4, height * 9 // 10)), (0, 255, 255), 2)

    # TensorRT modeli ile tahmin yap
    results = model.predict(frame, stream=True, device="cuda",imgsz=704)  # TensorRT için cihazı açıkça belirt

    for result in results:
        boxes = result.boxes
        for box in boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            accuracy = int(box.conf[0] * 100)
            color = (0, 255, 0) if (x2 - x1 < width * 0.05 and y2 - y1 < height * 0.05) else (0, 0, 255)

            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
            cv2.putText(frame, f"fixed wing UAV={accuracy}%", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)

            cv2.circle(frame, (width // 2, height // 2), 4, (0, 0, 0), -1)
            cv2.circle(frame, ((x1 + x2) // 2, (y1 + y2) // 2), 4, (0, 0, 0), -1)
            cv2.line(frame, (width // 2, height // 2), ((x1 + x2) // 2, (y1 + y2) // 2), (0, 0, 0), thickness=2)
    new_frame_time = time.time()
    fps = int(1 / (new_frame_time - prev_frame_time)) if prev_frame_time else 0
    prev_frame_time = new_frame_time

    fps_list.append(fps)
    if len(fps_list) > 10:  # Son 10 FPS değerini baz al
        fps_list.pop(0)
    smoothed_fps = sum(fps_list) / len(fps_list)  # Ortalama FPS

    cv2.putText(frame, f"FPS: {int(smoothed_fps)} / Video FPS: {int(video_fps)}", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    cv2.imshow("Predicted and tracking", frame)

    # new_frame_time = time.time()
    # fps = int(1 / (new_frame_time - prev_frame_time)) if prev_frame_time else 0
    # prev_frame_time = new_frame_time
    # cv2.putText(frame, f"fps={fps}", ((width // 4 + 5), (height // 10 + 35)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 1)
    # cv2.imshow("Detection", frame)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
