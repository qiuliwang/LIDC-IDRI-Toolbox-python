#-*- coding: UTF-8 -*-

import pydicom
import cv2
import os

class SeNDicom(object):
    # class for dicom files with the same SeriesNumber
    def __init__():
        self.dicomfiles = []
        self.SliceThickness = 0
    
    def addDicomFile(dicomfile):
        if countDicomFiles == 0:
            self.dicomfiles.append(dicomfile)
            self.SliceThickness = dicomfile.data_element("SliceThickness").value

        else:
            if self.SliceThickness == dicomfile.data_element("SliceThickness").value:
                self.dicomfiles.append(dicomfile)

    def countDicomFiles():
        return len(self.dicomfiles)