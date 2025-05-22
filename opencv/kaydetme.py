import cv2
resim=cv2.imread("kedi.jpg",0)
cv2.imshow("pencere",resim)
cv2.imwrite("kedilogogri.jpg",resim)
a=cv2.waitKey(0)
if a==27:
    cv2.destroyAllWindows()
elif a==ord("s"):
    cv2.imwrite("s_tusu_grikedi.jpg",resim)



