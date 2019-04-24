'''
Created by Wang Qiu Li

7/4/2018

prepare data for malignancy model
get nodules according to malignancy level, and save as npy files
'''

import os
import csvTools
from sklearn.model_selection import train_test_split
import numpy as np
import re

basedir = 'D:Data/LIDC-IDRI/NPY/'

# 10477 - 10456

datas = os.listdir(basedir)

labels = csvTools.readCSV('files/malignancy.csv')

'''
index of id = 0
index of malignancy level = 29
'''

def get_train_and_test_filename(path,test_size,seed):
    '''
    return train data and test data
    '''
    filelist = os.listdir(path)
    return train_test_split(filelist, test_size=test_size, random_state=seed)

def get_high_data(path):
    '''
    return lmn or hmn data for testing
    '''
    filelist = os.listdir(path)
    returnlist = []
    for onefile in filelist:
        if 'low' in onefile:
            returnlist.append(onefile)
    return returnlist

def get_batch_withlabels(batch_filename):
    '''
    get batch
    return data, spiculation level and label
    '''
    batch_array = []
    batch_label = []

    for onefile in batch_filename[:2]:
        try:
            # print(onefile)
            index = onefile[:onefile.find('_')]
            # print(index)

            sphercity = []
            margin = []
            lobulation =[]
            spiculation = []

            chara_list = []
            for onenodule in labels:
                if onenodule[0] == index:
                    print(onenodule[24],onenodule[25],onenodule[26],onenodule[27])
                    sphercity.append(onenodule[24])
                    margin.append(onenodule[25])
                    lobulation.append(onenodule[26])
                    spiculation.append(onenodule[27])
                    continue

            print(onefile)
            arr = np.load(basedir + onefile)
            batch_array.append(arr)

            if 'high' in onefile:
                batch_label.append([0, 1])
            elif 'low' in onefile:
                batch_label.append([1, 0])
            else:
                print(onefile)
        except Exception as e:
            print("file not exists! %s"%onefile)
            batch_array.append(batch_array[-1]) 
    return np.array(batch_array), np.array(sphercity), np.array(margin), np.array(lobulation), np.array(spiculation), np.array(batch_label)


def get_batch(batch_filename):
    '''
    get batch
    return data and label
    '''
    batch_array = []
    batch_label = []

    for onefile in batch_filename:
        try:
            arr = np.load(basedir + onefile)
            batch_array.append(arr)
            # id = re.findall("\d+",onefile)[0]
            if 'high' in onefile:
                batch_label.append([0, 1])
            elif 'low' in onefile:
                batch_label.append([1, 0])
            else:
                print(onefile)
        except Exception as e:
            print("file not exists! %s"%onefile)
            batch_array.append(batch_array[-1]) 
    return np.array(batch_array), np.array(batch_label)

def get_test_batch(test_filesname):
    '''
    get test batch
    return data and label
    '''
    batch_array = []
    batch_label = []

    for onefile in batch_filename:
        try:
            arr = np.load(basedir + onefile)
            batch_array.append(arr)
            # id = re.findall("\d+",onefile)[0]
            if 'real' in onefile:
                batch_label.append([0, 1])
            elif 'fake' in onefile:
                batch_label.append([1, 0])
            else:
                print(onefile)
        except Exception as e:
            print("file not exists! %s"%onefile)
            batch_array.append(batch_array[-1]) 
    return np.array(batch_array), np.array(batch_label)
