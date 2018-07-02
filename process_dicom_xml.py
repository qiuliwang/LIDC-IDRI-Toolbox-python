'''
Created by Wang Qiu Li
6/29/2018

process xml and dicom in scans
'''
try: 
  import xml.etree.cElementTree as ET 
except ImportError: 
  import xml.etree.ElementTree as ET 
import sys,os

class process(object):

    def __init__(self, dicomfiles, xmlfiles):
        self.dicomfiles = dicomfiles
        self.xmlfiles = xmlfiles

    def process_xml(self):
        