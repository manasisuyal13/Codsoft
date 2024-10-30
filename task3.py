import cv2
import os

# Initialize the Haar Cascade classifier
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Directory for saved images
output_path = 'output_faces'
os.makedirs(output_path, exist_ok=True)

def detect_faces_in_image(image_path):
    """Detects faces in a given image file, adds 'Face Detected' text, saves the result, and confirms detection."""
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.putText(img, "Face Detected", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)
    
    # Save the processed image
    output_image_path = os.path.join(output_path, "detected_faces_image.jpg")
    cv2.imwrite(output_image_path, img)
    print(f"Face detection complete! Saved the image with detected faces at {output_image_path}")
    
    # Print final detection confirmation
    if len(faces) > 0:
        print("Face(s) detected successfully in the image!")

def detect_faces_from_webcam():
    """Detects faces from a live webcam feed, saves each frame with detected faces, stops after 50 frames, and confirms detection."""
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Could not open webcam.")
        return
    
    frame_count = 0
    while frame_count < 50:  # Stop after 50 frames
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            # Add text only in the 50th frame
            if frame_count == 49:
                cv2.putText(frame, "Face Detected", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

        # Save each frame with detected faces
        frame_filename = os.path.join(output_path, f"webcam_frame_{frame_count}.jpg")
        cv2.imwrite(frame_filename, frame)
        frame_count += 1
        print(f"Saved frame {frame_count} with detected faces.")

    cap.release()
    print("Face detection from webcam is complete! 50 frames processed and saved in the 'output_faces' folder.")

    # Print final detection confirmation
    if frame_count > 0:
        print("Face(s) detected successfully in webcam feed!")

# Prompt the user for input
choice = input("Would you like to detect faces from an 'image' or 'webcam'? ").strip().lower()

if choice == 'image':
    image_path = input("Please provide the path to the image file: ").strip()
    detect_faces_in_image(image_path)
elif choice == 'webcam':
    detect_faces_from_webcam()
else:
    print("Invalid choice. Please enter 'image' or 'webcam'.")
