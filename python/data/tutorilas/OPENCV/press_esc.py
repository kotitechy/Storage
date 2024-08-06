import cv2

img = cv2.imread('lena.jpg', -1)
cv2.imshow('lena', img)
k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('c'):
    print('image copied')
    img = cv2.imread('krshn.jpg', 0)
    cv2.imwrite('lena_copy.png', img)
    cv2.destroyAllWindows()