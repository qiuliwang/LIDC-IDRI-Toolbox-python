#-*- coding: UTF-8 -*-

'''
Created by WangQL
2019.4.25

aims to select the series suitable for deep learning.

get 'B80f', 'I70f', 'B70f', 'B80', 'B70s' from original CT scans and copy them to another dir
'''
import pydicom
import cv2
import os
import shutil
import tqdm

path = '/home/wangqiuli/Data/pneumonia/chest3/'
pathdir = '/home/wangqiuli/Data/pneumonia/SecondNormal/'

patients = os.listdir(path)
print("number of patitents: ", len(patients))

b80ffiles = []

seriesNumber = []
kernellist = []

# slicethickness = ['B80f', 'I70f', 'B70f', 'B80', 'B70s']

record = open('failedCasesNormal.txt', 'w')
for patient in tqdm.tqdm(patients):
        files = os.listdir(path + patient)
        bestdicom = []
        dictfordicoms = {}
        for onefile in (files):
                ds = pydicom.dcmread(os.path.join(path, patient, onefile))
                if ("ConvolutionKernel" in ds.dir()) and ('SeriesDescription' in ds.dir()):
                        convKernel = ds.data_element("ConvolutionKernel").value
                        se = ds.data_element("SeriesNumber").value
                        thickness = ds.data_element("SliceThickness").value
                        SPO = ds.data_element('SeriesDescription').value
                        if ('SPO' not in SPO) and ('MPR' not in SPO):
                                if convKernel == 'B80f':  
                                        dictkeys = dictfordicoms.keys()
                                        if not se in dictkeys:
                                                dictfordicoms[se] = 1
                                        else:
                                                dictfordicoms[se] += 1
                                if convKernel == 'I70f':  
                                        dictkeys = dictfordicoms.keys()
                                        if not se in dictkeys:
                                                dictfordicoms[se] = 1
                                        else:
                                                dictfordicoms[se] += 1                        
                                if convKernel == 'B70f':  
                                        dictkeys = dictfordicoms.keys()
                                        if not se in dictkeys:
                                                dictfordicoms[se] = 1
                                        else:
                                                dictfordicoms[se] += 1
                                if convKernel == 'B80':  
                                        dictkeys = dictfordicoms.keys()
                                        if not se in dictkeys:
                                                dictfordicoms[se] = 1
                                        else:
                                                dictfordicoms[se] += 1
                                if convKernel == 'B70s':  
                                        dictkeys = dictfordicoms.keys()
                                        if not se in dictkeys:
                                                dictfordicoms[se] = 1
                                        else:
                                                dictfordicoms[se] += 1
                                if convKernel == 'B31f':  
                                        dictkeys = dictfordicoms.keys()
                                        if not se in dictkeys:
                                                dictfordicoms[se] = 1
                                        else:
                                                dictfordicoms[se] += 1
                                if convKernel[0] == 'I31f':  
                                        dictkeys = dictfordicoms.keys()
                                        if not se in dictkeys:
                                                dictfordicoms[se] = 1
                                        else:
                                                dictfordicoms[se] += 1    

        if (len(dictfordicoms.keys()) > 0):
                key_name = max(dictfordicoms, key=dictfordicoms.get)
                '''
                os.makedirs(path) 
                shutil.copy(sourceDir,  targetDir)
                isExists=os.path.exists(path)
                '''
		if not os.path.exists(pathdir + patient):
                	os.makedirs(pathdir + patient)
		
                	for onefile in files:
                        	ds = pydicom.dcmread(os.path.join(path, patient, onefile))
                        	if "ConvolutionKernel" in ds.dir():
                                	se = ds.data_element("SeriesNumber").value
                                	thickness = ds.data_element("SliceThickness").value
                               		if se == key_name:
                                        	shutil.copy(os.path.join(path, patient, onefile), os.path.join(pathdir, patient, onefile))

        else:
                record.write(patient + '\n')

record.close()
