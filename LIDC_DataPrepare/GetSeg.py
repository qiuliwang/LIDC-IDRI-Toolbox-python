'''
Created by Wang Qiu Li
1/11/2020

get segmentation for nodules
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

caselist = os.listdir(imagedir)
masklist = os.listdir(maskdir)

noduleinfo = csvTools.readCSV('files/malignancy.csv')
idscaninfo = csvTools.readCSV('files/id_scan.txt')

def get_pixels_hu(ds):
    image = ds.pixel_array
    image = np.array(image , dtype = np.float32)
    intercept = ds.RescaleIntercept
    slope = ds.RescaleSlope
    image = image * slope
    image += intercept
    return image

def truncate_hu(image_array, max, min):

    image_array[image_array > max] = max
    image_array[image_array < min] = min
    return image_array
    
def caseid_to_scanid(caseid):
    returnstr = ''
    if caseid < 10:
        returnstr = '000' + str(caseid)
    elif caseid < 100:
        returnstr = '00' + str(caseid)
    elif caseid < 1000:
        returnstr = '0' + str(caseid)
    else:
        returnstr = str(caseid)
    return 'LIDC-IDRI-' + returnstr

tempsign = 0

import tqdm



for onenodule in tqdm.tqdm(noduleinfo):
    xml = ''
    # try:
    case_id = onenodule[1]
    case_id = caseid_to_scanid(int(case_id))
    nodule_id = onenodule[3]
    scan_list_id = onenodule[2]

    if case_id not in caselist:
        break
    else:
        todo
    