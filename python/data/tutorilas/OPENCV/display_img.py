import cv2

img = cv2.imread("lena.jpg", 1)
# print(img)

cv2.imshow("imh", img)
cv2.waitKey(5000)
cv2.destroyAllWindows()