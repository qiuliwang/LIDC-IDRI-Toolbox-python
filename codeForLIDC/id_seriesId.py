
# coding: utf-8

# In[1]:


'''
Created by WangQL
4.9.2018

get nodules from CT use list3.2.csv
'''

import os
import pandas as pd


# # data_dir = 'stage1'
# # patients = os.listdir(data_dir)
labels_data1 = pd.read_csv('D:\Data\LIDC-IDRI\LIDC-IDRI_MetaData.csv',index_col = 0)
labels_data2 = pd.read_csv('D:\Data\LIDC-IDRI\LIDC-IDRI_MetaData.csv',index_col = 'Series UID')

print(labels_data1.columns)
print(labels_data2.columns)


# In[2]:


# get UID
patients_id = labels_data1.iloc[:,8]
arrs=patients_id.values  
print(type(arrs[0]))
print(arrs[:10])
print(len(arrs))


# In[3]:


# get CT UID
new_patients = []
new_patients_id = []

# get id which has CT info
for patient in arrs:
    #  label = labels_df.at[patient, 'cancer']
    temp_type = labels_data2.at[patient, 'Modality']
    if temp_type == 'CT':
        new_patients.append(patient)
        temp_id = labels_data2.at[patient, 'Patient Id']
        new_patients_id.append(temp_id)
        
print(new_patients[:10])
print(len(new_patients))
print(len(new_patients_id))


# In[4]:


# combine id with series
dictionary = {}
i = 0

while i < len(new_patients_id):
    id = new_patients_id[i]
    series = new_patients[i]
    if i < 10:
        print(id, series)
    dictionary[id] = series
    i += 1


# In[5]:


tumer_id = pd.read_csv('D:\Data\LIDC-IDRI\list3.2.csv',index_col = 0)
print(tumer_id.columns)


def NumToStr(num):
    strnum = str(num)
    if num < 10:
        strnum = "000" + strnum
    elif num < 100:
        strnum = "00" + strnum
    elif num < 1000:
        strnum = "0" + strnum
    return strnum

def NumToStr2(num):
    strnum = str(num)
    if num < 10:
        strnum = "00000" + strnum
    elif num < 100:
        strnum = "0000" + strnum
    elif num < 1000:
        strnum = "000" + strnum
    return strnum

import shutil


cases = tumer_id.iloc[:,0]
cases_x_loc = tumer_id.iloc[:,5]
cases_y_loc = tumer_id.iloc[:,6]
cases_slice_no = tumer_id.iloc[:,7]
print(len(cases))
print(len(cases_slice_no))
print(cases_slice_no[:5])
print(cases_x_loc[:5])
print(cases_y_loc[:5])


# In[12]:


import pydicom
import scipy.misc
import cv2
sign = 0

def cutTheImage(x, y, pix):
    temp = 50
    x1 = x - temp
    x2 = x + temp
    y1 = y - temp
    y2 = y + temp
    img_cut = pix[x1:x2, y1:y2]
    return img_cut

t = len(cases)
for (case, slice, x, y) in zip(cases, cases_slice_no,cases_x_loc,cases_y_loc):
    caseid = 'LIDC-IDRI-' + NumToStr(case)
    caseseries = dictionary[caseid]
    old_dir = 'D:\\Data\\LIDC-IDRI\\CT_DATA\\' + caseseries
    dicomlist = os.listdir(old_dir)
    # remove xml file
    for dic in dicomlist:
        typeoffile = dic[len(dic)-3:len(dic)]
        if typeoffile == 'xml':
            dicomlist.remove(dic)
    
    slices = [pydicom.dcmread(old_dir + '\\' + s) for s in dicomlist]

    slices.sort(key = lambda x : float(x.ImagePositionPatient[2]),reverse=True)

    slice_x = slices[slice - 1]
    pix = slice_x.pixel_array  # numpy.ndarray
    image_name = old_dir[0:18] + 'CT_IMAGE\\' + str(caseid) + '_' + str(slice)+'.jpeg'

    # cut out the nodule
    cut_img = cutTheImage(y, x, pix)
    scipy.misc.imsave(image_name, cut_img)
    print(sign / t)
    sign = sign + 1
    if sign == 10:
        print('break')
        break

