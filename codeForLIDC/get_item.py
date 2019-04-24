#-*- coding: UTF-8 -*-
'''
Created by WangQL
2019/4/24

'''
import pydicom
import cv2
import os

dir = 'testdicom/'

# get SliceThickness of one dcm file
ds = pydicom.dcmread('000001.dcm')
for elem in ds.dir():
    if elem == 'SliceThickness':
        contant = ds.SliceThickness
        print(contant)
print('\n\n')

