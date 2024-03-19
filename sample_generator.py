import cv2
from Body.speak import speak

cam= cv2.VideoCapture(0)
cam.set(3,640)
cam.set(4,480)


detector=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

speak("Enter a user ID Number")
face_id=input()
speak("Please Enter Your Good Name")
face_name=input()
1
speak("Taking samples, Please look at the camera..........")
count=0

while True:
    ret,img=cam.read()
    converted_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=detector.detectMultiScale(converted_image,1.3,5)

    for (x,y,w,h) in faces:
        
        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0),2)
        count+=1
        
        cv2.imwrite("Samples/face." + str(face_id) + '.' + str(count) + ".jpg", converted_image[y:y+h, x:x+w])

        cv2.imshow('image', img)
        
    k=cv2.waitKey(100) & 0xff
    if k==27:
        break
    elif count>=20:
        break
    
speak("Samples has been taken now.")
speak("Thankyou for your Cooperation")
cam.release()
cv2.destroyAllWindows()
