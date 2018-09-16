import pydicom
import cv2

ds = pydicom.dcmread('FILE1.dcm')
print(type(ds))
item1 = ds.data_element('SliceThickness')
item2 = ds.data_element('PixelSpacing')

print(item1.value)
print(item2.value)

ds = pydicom.dcmread('000001.dcm')
print(type(ds))
item1 = ds.data_element('SliceThickness')
item2 = ds.data_element('PixelSpacing')

print(item1.value)
print(item2.value)

# onepic = ds.pixel_array
# clahe = cv2.createCLAHE(clipLimit = 2.0, tileGridSize = (8,8))
# print(type(clahe))
# onepic = clahe.apply(onepic)