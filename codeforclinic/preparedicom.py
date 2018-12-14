#-*- coding: UTF-8 -*-

import pydicom
import cv2
import os

path = '/raid/data/clinic/clinic/benign1/'

patients = os.listdir(path)
print(len(patients))

print(patients[:1])

b80ffiles = []

seriesNumber = []
for patient in patients[:1]:
    files = os.listdir(path + patient)
    for onefile in files:
        ds = pydicom.dcmread(os.path.join(path, patient, onefile))
        #ConvolutionKernel
        if "ConvolutionKernel" in ds.dir():
                contant = ds.data_element("ConvolutionKernel")
                se = ds.data_element("SeriesNumber")
                if contant.value == 'B80f':
                        b80ffiles.append(onefile)
                        if not se in seriesNumber:
                                seriesNumber.append(se)

print(len(b80ffiles))
print(len(seriesNumber))