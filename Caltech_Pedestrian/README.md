# CaltechPestrian2VOC

将Caltech数据集转化成PASCAL VOC的格式，[下载地址](http://www.vision.caltech.edu/Image_Datasets/CaltechPedestrians/)

文件结构如下：其中红框中的是原始的文件夹，其余4个文件夹是在执行过程中生成的

![](./static/structure.png)

## 1. Seq文件转化成JEPG图像文件
## 1. Convert seq fils to jpeg files
 
调用seq2jpg.py文件，输入data文件夹，输出到JPEG文件夹中
input data dir, out put JPEG dir

## 2. VBB标注文件转化为XML文件
## 2. VBB to XML
调用vbb2voc.py文件，输入annotations文件夹，输出到xmlresult文件夹中
input annotations dir , output xmlresult dir

## 3. JPEG文件按照xml文件的命名格式进行重命名，并将所有的图像放在一个文件夹中
## 3. rename JPEG to same names as xmls and put them in one dir

调用rename_jpg.py文件，输入JPEG文件夹，输出到JPEGImages文件夹中
input JPEG dir , output JPEGImages dir


**IMPORTANT NOTES**
I found there're some errors in the vbb files. To be specific, some bounding boxes are out of the image such as the xmax is greater than the width of the image, which will cause big mistakes in training faster R-CNN. Therefore, you can mannually check the wrong xml files during training. Or I will try to correct the wrong bnd boxes later automatically.
