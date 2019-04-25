#-*- coding: UTF-8 -*-

'''
Created by WangQL
2019.4.25
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
        # print('================')
        print(patient)
        for onefile in (files):
                ds = pydicom.dcmread(os.path.join(path, patient, onefile))
                if ("ConvolutionKernel" in ds.dir()) and ('SeriesDescription' in ds.dir()):
                        convKernel = ds.data_element("ConvolutionKernel").value
                        se = ds.data_element("SeriesNumber").value
                        thickness = ds.data_element("SliceThickness").value
                        SPO = ds.data_element('SeriesDescription').value
                        if ('SPO' not in SPO) and ('MPR' not in SPO):
                                if convKernel == 'B80f': #or 'I70f':# or 'B70f' or 'B80':
                                        # print(convKernel)
                                        dictkeys = dictfordicoms.keys()
                                        if not se in dictkeys:
                                                dictfordicoms[se] = 1
                                        else:
                                                dictfordicoms[se] += 1
                                if convKernel == 'I70f': #or 'I70f':# or 'B70f' or 'B80':
                                        # print(convKernel)
                                        dictkeys = dictfordicoms.keys()
                                        if not se in dictkeys:
                                                dictfordicoms[se] = 1
                                        else:
                                                dictfordicoms[se] += 1                        
                                if convKernel == 'B70f': #or 'I70f':# or 'B70f' or 'B80':
                                        # print(convKernel)
                                        dictkeys = dictfordicoms.keys()
                                        if not se in dictkeys:
                                                dictfordicoms[se] = 1
                                        else:
                                                dictfordicoms[se] += 1
                                if convKernel == 'B80': #or 'I70f':# or 'B70f' or 'B80':
                                        # print(convKernel)
                                        dictkeys = dictfordicoms.keys()
                                        if not se in dictkeys:
                                                dictfordicoms[se] = 1
                                        else:
                                                dictfordicoms[se] += 1
                                if convKernel == 'B70s': #or 'I70f':# or 'B70f' or 'B80':
                                        # print(convKernel)
                                        dictkeys = dictfordicoms.keys()
                                        if not se in dictkeys:
                                                dictfordicoms[se] = 1
                                        else:
                                                dictfordicoms[se] += 1
                                if convKernel == 'B31f': #or 'I70f':# or 'B70f' or 'B80':
                                        # print(convKernel)
                                        dictkeys = dictfordicoms.keys()
                                        if not se in dictkeys:
                                                dictfordicoms[se] = 1
                                        else:
                                                dictfordicoms[se] += 1
                                if convKernel[0] == 'I31f': #or 'I70f':# or 'B70f' or 'B80':
                                        # print(convKernel)
                                        dictkeys = dictfordicoms.keys()
                                        if not se in dictkeys:
                                                dictfordicoms[se] = 1
                                        else:
                                                dictfordicoms[se] += 1    



                # print(dictfordicoms.keys())

        if (len(dictfordicoms.keys()) > 0):
                key_name = max(dictfordicoms, key=dictfordicoms.get)
                # print(key_name)
                # print(dictfordicoms[key_name])
        # print('xxxxx')
        # print(patient)
        # print(key_name)
        # print(dictfordicoms[key_name])
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
