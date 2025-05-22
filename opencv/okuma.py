import cv2
resim=cv2.imread("kedi.jpg", 0)
cv2.imshow("pencere",resim)
cv2.waitKey(0)
cv2.destroyAllWindows()
