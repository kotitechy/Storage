import cv2

# Initialize the camera
camera = cv2.VideoCapture(0)

# Check if the camera is opened successfully
if not camera.isOpened():
    print("Error: Couldn't open camera.")
    exit()

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')  # You can also use other codecs like 'MJPG'
out = cv2.VideoWriter('captured_video.avi', fourcc, 20.0, (640, 480))  # Adjust frame size and FPS as needed

while True:
    # Capture frame-by-frame
    ret, frame = camera.read()

    # Check if the frame is captured successfully
    if not ret:
        print("Error: Couldn't capture frame.")
        break

    # Write the frame into the output video
    out.write(frame)

    # Display the resulting frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to exit
        break

# Release everything when done
camera.release()
out.release()
cv2.destroyAllWindows()
