# -*- coding: utf-8 -*-
"""
@author: Soumyasis
"""
import os
from sys import platform

forged_path = "./signatures/full_forg/"
genuine_path = "./signatures/full_org/"

orig_groups, forg_groups = [], []
forged_images = os.listdir(forged_path)
forged_images.sort()
original_images = os.listdir(genuine_path)
original_images.sort()

path = "./cedar/"
try:
	os.makedirs(path)
except:
	print('Directory exists')
for i in range(1,56,1):
    try:
        os.makedirs(path+str(i).zfill(2)+'/')
        #os.makedirs(path+str(i).zfill(2)+'/forged/')
        #os.makedirs(path+str(i).zfill(2)+'/genuine/')
    except:
        print('Directories exist')
    
for image in forged_images:
    name = image.split('_')
    if(len(name)<3):
        continue
#     print(name)
    folder = name[1].zfill(2)
    orig_idx = name[2].split('.')[0]
    new_idx = orig_idx.zfill(2)
    new_name = name[0]+'_'+folder+'_'+new_idx+'.'+name[2].split('.')[1]
    command = 'cp '+ forged_path+image +' '+path+folder+'/'+ new_name
    #command = 'copy '+ forged_path+image +' '+path+folder+'/forged/'+ new_name
    print(command)
    os.system(command)
    
for image in original_images:
    name = image.split('_')
    if(len(name)<3):
        continue
#     print(name)
    folder = name[1].zfill(2)
    orig_idx = name[2].split('.')[0]
    new_idx = orig_idx.zfill(2)
    new_name = name[0]+'_'+folder+'_'+new_idx+'.'+name[2].split('.')[1]
    command = 'cp '+ genuine_path+image +' '+path+folder+'/'+ new_name
    #command = 'copy '+ forged_path+image +' '+path+folder+'/genuine/'+ new_name
    print(command)
    os.system(command)
