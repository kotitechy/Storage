import cv2 

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')  # foucc code
output = cv2.VideoWriter("t1.avi", fourcc, 20.0, (640,480))
# four args output file, fourcc code, frames persecond, framewidth, height


print(cap.isOpened())
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:

        print('widthxheight')
        output.write(frame)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', frame)


        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
output.release()
cv2.destroyAllWindows()
