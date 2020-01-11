'''
Created by Wang Qiu Li
1/11/2020

make dirs for all scans
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

caselist = os.listdir(imagedir)
masklist = os.listdir(maskdir)
for oneScanId in idscaninfo:
    caseid = oneScanId[0][:14]
    if caseid in caselist:
        os.makedirs(imagedir+oneScanId[0])
        os.makedirs(maskdir+oneScanId[0])
