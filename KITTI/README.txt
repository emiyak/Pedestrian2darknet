KITTI labels are in txt format, stuctured as followed:

The label files contain the following information, which can be read and
written using the matlab tools (readLabels.m) provided within this devkit. 
All values (numerical or strings) are separated via spaces, each row 
corresponds to one object. The 17 columns represent:

#Values    Name      Description
----------------------------------------------------------------------------
   1    frame        Frame within the sequence where the object appearers
   1    track id     Unique tracking id of this object within this sequence
   1    type         Describes the type of object: 'Car', 'Van', 'Truck',
                     'Pedestrian', 'Person_sitting', 'Cyclist', 'Tram',
                     'Misc' or 'DontCare'
   1    truncated    Integer (0,1,2) indicating the level of truncation.
                     Note that this is in contrast to the object detection
                     benchmark where truncation is a float in [0,1].
   1    occluded     Integer (0,1,2,3) indicating occlusion state:
                     0 = fully visible, 1 = partly occluded
                     2 = largely occluded, 3 = unknown
   1    alpha        Observation angle of object, ranging [-pi..pi]
   4    bbox         2D bounding box of object in the image (0-based index):
                     contains left, top, right, bottom pixel coordinates
   3    dimensions   3D object dimensions: height, width, length (in meters)
   3    location     3D object location x,y,z in camera coordinates (in meters)
   1    rotation_y   Rotation ry around Y-axis in camera coordinates [-pi..pi]
   1    score        Only for results: Float, indicating confidence in
                     detection, needed for p/r curves, higher is better.

Pls note that KITTI labels for each dataset may be different. In this case one txt file contains labels of many images. For other datasets that could be the case of one txt to one image.

So firstly, convert_txt should be used to split txt files so there will be one txt for each image.

Then changetxt is used to combine classes or discard some classes.

txt2voc is used to change txt to voc format.

├── 0000
├── 0001
├── 0002
├── 0003
├── 0004
├── 0005
├── 0006
├── 0007
├── 0008
├── 0009
├── 0010
├── 0011
├── 0012
├── 0013
├── 0014
├── 0015
├── 0016
├── 0017
├── 0018
├── 0019
├── 0020
└── renamejpg.py

renamejpg is used to rename jpgs to same names as txts and place them in target folder.
