import pydicom
import scipy.misc

sliceone = pydicom.dcmread('000001.dcm')

#print(sliceone)
pixarray = sliceone.pixel_array
scipy.misc.imsave('000001.jpeg', pixarray)
