import cv2
import mediapipe as mp
cap=cv2.VideoCapture("adam.mp4")
mpfacedetection=mp.solutions.face_detection
facedetection=mpfacedetection.FaceDetection()
while True:
    succes,img=cap.read()
    img_rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

    results=facedetection.process(img_rgb)
    #print(results.detections)
    if results.detections:
        for id,detections in enumerate(results.detections):
          bboxC=detections.location_data.relative_bounding_box
          #print(bboxC)
          h,w,_=img.shape
          bbox=int(bboxC.xmin*w),int(bboxC.ymin*h),int(bboxC.widht*w),int(bboxC.height*h)
          cv2.rectangle(img,bbox,(0,255,255),2)

    cv2.imshow("img",img)
    cv2.waitKey(10)



