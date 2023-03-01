import cv2
import time
import subprocess

# Load the Haar Cascade face detection model
face_cascade = cv2.CascadeClassifier(r'C:\Users\Admin\AppData\Local\Programs\Python\Python39\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml')

# Open the default camera
cap = cv2.VideoCapture(0)

# Initialize the last detected face time
last_detected_time = time.time()

# Set the time threshold for face detection (in seconds)
time_threshold = 2

# Loop over the video frames
while True:
    # Read a frame from the camera
    ret, frame = cap.read()
    
    frame = cv2.flip(frame, 1)
    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect faces in the grayscale frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    
    # If a face is detected, update the last detected face time
    if len(faces) > 0:
        last_detected_time = time.time()
    
    # If no face is detected for a certain amount of time, lock the screen
    if time.time() - last_detected_time > time_threshold:
        subprocess.run(['rundll32.exe', 'user32.dll,LockWorkStation'])
        
    # Draw a rectangle around each detected face
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, "Press q to close", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        
    # Show the frame
    cv2.imshow('Face Tracker', frame)
    
    # Check for the 'q' key to exit
    if cv2.waitKey(1) == ord('q'):
        break

# Release the camera and close the window
cap.release()
cv2.destroyAllWindows()
