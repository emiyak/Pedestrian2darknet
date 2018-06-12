#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import glob
import cv2 as cv

#change this dir to your dir
#move all produced txts to one dir after execution of this script
for dname in sorted(glob.glob('*.txt')):
	with open(dname) as f:
		content = f.readlines()
		content = [x.strip() for x in content]
		for line in content:
                        number = line.split()[0].zfill(6)
                        filename = 'KITTI_'+os.path.basename(dname).split('.')[0]+'_'+number+'.txt'
                        if not os.path.exists(filename):
                                file= open(filename,"a+")
                        else:
                                file= open(filename,"a")
                        file.write(" ".join(line.split()[1:]) + "\n")
                                
                        

