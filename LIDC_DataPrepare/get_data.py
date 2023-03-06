'''
Created by Wang Qiu Li
7/3/2021

Based on get_dicom_info

Get nodules with multiple annotations

'''

import csvTools
import os
import pandas as pd
import pydicom
import cv2
import numpy as np
import glob
import imageio

import xmlopt

basedir = '/Users/wangql/Local/Data/LIDC/DOI/'
# three_dir = 'three_channel/'
imagedir = 'mid_image_hu/'
npydir = 'npy_hu/'

noduleinfo = csvTools.readCSV('files/malignancy.csv')
idscaninfo = csvTools.readCSV('files/id_scan.txt')

def get_pixels_hu(ds):
    image = ds.pixel_array
    image = np.array(image , dtype = np.float32)
    intercept = ds.RescaleIntercept
    slope = ds.RescaleSlope
    image = image * slope
    image += intercept
    return image

def getThreeChannel(pixhu):
    # adjust the HU ranges according to your own condition.
    lungwindow = truncate_hu(pixhu, 800, -1000)
    highattenuation = truncate_hu(pixhu, 240, -160)
    lowattenuation = truncate_hu(pixhu, -950, -1400)
    pngfile = [lungwindow, highattenuation, lowattenuation]
    pngfile = np.array(pngfile).transpose(1,2,0)
    return  pngfile  

def truncate_hu(image_array, max, min):
    image = image_array.copy()
    image[image > max] = max
    image[image < min] = min
    image = normalazation(image)
    return image
    
# LUNA2016 data prepare ,second step: normalzation the HU
def normalazation(image_array):
    max = image_array.max()
    min = image_array.min()
    image_array = (image_array-min)/(max-min)  # float cannot apply the compute,or array error will occur
    avg = image_array.mean()
    image_array = image_array-avg
    return image_array   # a bug here, a array must be returned,directly appling function did't work


def cutTheImage(x, y, pix):
    temp = 25
    x1 = x - temp
    x2 = x + temp
    y1 = y - temp
    y2 = y + temp
    img_cut = pix[x1:x2, y1:y2]
    return img_cut

def caseid_to_scanid(caseid):
    returnstr = ''
    if caseid < 10:
        returnstr = '000' + str(caseid)
    elif caseid < 100:
        returnstr = '00' + str(caseid)
    elif caseid < 1000:
        returnstr = '0' + str(caseid)
    else:
        returnstr = str(caseid)
    return 'LIDC-IDRI-' + returnstr

def reverse(inputarray):
    shape = inputarray.shape
    nparray = np.ones(shape)
    for i in range(shape[0]):
        for j in range(shape[1]):
            if inputarray[i][j] == 0:
                nparray[i][j] = 1
            else:
                nparray[i][j] = 0
    return nparray

def red_mask(image_list):
    if len(image_list) == 1:
        return image_list[0]
    else:
        temp = np.zeros((512,512))
        for i in range(len(image_list)):
            temp += image_list[i]
        temp[temp > 0.5] = 1.0
        return temp

def blue_mask(image_list):
    if len(image_list) == 1:
        return image_list[0]
    else:
        temp = np.zeros((512,512))
        for i in range(len(image_list)):
            temp += image_list[i]
        temp[temp < len(image_list)] = 0.0
        return temp

def dif_mask(image_list):
    if len(image_list) == 1:
        return np.zeros((512,512))
    else:
        temp = np.zeros((512,512))
        for i in range(len(image_list)):
            temp += image_list[i]
        temp[temp == len(image_list)] = 0.0
        temp[temp > 0] = 1.0

        return temp

f = open('errlist.txt', 'w')
count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0

errorcount = 0

tempsign = 0

import tqdm

