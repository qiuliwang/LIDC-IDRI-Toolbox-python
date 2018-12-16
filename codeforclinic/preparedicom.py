#-*- coding: UTF-8 -*-

import pydicom
import cv2
import os
import SeNDicom
import shutil

path = '../testdicom/'
pathdir = '../testdirdicom/'
# print(os.path.dirname(os.getcwd()))

patients = os.listdir(path)
print(len(patients))

print(patients[:1])

b80ffiles = []

seriesNumber = []
slicethickness = []
for patient in patients[:1]:
        files = os.listdir(path + patient)
        bestdicom = []
        dictfordicoms = {}
        
        for onefile in files:
                ds = pydicom.dcmread(os.path.join(path, patient, onefile))
                if "ConvolutionKernel" in ds.dir():
                        convKernel = ds.data_element("ConvolutionKernel").value
                        se = ds.data_element("SeriesNumber").value
                        thickness = ds.data_element("SliceThickness").value
                        if convKernel == 'B80f':
                                dictkeys = dictfordicoms.keys()
                                if not se in dictkeys:
                                        dictfordicoms[se] = 1
                                else:
                                        dictfordicoms[se] += 1
                        # print(onefile)

        for key in dictfordicoms.keys():
                print(key, dictfordicoms[key])

        # get max key value/se number
        key_name = max(dictfordicoms, key=dictfordicoms.get)
        print(key_name)

        '''
        os.makedirs(path) 
        shutil.copy(sourceDir,  targetDir)
            isExists=os.path.exists(path)

        '''
        os.makedirs(pathdir + patient)

        for onefile in files:
                ds = pydicom.dcmread(os.path.join(path, patient, onefile))
                if "ConvolutionKernel" in ds.dir():
                        se = ds.data_element("SeriesNumber").value
                        thickness = ds.data_element("SliceThickness").value
                        if se == key_name:
                                shutil.copy(os.path.join(path, patient, onefile), os.path.join(pathdir, patient, onefile))


        # for onefile in files:
        #         ds = pydicom.dcmread(os.path.join(path, patient, onefile))
        #         #ConvolutionKernel
        #         if "ConvolutionKernel" in ds.dir():
        #                 contant = ds.data_element("ConvolutionKernel")
        #                 se = ds.data_element("SeriesNumber")
        #                 thickness = ds.data_element("SliceThickness").value
        #                 if contant.value == 'B80f':
        #                         b80ffiles.append(onefile)
        #                         if not se in seriesNumber:
        #                                 seriesNumber.append(se)
        #                         if not thickness in slicethickness:
        #                                 slicethickness.append(thickness)

        # minithickness = 10
        # for temp in slicethickness:
        #         if temp < minithickness:
        #                 minithickness = temp
        # print(minithickness)

        # for onefile in files:
        #         ds = pydicom.dcmread(os.path.join(path, patient, onefile))       
        #         if "ConvolutionKernel" in ds.dir():
        #                 contant = ds.data_element("ConvolutionKernel")
        #                 se = ds.data_element("SeriesNumber")
        #                 thickness = ds.data_element("SliceThickness").value
        #                 if contant.value == 'B80f' and thickness == minithickness:
        #                         bestdicom.append(onefile)

        # print(len(bestdicom))



# print(len(b80ffiles))
# print(len(seriesNumber))

# for se in seriesNumber:
#         print(se.value)

