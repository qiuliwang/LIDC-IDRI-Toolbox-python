'''
Created by Wang Qiu Li

7/4/2018

prepare data for malignancy model
'''

import os
import csvTools
from sklearn.model_selection import train_test_split
import numpy as np
import re

basedir = '/data0/LIDC/NNNPY/'

# 10477 - 10456

datas = os.listdir(basedir)
print(len(datas))

# errdatas = csvTools.readCSV('errfile.txt')
# print(len(errdatas))

# for errdata in errdatas:
#     dataname = errdata[0]
#     datapath = basedir + dataname
#     print(datapath)
#     os.remove(datapath)
# print('done!')

labels = csvTools.readCSV('malignancy.csv')
'''
id = 0
malignancy level = 29
'''

#basedir = '/data0/LIDC/NNPY/'
def get_train_and_test_filename(path,test_size,seed):
    filelist = os.listdir(path)
    return train_test_split(filelist, test_size=test_size, random_state=seed)

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
            arr = arr.transpose(2, 1, 0)
            batch_array.append(arr)
            # id = re.findall("\d+",onefile)[0]
            if 'high' in onefile:
                batch_label.append([0, 1])
            elif 'low' in onefile:
                batch_label.append([1, 0])
            else:
                print(onefile)
        except Exception as e:
            print("file not exists! %s"%npy)
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
            arr = arr.transpose(2, 1, 0)
            batch_array.append(arr)
            # id = re.findall("\d+",onefile)[0]
            if 'high' in onefile:
                batch_label.append([0, 1])
            elif 'low' in onefile:
                batch_label.append([1, 0])
            else:
                print(onefile)
        except Exception as e:
            print("file not exists! %s"%npy)
            batch_array.append(batch_array[-1]) 
    return np.array(batch_array), np.array(batch_label)

trainbatch, testbatch = get_train_and_test_filename(basedir, 0.1, 121)
print(len(trainbatch))
print(len(testbatch))
batch_filename = trainbatch[:32]
batch_array, batch_label = get_batch(batch_filename)
print(len(batch_array))
print(len(batch_label))