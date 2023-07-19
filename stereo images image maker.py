import cv2
import numpy as np

img0 = cv2.imread('Figure1.jpg')
img1 = cv2.imread('Figure1.jpg')
img2 = cv2.imread('Figure1.jpg')

im0_info = img0.shape
height = im0_info[0]
width = im0_info[1]

cv2.namedWindow('window', cv2.WINDOW_NORMAL)

img1[:, :, 0] = 0
img1[:, :, 2] = 0

img2[:, :, 1] = 0

translation = np.float32([[1, 0, 20], [0, 1, 0]])

img1 = cv2.warpAffine(img1, translation, (width, height))

img3 = cv2.addWeighted(img1, 1.0, img2, 1.0, 0)

img3 = img3[:, 20:]
cv2.imshow('window', img3)
cv2.imwrite('3D.png', img3)
cv2.waitKey(0)
cv2.destroyAllWindows()

