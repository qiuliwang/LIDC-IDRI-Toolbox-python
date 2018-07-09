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

basedir = 'D:Data/LIDC-IDRI/NPY/'

# 10477 - 10456

datas = os.listdir(basedir)
# print(len(datas))

# errdatas = csvTools.readCSV('errfile.txt')
# print(len(errdatas))

# for errdata in errdatas:
#     dataname = errdata[0]
#     datapath = basedir + dataname
#     print(datapath)
#     os.remove(datapath)
# print('done!')

labels = csvTools.readCSV('files/malignancy.csv')
'''
id = 0
malignancy level = 29
'''

#basedir = '/data0/LIDC/NNPY/'
def get_train_and_test_filename(path,test_size,seed):
    filelist = os.listdir(path)
    return train_test_split(filelist, test_size=test_size, random_state=seed)

def get_high_data(path):
    filelist = os.listdir(path)
    returnlist = []
    for onefile in filelist:
        if 'low' in onefile:
            returnlist.append(onefile)
    return returnlist

def get_batch_withlabels(batch_filename):
    '''
    get batch
    return data and label
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
                    #tempnodule.append(onenodule)
                    # chara_list.append(onenodule[21])
                    # chara_list.append(onenodule[22])
                    # chara_list.append(onenodule[23])
                    print(onenodule[24],onenodule[25],onenodule[26],onenodule[27])
                    sphercity.append(onenodule[24])
                    margin.append(onenodule[25])
                    lobulation.append(onenodule[26])
                    spiculation.append(onenodule[27])

                    # chara_list.append(onenodule[28])
                    continue
            print(onefile)
            # print(chara_list)

            # print(len(chara_list))
            # print(onenodule)
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

trainbatch, testbatch = get_train_and_test_filename(basedir, 0.1, 121)
# print(len(trainbatch))
# print(len(testbatch))
batch_filename = trainbatch[:32]
batch_array, sphercity, margin, lobulation, spiculation, batch_label = get_batch_withlabels(batch_filename)
print(len(batch_array))
print(len(sphercity))
print(len(margin))
print(len(lobulation))
print(len(spiculation))

print(len(batch_label))