'''
Created by Wang Qiu Li
1/11/2020

get CT images and init masks
'''

import csvTools
import os
import pandas as pd
import pydicom
import scipy.misc
import cv2
import numpy as np
import glob

import xmlopt

basedir = '/home/wangqiuli/Data/LIDC/DOI/'
resdir = 'noduleimage/'
imagedir = 'ori_images/'
maskdir = 'ori_masks/'

noduleinfo = csvTools.readCSV('files/malignancy.csv')
idscaninfo = csvTools.readCSV('files/id_scan.txt')
maskinfo = glob.glob(maskdir)

def get_pixels_hu(ds):
    image = ds.pixel_array
    image = np.array(image , dtype = np.float32)
    intercept = ds.RescaleIntercept
    slope = ds.RescaleSlope
    image = image * slope
    image += intercept
    return image

caselist = os.listdir(imagedir)
masklist = os.listdir(maskdir)
for oneScanId in idscaninfo:
    caseid = oneScanId[0][:14]
    if caseid in caselist:
        LIDC_scan_path = basedir + oneScanId[0] + '/'
        Ori_scan_path = imagedir + oneScanId[0] + '/'
        Mask_scan_path = maskdir + oneScanId[0] + '/'

        filelist1 = os.listdir(LIDC_scan_path)
        slices_ori = []

        xmlfiles = []
        for onefile in filelist1:
            if '.dcm' in onefile:
                slices_ori.append(onefile)
            elif '.xml' in onefile:
                xmlfiles.append(onefile)

        slices = [pydicom.dcmread(LIDC_scan_path + s) for s in slices_ori]
        slices.sort(key = lambda x : float(x.ImagePositionPatient[2]),reverse=True)
        print(len(slices))
        
        slices_pix = []
        for oneslice in slices:
            tempPix = get_pixels_hu(oneslice)
            
            #use location as index
            tempMask = np.zeros(tempPix.shape)
            zloc = str(oneslice.ImagePositionPatient[2])
            slices_pix.append(tempPix)

            scipy.misc.imsave(Ori_scan_path + zloc + '.png', tempPix)
            scipy.misc.imsave(Mask_scan_path + zloc + '.png', tempMask)