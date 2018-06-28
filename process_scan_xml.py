'''
Created by Wang Qiu Li
6/28/2018

process xml in scans
'''

basedir = 'D:/Data/LIDC-IDRI/DOI/'

import Func_get_PatientId_SeriesUID

listscan = Func_get_PatientId_SeriesUID.getScan()
# print(listscan[0])
# print(len(listscan))