for onenodule in tqdm.tqdm(noduleinfo):
    xml = ''
    try:
        scanid = onenodule[1]
        scanid = caseid_to_scanid(int(scanid))
        noduleid = onenodule[3]
        scan_list_id = onenodule[2]
        # if scanid != 'LIDC-IDRI-0195':
        #     continue

        # if int(noduleid) != 2:
        #     continue
        scanpaths = []
        for idscan in idscaninfo:
            if scanid in idscan[0]:
                scanpaths.append(idscan[0])

        noduleld_list = []
        for i in range(10, 14):
            if str(onenodule[i]).strip() != '':
                noduleld_list.append(onenodule[i])

        for scanpath in scanpaths:
            # try:   
            if len(noduleld_list) > 1:
                # print('id list: ', noduleld_list)

                filelist1 = os.listdir(basedir + scanpath)
                filelist2 = []

                xmlfiles = []
                for onefile in filelist1:
                    if '.dcm' in onefile:
                        filelist2.append(onefile)
                    elif '.xml' in onefile:
                        xmlfiles.append(onefile)

                xmlfile = basedir + scanpath + '/' + xmlfiles[0]
                xml = xmlfile
                slices = [pydicom.dcmread(basedir + scanpath + '/' + s) for s in filelist2]

                slices.sort(key = lambda x : float(x.ImagePositionPatient[2]),reverse=True)
                x_loc = int(onenodule[6])
                y_loc = int(onenodule[7])
                z_loc = int(onenodule[8])
                ds = slices[z_loc - 1]

                masks = []

                if (str(ds.SeriesNumber) == onenodule[2]) or (str(onenodule[2]) == str(0)):
                    slice_location = ds.ImagePositionPatient[2]
                    # print('slice location: ', slice_location)
                    # print('noduleld_list: ', len(noduleld_list))
                    for one_nodule in noduleld_list:
                        
                        mask_image, signtemp = xmlopt.getEdgeMap(xmlfile, slice_location, [one_nodule])
                        masks.append(mask_image)

                    red = red_mask(masks)
                    blue = blue_mask(masks)
                    dif = dif_mask(masks)

                    ori_hu = get_pixels_hu(ds)
                    pix = ori_hu #getThreeChannel(ori_hu)
                    
                    if (x_loc < 25 or x_loc > (512 - 25)) or (y_loc < 25 or y_loc > (512 - 25)):
                        print('out of size:', scanid, noduleid)
                    else:
                        if np.max(red) > 0 and np.max(dif) > 0 and np.max(blue):
                            cut_img = cutTheImage(y_loc, x_loc, pix)
                            cut_red = cutTheImage(y_loc, x_loc, red)
                            cut_blue = cutTheImage(y_loc, x_loc, blue)
                            cut_dif = cutTheImage(y_loc, x_loc, dif)

                            imageio.imsave(imagedir + str(scanid) + '_' + str(noduleid) + '_' + str(scan_list_id) + '.png', cut_img)
                            imageio.imsave(imagedir + str(scanid) + '_' + str(noduleid) + '_' + str(scan_list_id) + '_union.png', cut_red)
                            imageio.imsave(imagedir + str(scanid) + '_' + str(noduleid) + '_' + str(scan_list_id) + '_intersection.png', cut_blue)
                            imageio.imsave(imagedir + str(scanid) + '_' + str(noduleid) + '_' + str(scan_list_id) + '_dif.png', cut_dif)

                            np.save(npydir + str(scanid) + '_' + str(noduleid) + '_' + str(scan_list_id) + '.npy', cut_img)
                            np.save(npydir + str(scanid) + '_' + str(noduleid) + '_' + str(scan_list_id) + '_union.npy', cut_red)
                            np.save(npydir+ str(scanid) + '_' + str(noduleid) + '_' + str(scan_list_id) + '_intersection.npy', cut_blue)
                            np.save(npydir + str(scanid) + '_' + str(noduleid) + '_' + str(scan_list_id) + '_dif.npy', cut_dif)

                        # for i in range(len(masks)):
                        #     mask_image = masks[i]                   
                        #     cut_mask = cutTheImage(y_loc, x_loc, mask_image)
                        #     scipy.misc.imsave(imagedir + str(scanid) + '_' + str(noduleid) + '_' + str(scan_list_id) + '_'  + str(i)+ '_mask.png', cut_mask)
                else:
                    print(scanid)
                    print('not equal')
    except:
        print(scanid)           
        print('Error')