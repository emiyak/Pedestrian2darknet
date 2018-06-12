import os
path = '/media/graymatics/backup/lize/dataset/Pedestrian/Caltech_Pedestrian/JPEG/'
outpath = '/media/graymatics/backup/lize/dataset/Pedestrian/Caltech_Pedestrian/JPEGImages/'
#if not os.path.exists(outpath):
#	os.makedirs(outpath)
for folder in os.listdir(path):
	#if folder != '.DS_Store':
		print(folder)
		for camera in os.listdir(os.path.join(path, folder)):
				print(camera)
			#if camera != '.DS_Store':
				cameraPath = os.path.join(os.path.join(path, folder),camera)
				for file in os.listdir(cameraPath):
					dstname = folder + '_' + camera + '_' + file
					dst = os.path.join(outpath,dstname)
					src = os.path.join(path,folder,camera,file)
					print ("rename from {} -> {}".format(src,dst))
					os.rename(src,dst)
