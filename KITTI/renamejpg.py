#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import glob
import cv2 as cv
import shutil

dst_dir= "/media/graymatics/backup/lize/dataset/Pedestrian/KITTI/training/label_02/img/"
for dname in sorted(glob.glob('*')):
            for fname in sorted(glob.glob('{}/*.png'.format(dname))):
                    new_name = dst_dir + 'KITTI_'+os.path.basename(dname)+"_"+os.path.basename(fname)
                    shutil.copy(fname , new_name)
                    
                    

