import cv2

image = cv2.imread('img.png')

cv2.imshow('Image', image)
cv2.waitkey(0)
cv2.destroyAllWindows()