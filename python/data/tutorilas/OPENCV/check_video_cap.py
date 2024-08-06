import cv2 

cap = cv2.VideoCapture(0)
print(cap.isOpened())

# cap properties
import cv2 

cap = cv2.VideoCapture(0)
print(cap.isOpened())
while(cap.isOpened()):
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', frame)
    print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
# opencv --> prperties of cv2.cap ('opencv\Flags for video i/o')
