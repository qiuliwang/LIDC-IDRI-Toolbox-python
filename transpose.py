'''
Created by Wang Qiu Li
7/3/2018

get dicom info according to malignancy.csv and ld_scan.txt
'''

import numpy as np
import os
from PIL import Image
import csvTools
datadir = '/data0/LIDC/NNPY/'
testdir = '/home/wangqiuli/Documents/test/'

def angle_transpose(file,degree,flag_string):
    '''
     @param file : a npy file which store all information of one cubic
     @param degree: how many degree will the image be transposed,90,180,270 are OK
     @flag_string:  which tag will be added to the filename after transposed
    '''
    array = np.load(file)       
    array = array.transpose(2,1,0)

    newarr = np.zeros(array.shape,dtype=np.float32)
    for depth in range(array.shape[0]):
        jpg = array[depth]
        jpg.reshape((jpg.shape[0],jpg.shape[1],1))
        img = Image.fromarray(jpg)
        #img.show()
        out = img.rotate(degree)  # 逆时针旋转90度
        newarr[depth,:,:] = np.array(out).reshape(array.shape[1],-1)[:,:]
    newarr = newarr.transpose(2,1,0)
    print(newarr.shape)
    np.save(file.replace(".npy",flag_string+".npy"),newarr)

x = np.load('1_high.npy')
print(x.shape)
angle_transpose('1_high.npy', 90, '_leftright')

# filelist = os.listdir(datadir)

# errfile = []
# for onefile in filelist:
#     print(datadir + onefile)
#     try:
#         angle_transpose(datadir + onefile,90,"_leftright")
#         angle_transpose(datadir + onefile, 180, "_updown")
#         angle_transpose(datadir + onefile, 270, "_diagonal")
#     except BaseException:
#         print(onefile)
#         errfile.append(onefile)

# csvTools.writeTXT('errfile.txt', errfile)