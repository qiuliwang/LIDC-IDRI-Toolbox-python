'''
Created by Wang Qiu Li
1/11/2020

make dirs for all cases
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

basedir = '/Data/LIDC/DOI/'
resdir = 'noduleimage/'
imagedir = 'ori_images/'
maskdir = 'ori_masks/'

noduleinfo = csvTools.readCSV('files/malignancy.csv')
idscaninfo = csvTools.readCSV('files/id_scan.txt')
maskinfo = glob.glob(maskdir)

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

import tqdm

case_list = []
for onenodule in tqdm.tqdm(noduleinfo):
    scanid = onenodule[1]
    scanid = caseid_to_scanid(int(scanid))
    if scanid not in case_list:
        case_list.append(scanid)

print('number of cases: ', len(case_list))


for onecase in tqdm.tqdm(case_list[:3]):
    if not os.path.exists(imagedir + onecase):
        os.makedirs(imagedir + onecase)
    if not os.path.exists(maskdir + onecase):
        os.makedirs(maskdir + onecase)