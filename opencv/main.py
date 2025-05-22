import cv2
from util import get_limits
from PIL import Image
yellow=[0,255,255]
cap=cv2.VideoCapture(0)
while True:
    ret,frame=cap.read()
    hsv_img=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)#hsv formatı ggörüntüde renk tespiti yapmak için daha uygundur
    lowerLimit,upperLimit=get_limits(yellow)
    mask=cv2.inRange(hsv_img,lowerLimit,upperLimit) #sarı rengin alt ve üst sınırlarını belirledik bu sınırlar arasında kalan alanlar beyaz diğer alanlar siyah olur
    mask_=Image.fromarray(mask) #matrisleri bir pillow görüntüsüne dönüştürür
    bbox=mask_.getbbox() #beyaz alan içerisindeki dikdörtgenin değerini döndürür üstteki dönüşümü bunu kullanmak için yaptık
    if bbox is not None:
        x1,y1,x2,y2=bbox
        x=cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),5)
    cv2.imshow("mask",frame)
    if cv2.waitKey(1)&0xFF == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()