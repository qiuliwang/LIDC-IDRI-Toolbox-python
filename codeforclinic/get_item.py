#-*- coding: UTF-8 -*-

import pydicom
import cv2
import os
import scipy.misc
import numpy as np 


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
def get_pixels_hu(pixel):
    image = pixel.pixel_array
    # Convert to int16 (from sometimes int16),
    # should be possible as values should always be low enough (<32k)
    image = image.astype(np.int16)
    # Set outside-of-scan pixels to 0
    # The intercept is usually -1024, so air is approximately 0
    image[image == -2000] = 0
    # Convert to Hounsfield units (HU)
    intercept = pixel.RescaleIntercept
    slope = pixel.RescaleSlope
    print(slope)
    if slope == 1:
        image = slope * image.astype(np.float64)
        image = image.astype(np.int16)
        image += np.int16(intercept)
    return np.array(image, dtype=np.int16)

ds1 = pydicom.dcmread('000071.dcm')
pixel1 = get_pixels_hu(ds1)
scipy.misc.imsave('outfile1.jpg', pixel1)
pixel2 = ds1.pixel_array
scipy.misc.imsave('outfile2.jpg', pixel2)

# ds2 = pydicom.dcmread('FILE318.dcm')
# pixel2 = get_pixels_hu(ds2)
# scipy.misc.imsave('outfile2.jpg', pixel2)



# for elem in ds.dir():
#     if elem == 'SliceThickness':
#         contant = ds.SliceThickness
#         print(contant)
# print('\n\n')




# onepic = ds.pixel_array
# clahe = cv2.createCLAHE(clipLimit = 2.0, tileGridSize = (8,8))
# print(type(clahe))
# onepic = clahe.apply(onepic)