import cv2
face_cas=cv2.CascadeClassifier('haarcascade_frontalface_alt_tree.xml')
vid=cv2.VideoCapture(0)
while vid.isOpened():
    ret,frame=vid.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces_reg=face_cas.detectMultiScale(gray,1.1,4)
    for (x,y,w,h) in faces_reg:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(100,84,0),4)

    cv2.imshow('video',frame)
    if cv2.waitKey(2)& 0xFF==ord('s'):
        break
vid.release()