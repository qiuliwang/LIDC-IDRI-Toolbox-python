'''
Created by Wang Qiu Li
6/27/2018
'''

import csvTools

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
temp = []
sign = 0
for metadata in metadatas:
    if sign != 0:
        # print(len(metadata))
        # print(metadata[4])
        if metadata[4] == 'CT':
            ctdata = []
            ctdata.append(metadata[1])
            ctdata.append(metadata[9])
            CTList.append(ctdata)
    sign += 1

print(len(CTList))

# csvTools.writeCSV('PatientId_SeriesUID.csv', CTList)

