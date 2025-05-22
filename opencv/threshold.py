import cv2
img=cv2.imread("kus.jpg")
cv2.imshow("pencere",img)
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh=cv2.threshold(img_gray,130,255,cv2.THRESH_BINARY) #görüntyü siyah beyaza çevirir
cv2.imshow("thresh",thresh)
thresh=cv2.blur(thresh,(10,10)) #görüntüdeki gürültüyü azalatır siyah nokta vb..
ret,thresh=cv2.threshold(thresh,80,255,cv2.THRESH_BINARY)
cv2.imshow("thresh",thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
