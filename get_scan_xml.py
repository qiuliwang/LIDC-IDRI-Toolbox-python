'''
Created by Wang Qiu Li
6/28/2018

get xml in scans
'''

import os
import csvTools
try: 
  import xml.etree.cElementTree as ET 
except ImportError: 
  import xml.etree.ElementTree as ET 
import sys,os

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

# restore nodule characteristics
noudle_chara_list = []

for scan in listscan:
    scanid = scan[10:14]
    scanid = int(scanid)
    # print(scanid)

    # nodulelist = []
    # for metadata in metadatas:
        # print(type(scanid))
        # print(type(metadata[1]))
        # if int(metadata[1]) == scanid:
        #     print(metadata[10], metadata[11], metadata[12], metadata[13])
        #     nodulelist.append(metadata[10])
        #     nodulelist.append(metadata[11])
        #     nodulelist.append(metadata[12])
        #     nodulelist.append(metadata[13])
        #     break

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
    # if len(xmlfile) > 1:
    #     print(scan)

    '''
    LIDC-IDRI-0127/1.3.6.1.4.1.14519.5.2.1.6279.6001.195975724868929317649402600442/1.3.6.1.4.1.14519.5.2.1.6279.6001.229343399861261429237689489892
    LIDC-IDRI-0777/1.3.6.1.4.1.14519.5.2.1.6279.6001.226719444846209417020566423366/1.3.6.1.4.1.14519.5.2.1.6279.6001.192256506776434538421891524301
    LIDC-IDRI-1009/1.3.6.1.4.1.14519.5.2.1.6279.6001.849069697860879761549990488101/1.3.6.1.4.1.14519.5.2.1.6279.6001.855232435861303786204450738044
    LIDC-IDRI-1010/1.3.6.1.4.1.14519.5.2.1.6279.6001.145373944605191222309393681361/1.3.6.1.4.1.14519.5.2.1.6279.6001.550599855064600241623943717588
    LIDC-IDRI-1011/1.3.6.1.4.1.14519.5.2.1.6279.6001.287560874054243719452635194040/1.3.6.1.4.1.14519.5.2.1.6279.6001.272123398257168239653655006815

    these cases have more than one xml files
    but these xml files seem to be the same

    '''

    # we have xml files and dicom files in one scan

    xmlfile = xmlfile[0]
    xmlfile = scan+'/'+xmlfile
    # print(xmlfile)
    '''
    LIDC-IDRI-0001/1.3.6.1.4.1.14519.5.2.1.6279.6001.298806137288633453246975630178/1.3.6.1.4.1.14519.5.2.1.6279.6001.179049373636438705059720603192/069.xml
    LIDC-IDRI-0002/1.3.6.1.4.1.14519.5.2.1.6279.6001.490157381160200744295382098329/1.3.6.1.4.1.14519.5.2.1.6279.6001.619372068417051974713149104919/071.xml
    LIDC-IDRI-0003/1.3.6.1.4.1.14519.5.2.1.6279.6001.101370605276577556143013894866/1.3.6.1.4.1.14519.5.2.1.6279.6001.170706757615202213033480003264/072.xml
    LIDC-IDRI-0004/1.3.6.1.4.1.14519.5.2.1.6279.6001.191425307197546732281885591780/1.3.6.1.4.1.14519.5.2.1.6279.6001.323541312620128092852212458228/074.xml
    LIDC-IDRI-0005/1.3.6.1.4.1.14519.5.2.1.6279.6001.190188259083742759886805142125/1.3.6.1.4.1.14519.5.2.1.6279.6001.129007566048223160327836686225/076.xml

    '''

    '''
    readingSession
        annotationVersion
        servicingRadiologistID
        unblindedReadNodule
            noduleID
            characteristics
            <subtlety>5</subtlety>
            <internalStructure>1</internalStructure>
            <calcification>6</calcification>
            <sphericity>4</sphericity>
            <margin>4</margin>
            <lobulation>5</lobulation>
            <spiculation>5</spiculation>
            <texture>5</texture>
            <malignancy>5</malignancy>
    '''
    tree = ET.parse(basedir + xmlfile) 
    root = tree.getroot() 


    for child in root:
        # print('child')
        # print(child.tag[20:len(child.tag)])
        if 'readingSession' in child.tag:
            for leave in child:
                if 'unblindedReadNodule' in leave.tag:
                    for dot in leave:
                        if 'characteristics' in dot.tag:
                            temp_for_nodule = []
                            for dottemp in leave:
                                if 'noduleID' in dottemp.tag:
                                    # print(dottemp.text)
                                    temp_for_nodule.append(scan[:14])
                                    temp_for_nodule.append(dottemp.text)
                                if 'characteristics' in dottemp.tag:
                                    # print('=====')
                                    for chara in dottemp:
                                        # print(chara.text)
                                        temp_for_nodule.append(chara.text)
                            noudle_chara_list.append(temp_for_nodule)

print(len(noudle_chara_list)) 
csvTools.writeCSV('nodule_chara_list.csv', noudle_chara_list)
# for caset in noudle_chara_list:
#     print(len(caset))
#     print(caset)    

        # childname = child.tag[20:len(child.tag)]