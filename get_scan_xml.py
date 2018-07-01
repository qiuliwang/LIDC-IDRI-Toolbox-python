'''
Created by Wang Qiu Li
6/28/2018

process xml in scans
'''

import os
import csvTools

basedir = 'D:/Data/LIDC-IDRI/DOI/'
csvdir= 'files/list3.2.csv'

import Func_get_PatientId_SeriesUID

listscan = Func_get_PatientId_SeriesUID.getScan()
# print(listscan[0])
# print(len(listscan))
'''
LIDC-IDRI-0001/1.3.6.1.4.1.14519.5.2.1.6279.6001.298806137288633453246975630178/1.3.6.1.4.1.14519.5.2.1.6279.6001.179049373636438705059720603192
1018

'''

metadatas = csvTools.readCSV(csvdir)
# print(len(metadatas))
'''
['id', 'case', 'scan', 'roi', 'volume', 'eq. diam.', 'x loc.', 'y loc.', 'slice no.', '', 'nodIDs', '', '', '', '', '', '']
'''
metadatas = metadatas[1:len(metadatas)]
# ==print(metadatas[0])
# print(metadatas[len(metadatas) - 1])
'''
['1', '1', '3000566', '1', '6459.75', '23.107', '317', '367', '43', '', 'IL057_127364', 'Nodule 001', 'MI014_12127', '0', '', '', '']
['2635', '1012', '32231', '1', '122.2', '6.157', '145', '153', '105', '', '0', '201255', '157143', 'Nodule 001', '', '', '']
'''

for scan in listscan[:3]:
    scanid = scan[10:14]
    scanid = int(scanid)
    # print(scanid)

    nodulelist = []
    for metadata in metadatas:
        # print(type(scanid))
        # print(type(metadata[1]))
        if int(metadata[1]) == scanid:
            print(metadata[10], metadata[11], metadata[12], metadata[13])
            nodulelist.append(metadata[10])
            nodulelist.append(metadata[11])
            nodulelist.append(metadata[12])
            nodulelist.append(metadata[13])
            break

    dicomfile = []
    xmlfile = []
    scandir = basedir + scan
    filelist = os.listdir(scandir)
    for filename in filelist:
        if '.xml' in filename:
            xmlfile.append(filename)
        if '.dcm' in filename:
            dicomfile.append(filename)
    # print(len(dicomfile))
    # print(len(xmlfile))

    # we have xml files and dicom files in one scan
