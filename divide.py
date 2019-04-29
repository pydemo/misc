

#https://stackoverflow.com/questions/5605174/python-pil-function-to-divide-blend-two-images


import numpy as np
import scipy.misc as mpl

a = mpl.imread('01background.jpg')
b = mpl.imread('02testgray.jpg')

c = a/((b.astype('float')+1)/256)
d = c*(c < 255)+255*np.ones(np.shape(c))*(c > 255)

e = d.astype('uint8')

mpl.imshow(e)
mpl.imsave('output.png', e)
