import cv2
face=cv2.imread("face.jpg")
#cv2.imshow("pencere",face)
k_size=7
face_blur=cv2.blur(face,(k_size,k_size))
gaussian_blur=cv2.GaussianBlur(face,(k_size,k_size),3)
median_blur=cv2.medianBlur(face,k_size)
cv2.imshow("blur_pencere",face_blur)
cv2.imshow("gaussian_blur_pencere",gaussian_blur)
cv2.imshow("median_blur_pencere",k_size)
cv2.waitKey(0)
cv2.destroyAllWindows()