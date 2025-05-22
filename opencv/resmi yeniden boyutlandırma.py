import cv2
img=cv2.imread("kedi.jpg")
print(img.shape) #fotoğraf boyutu görme
resized_img=cv2.resize(img,(900,640))
print(resized_img.shape)
cv2.imshow("pencere",resized_img)
cv2.waitKey()
