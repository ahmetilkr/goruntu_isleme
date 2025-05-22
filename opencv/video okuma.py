import cv2
cap=cv2.VideoCapture("video.mp4")
while True:
    ret,frame=cap.read()
    if ret==0:
        break
    cv2.imshow("pencere",frame)
    if cv2.waitKey(1) & 0xFF ==ord("s"):
     break

cap.release()
cv2.destroyAllWindows()


