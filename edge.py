#!/usr/bin/python

'''
This example illustrates how to use Hough Transform to find lines

Usage:
    houghlines.py [<image_name>]
    image argument defaults to ../data/pic1.png
'''

# Python 2/3 compatibility
from __future__ import print_function

import cv2
import numpy as np
import sys
import math
from numpy import zeros, uint8
from datetime import  datetime
from sys import exit
import os
from types import *

e=exit
ts = str(datetime.utcnow()).replace(' ','_').replace(':','_')
print (ts)
#e(0)
# read image
models='SAMSUNG_100MSDCF' 
models=r'insta\ukraine' 
models='lino21'
in_path='in/%s' % models
#in_path=r'C:\Users\a lex_buz\Pictures\Samsung\100MSDCF'
#gsnl= list(set([x for x in dir(cv2) if x.startswith('COLOR_')]))
#for gscale_name in gsnl:

        
if __name__ == '__main__':

    print(__doc__)

    import cv2
    import numpy as np


    out_path=os.path.join(in_path,'edge',ts)

    if not os.path.isdir(out_path): 
        os.makedirs(out_path)   
    #e(0)
    for i,f in enumerate(os.listdir(in_path)):
        in_img=os.path.join(in_path,f)
        print (f)
        if os.path.isdir(in_img):
            continue
        out_img=os.path.join(out_path,f)        
        #fn = "../data/pic1.png"
        img = cv2.imread(in_img, cv2.IMREAD_GRAYSCALE)
        rows, cols = img.shape
        sobel_horizontal = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
        sobel_vertical = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)   
        #cv2.imshow('Original', img)
        #cv2.imshow('Sobel horizontal', sobel_horizontal)
        #cv2.imshow('Sobel vertical', sobel_vertical)

        #cv2.waitKey(0)             
        cv2.imwrite(os.path.join(out_path, "edge_h_%s" %  f), sobel_horizontal)
        cv2.imwrite(os.path.join(out_path, "edge_v_%s" %  f), sobel_vertical)
        #e(0)

