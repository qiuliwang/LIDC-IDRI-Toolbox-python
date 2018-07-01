'''
Created by Wang Qiu Li
6/27/2018
'''

import csvTools
import os

basedir = 'D:/Data/LIDC-IDRI/DOI/'

metadatas = csvTools.readCSV('csv_xls/LIDC-IDRI_MetaData.csv')
print(len(metadatas))
# print(metadatas[0])

'''
10 column
['Collection', 'Patient Id', 'Study Date', 
 'Study Description', 'Modality', 'Series Description',
 'Manufacturer', 'Manufacturer Model', 'Software Version', 'Series UID']
'''

'''
LIDC-IDRI-0132
LIDC-IDRI-0151
LIDC-IDRI-0315
LIDC-IDRI-0332
LIDC-IDRI-0355
LIDC-IDRI-0365
LIDC-IDRI-0442
LIDC-IDRI-0484
has two CT scans

1012 + 6 = 1018
'''
CTList = []
Patient_Id = []
Series_UID = []
sign = 0
for metadata in metadatas:
    if sign != 0:
        # print(len(metadata))
        # print(metadata[4])
        if metadata[4] == 'CT':
            ctdata = []
            ctdata.append(metadata[1])
            Patient_Id.append(metadata[1])
            ctdata.append(metadata[9])
            Series_UID.append(metadata[9])

            CTList.append(ctdata)
    sign += 1

print(len(CTList))
print(len(Patient_Id))
print(len(Series_UID))
# csvTools.writeCSV('PatientId_SeriesUID.csv', CTList)

patients = os.listdir(basedir)
scan = []
for patient in patients:
    idlist1 = os.listdir(basedir + patient)
    for level1 in idlist1:
        idlist2 = os.listdir(basedir + patient + '/' + level1)
        for level2 in idlist2:
            if level2 in Series_UID:
                temp = patient + '/' + level1 + '/' + level2 + '\n'
                scan.append(temp)

print(scan[:10])
# file_object = open('id_scan.txt', 'w')
# file_object.writelines(scan)
# file_object.close( )

