import cv2
img=cv2.imread("kus.jpg")
img_rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #renk uzazyı değiştirme
img_hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.imshow("pencere",img)
#cv2.imshow("pencere",img_gray)
#cv2.imshow("pencere_gray",img_rgb)
cv2.imshow("pencere",img_hsv)
cv2.waitKey(0)
cv2.destroyAllWindows()