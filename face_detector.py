import cv2
import numpy as np
from PIL import Image
import os

path='Samples'

recognizer=cv2.face.LBPHFaceRecognizer_create()
detector=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")


def Images_and_labels(path):
    
    imagePaths=[os.path.join(path,f) for f in os.listdir(path)]
    faceSamples=[]
    ids=[]

    for imagePath in imagePaths:
        
        gray_img=Image.open(imagePath).convert('L')
        img_arr=np.array(gray_img,'uint8')

        id=int(os.path.split(imagePath)[-1].split(".")[1])
        faces=detector.detectMultiScale(img_arr)

        for (x,y,w,h) in faces:
            faceSamples.append(img_arr[y:y+h, x:x+w])
            ids.append(id)

    return faceSamples,ids

print("<< Training faces. It will take few seconds... >>")
print("<< Please Wait ! >>")

faces,ids=Images_and_labels(path)
recognizer.train(faces, np.array(ids))

recognizer.write('Trainer/trainer.yml')

print("<< Model has been Trained >> ")
print("<< Now we can recognize your Face ! >>")