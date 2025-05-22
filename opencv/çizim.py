import cv2
img=cv2.imread("tahta.jpg")
img_re=cv2.resize(img,(900,600))
cv2.imshow("pencere",img_re)
img_l=cv2.line(img_re,(100,150),(300,450),(0,255,0),3)
cv2.imshow("img_l",img_l)
img_r=cv2.rectangle(img_re,(200,350),(400,600),(0,0,255),5) #ilk parametre sol üst ikinci sağ alt üçüncü renk dördüncü kalınlık
cv2.imshow("dikdörtgen",img_r)
img_c=cv2.circle(img_re,(500,300),150,(255,0,0),5)
cv2.imshow("circle",img_c)
img_t=cv2.putText(img_re,"ahmet",(300,450),cv2.FONT_HERSHEY_SIMPLEX,10,(255,255,0),5)
cv2.imshow("text",img_t)
cv2.waitKey(0)
cv2.destroyAllWindows()
