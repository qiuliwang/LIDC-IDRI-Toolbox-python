'''
Created by Wang Qiu Li
7/2/2018

orignize info in nodule_chara_list.csv and list3.2.csv
'''

import os
import csvTools

basedir = 'D:/Data/LIDC-IDRI/DOI/'
csvdir= 'files/'


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


nodule_chara = csvTools.readCSV(csvdir + 'nodule_chara_list.csv')
# print(len(nodule_chara))

list3 = csvTools.readCSV(csvdir + 'list3.2.csv')
list3 = list3[1:len(list3)]
# print(len(list3))

# LIDC-IDRI-0001,Nodule 001,5,1,6,3,3,3,4,5,5
# 1,1,3000566,1,6459.75,23.107,317,367,43,,IL057_127364,Nodule 001,MI014_12127,0,,,

for item in list3:
    id = item[0]
    print('=====')
    print(id)
    case = item[1]
    case = caseid_to_scanid(int(case))
    print(case)

    ldlist = []
    for ids in item[10:14]:
        item.append(ids)
        # print(ids)
        if ids != '':
            ldlist.append(ids)

    # nodule_chara that contain case
    case_chara_id = []
    for cach in nodule_chara:
        if cach[0] == case:
            case_chara_id.append(cach)

    
    
    store_malignancy = []

    for ld in ldlist:
        print('nodule id ',ld)

        for one_case_chara in case_chara_id:
            if ld in one_case_chara:
                print(one_case_chara)
                store_malignancy.append(one_case_chara[10])
    print(len(store_malignancy))
    ave = 0
    for num in store_malignancy:
        ave += int(num)
    if len(store_malignancy) == 0:
        ave = 0
    else:
        ave = ave / len(store_malignancy)
    print(ave)
    item.append(ave)
    print(len(item))
# csvTools.writeCSV('malignancy.csv', list3)