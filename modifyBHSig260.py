import os 
import numpy as np

BHSig260_path = './BHSig260/'
BHSig260mod_path = './BHSig260modified/'

def check_dir(dir_path):
	if not os.path.exists(dir_path):
		os.makedirs(dir_path)


ind_count = 10


#Parsing through BHSig260 dataset to convert it into forged and genuine data split
for root,dirs,files in sorted(os.walk(BHSig260_path)):
	ind_count=ind_count+1
	if ind_count > 99:
		ind_id = str(ind_count)
	else:
		ind_id = '0' + str(ind_count) 	

	for file in sorted(files):
		fpath = os.path.join(root,file)

		if fpath.endswith(('.bmp','.tif','.jpg','.jpeg','.png')):
			# print(fpath)
			# print(ind_count)
			ForG = fpath.split('-')[-2] #F or G
			img_count = int(fpath.split('-')[-1][:-4]) -1 
			# print(img_count)

			if img_count > 9:
				img_no = '0' + str(img_count)
			else:
				img_no = '00' + str(img_count)

			if ForG == 'F':
				img_id = '021'+ str(ind_id) + '_' + str(img_no) + '.tif'
				command = 'cp '+ fpath +' '+os.path.join(BHSig260mod_path,'forged/')+ img_id
				os.system(command)
				# print(command)
			else:
				img_id = str(ind_id) + str(ind_id) + '_' + str(img_no) + '.tif'
				command = 'cp '+ fpath +' '+os.path.join(BHSig260mod_path,'genuine/')+ img_id
				# print(command)
				os.system(command)
					

#Copying english dataset into forged and genuine split

cmd = 'cp '+'./data/forged/*' + ' ' + os.path.join(BHSig260mod_path,'forged/')
os.system(cmd)
cmd = 'cp '+'./data/genuine/*' + ' ' + os.path.join(BHSig260mod_path,'genuine/')
os.system(cmd)


