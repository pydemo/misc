import cv2
from sys import exit
img = cv2.imread('test.jpg')
print('original image shape:', img.shape)
if 1:
	width, height = 128, 256
	resized_img = cv2.resize(img, (width, height))
	print('resized to 128x256 image shape:', resized_img.shape)
	#cv2.imshow("detected lines", resized_img)
	#cv2.waitKey(0)
	
img_flip_along_x = cv2.flip(img, -1)

cv2.imwrite('test_flipped.jpg', img_flip_along_x)
#cv2.imshow("detected lines", resized_img)
#cv2.waitKey(0)
#exit(0)

