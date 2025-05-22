import cv2
import numpy as np
img=cv2.imread("basketball.jpg")
img_r=cv2.resize(img,(600,900))
#cv2.imshow("pencere",img_r)
img_edge=cv2.Canny(img_r,100,200)
cv2.imshow("img_edge",img_edge)
img_edge_d=cv2.dilate(img_edge,np.ones((3,3),dtype=np.int8)) #çizgileri belirgin hala getirme
cv2.imshow("img_edge_d",img_edge_d)
img_edge_e=cv2.erode(img_edge_d,np.ones((3,3),dtype=np.int8)) #kalın çizgileri daraltmak ve daha net görünütü elde etmek için
cv2.imshow("img_edge_e",img_edge_e)
cv2.waitKey(0)
cv2.destroyAllWindows()
