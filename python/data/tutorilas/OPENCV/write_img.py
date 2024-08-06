import cv2

img = cv2.imread('lena.jpg', -1)
# copying image
cv2.imwrite('lenacopy.png', img)