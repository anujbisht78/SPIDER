import cv2

# Load the trained model
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('Trainer/trainer.yml')

# Load the cascade classifier
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Create a dictionary to map IDs to names
names = {0: "Anuj",}

# Set the confidence threshold for face recognition
confidence_threshold = 70

# Open the webcam
video_capture = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = faceCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        # Recognize the face
        id, confidence = recognizer.predict(gray[y:y+h, x:x+w])

        # Check if the face is recognized
        if confidence < confidence_threshold:
            name = names[id]
        else:
            name = "Unknown"

        # Draw a rectangle around the face and display the name
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, name, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('Video', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and destroy the windows
video_capture.release()
cv2.destroyAllWindows()