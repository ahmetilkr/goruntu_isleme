import cv2

img=cv2.imread("kuslar.jpg")
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh=cv2.threshold(img_gray,127,255,cv2.THRESH_BINARY_INV) #nesneleri beyaza döndürdük
contours,hierarchy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) #beyaza dönen nenlerinin sınırlarını buldu
for cnt in contours:
    if cv2.contourArea(cnt)>100: #beyaza dönen nenenin alanı 100 den büyükse
       #cv2.drawContours(img,cnt,-1,(0,255,0),1)
       x1,y1,w,h=cv2.boundingRect(cnt)  #kontrları bularak sınırları döndürür
       cv2.imshow("r",cv2.rectangle(img,(x1,y1),(x1+w,y1+h),(0,255,0),2)) #belirlenen alanı dikdörtgen çizdi sol üst köşesi
                                                                                   #ve sağ alt köşesini belirledik

cv2.imshow("img__gray",img_gray)
cv2.imshow("thresh",thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
