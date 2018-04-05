import argparse
import cv2
parser = argparse.ArgumentParser()
parser.add_argument('--path', default='test.jpg', help='Image path.')
params = parser.parse_args()
print('read {} as grayscale'.format(params.path))
img = cv2.imread(params.path)

assert img is not None  # check if the image was successfully loaded
print('read {}'.format(params.path))
print('shape:', img.shape)
print('dtype:', img.dtype)



img = cv2.imread(params.path, cv2.IMREAD_GRAYSCALE)
assert img is not None
print('read {} as grayscale'.format(params.path))
print('shape:', img.shape)
print('dtype:', img.dtype)


