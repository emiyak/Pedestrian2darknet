#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import glob
import cv2 as cv

with open('label.txt') as f:
    content = f.readlines()
    content = [x.strip() for x in content]
    print(content)
    for line in content:
        #path = line[line.find("\"")+1:line.find("\"")]
        path = line.split(':')[0][1:-1]
        img = cv.imread(str(path))
        print(path)
        height,width,channels= img.shape
        boxes = [p.split(')')[0] for p in line.split('(') if ')' in p]
        with open(path.split('.')[0]+'.txt','w') as out:
            for box in boxes:
                coor = box.split(',')
                coor = [int(x.strip()) for x in coor]
                x = (coor[0] + coor[2])/2/width
                y = (coor[1] + coor[3])/2/height
                w = abs(coor[2] - coor[0])/width
                h = abs(coor[3] - coor[1])/height
                out.write("0 "+ " ".join([str(a) for a in (x,y,w,h)]) + "\n")
        

