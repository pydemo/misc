import cv2
img = cv2.imread('test.jpg')
print('original image shape:', img.shape)
if 1:
	width, height = 128, 256
	resized_img = cv2.resize(img, (width, height))
	print('resized to 128x256 image shape:', resized_img.shape)
	#cv2.imshow("detected lines", resized_img)
	#cv2.waitKey(0)
	
w_mult, h_mult = 2, 4
resized_img = cv2.resize(img, (0, 0), resized_img, w_mult, h_mult, cv2.INTER_NEAREST)
print('half sized image shape:', resized_img.shape)	

cv2.imwrite('test_resized.jpg', resized_img)

