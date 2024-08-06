import cv2

# Initialize the camera
camera = cv2.VideoCapture(0)

# Check if the camera is opened successfully
if not camera.isOpened():
    print("Error: Couldn't open camera.")
    exit()

# Capture a frame
ret, frame = camera.read()

# Check if the frame is captured successfully
if not ret:
    print("Error: Couldn't capture frame.")
    exit()

# Release the camera
camera.release()

# Save the captured frame as an image
cv2.imwrite("captured_photo.jpg", frame)

print("Photo captured successfully!")
