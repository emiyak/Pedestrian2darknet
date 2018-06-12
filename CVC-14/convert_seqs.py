#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import glob
import cv2 as cv


def save_img(dname, fn, frame):
    str = '{}/{}_{}.png'.format(
        out_dir, os.path.basename(dname),
        os.path.basename(fn).split('.')[0])
    cv.imwrite(str, frame)
    return str

out_dir = 'img'
if not os.path.exists(out_dir):
    os.makedirs(out_dir)
for dname in sorted(glob.glob('*')):
    for fname in sorted(glob.glob('{}/*'.format(dname))):
            for ename in sorted(glob.glob('{}/*'.format(fname))):
                for fn in sorted(glob.glob('{}/FramesPos/*.tif'.format(ename))):
                    txt = '{}/Annotations/{}.txt'.format(ename, os.path.basename(fn).split('.')[0])
                    if not os.path.exists(txt):
                        continue
                    frame = cv.imread(fn)
                    path = save_img(fname, fn, frame)
                    #img = cv.imread(path)
                    height, width, channels = frame.shape
                    
                    with open(txt) as f:
                        content = f.readlines()
                        content = [x.strip() for x in content]
                        with open('anno/{}_{}.txt'.format(os.path.basename(fname),os.path.basename(fn).split('.')[0]) , 'w')  as out_file:
                            
                            for line in content:
                                line = line.split()
                                x = int(line[0])/width
                                y = int(line[1])/height
                                w = int(line[2])/width
                                h = int(line[3])/height
                                out_file.write("0 "+ " ".join([str(a) for a in (x,y,w,h)]) + "\n")
                        

                    print(fn)
