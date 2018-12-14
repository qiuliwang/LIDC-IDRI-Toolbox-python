'''
Created by Wang Qiu Li
6/28/2018

modified from get_PatientId_SeriesUID.py

return a list that contains the relationship between patient id and scan UID
'''

import csvTools
import os

basedir = 'D:/Data/LIDC-IDRI/DOI/'

def getScan():
    metadatas = csvTools.readCSV('files/LIDC-IDRI_MetaData.csv')
    CTList = []
    Patient_Id = []
    Series_UID = []
    sign = 0
    for metadata in metadatas:
        if sign != 0:
            if metadata[4] == 'CT':
                ctdata = []
                ctdata.append(metadata[1])
                Patient_Id.append(metadata[1])
                ctdata.append(metadata[9])
                Series_UID.append(metadata[9])

                CTList.append(ctdata)
        sign += 1
    # csvTools.writeCSV('PatientId_SeriesUID.csv', CTList)

    patients = os.listdir(basedir)
    scan = []
    for patient in patients:
        idlist1 = os.listdir(basedir + patient)
        for level1 in idlist1:
            idlist2 = os.listdir(basedir + patient + '/' + level1)
            for level2 in idlist2:
                if level2 in Series_UID:
                    temp = patient + '/' + level1 + '/' + level2
                    scan.append(temp)
    return scan