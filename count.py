import csvTools
import os
import pandas as pd
import pydicom
import scipy.misc
import cv2
import numpy as np

basedir = '/data0/LIDC/DOI/'
resdir = '303010/'

noduleinfo = csvTools.readCSV('files/malignancy.csv')
idscaninfo = csvTools.readCSV('files/id_scan.txt')

print(len(noduleinfo))