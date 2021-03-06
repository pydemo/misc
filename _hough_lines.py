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
e=exit
ts = str(datetime.utcnow()).replace(' ','_').replace(':','_')
print (ts)
#e(0)
# read image
in_path='in/models3'
#gsnl= list(set([x for x in dir(cv2) if x.startswith('COLOR_')]))
#for gscale_name in gsnl:



if __name__ == '__main__':

    print(__doc__)


    #gscale_name='IMREAD_GRAYSCALE'

    out_path=os.path.join('out','models3','houghlines',ts)

    if not os.path.isdir(out_path): 
        os.makedirs(out_path)

    
    
    #e(0)
    for i,f in enumerate(os.listdir(in_path)):
        in_img=os.path.join(in_path,f)
    
        out_img=os.path.join(out_path,f)        
        #fn = "../data/pic1.png"

        src = cv2.imread(in_img)
        dst = cv2.Canny(src, 50, 200)
        cdst = cv2.cvtColor(dst, cv2.COLOR_GRAY2BGR)

        if True: # HoughLinesP
            lines = cv2.HoughLinesP(dst, 1, math.pi/180.0, 40, np.array([]), 50, 10)
            a,b,c = lines.shape
            for i in range(a):
                cv2.line(cdst, (lines[i][0][0], lines[i][0][1]), (lines[i][0][2], lines[i][0][3]), (0, 0, 255), 3, cv2.LINE_AA)

        else:    # HoughLines
            lines = cv2.HoughLines(dst, 1, math.pi/180.0, 50, np.array([]), 0, 0)
            a,b,c = lines.shape
            for i in range(a):
                rho = lines[i][0][0]
                theta = lines[i][0][1]
                a = math.cos(theta)
                b = math.sin(theta)
                x0, y0 = a*rho, b*rho
                pt1 = ( int(x0+1000*(-b)), int(y0+1000*(a)) )
                pt2 = ( int(x0-1000*(-b)), int(y0-1000*(a)) )
                cv2.line(cdst, pt1, pt2, (0, 0, 255), 3, cv2.LINE_AA)

        #cv2.imshow("source", src)
        #cv2.imshow("detected lines", cdst)
        #cv2.waitKey(0)
        cv2.imwrite(out_img,cdst)
        #e(0)
