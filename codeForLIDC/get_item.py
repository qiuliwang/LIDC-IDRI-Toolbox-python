#-*- coding: UTF-8 -*-

import pydicom
import cv2
import os

dir = 'testdicom/'

# filelist = os.listdir(dir)
# selist = []
# for onefile in filelist:
#     ds = pydicom.dcmread(dir + onefile)
#     direct = ds.dir()
#     if 'SeriesNumber' in direct:
#         if ds.data_element('SeriesNumber').value == 5:
#             print(ds.data_element('SliceThickness').value)
#         # if ds.data_element('SliceThickness').value not in selist:
#         #     selist.append(ds.data_element('SliceThickness').value)

# print(selist)

ds = pydicom.dcmread('000001.dcm')
for elem in ds.dir():
    if elem == 'SliceThickness':
        contant = ds.SliceThickness
        print(contant)
print('\n\n')




# onepic = ds.pixel_array
# clahe = cv2.createCLAHE(clipLimit = 2.0, tileGridSize = (8,8))
# print(type(clahe))
# onepic = clahe.apply(onepic)