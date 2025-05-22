import cv2
img=cv2.imread("kedi.jpg")
print(img.shape)
cropped_img=img[50:213, 50:237] # 0 den 213e kadar olan kısmı al
cv2.imshow("pencere",cropped_img)
cv2.waitKey(0)