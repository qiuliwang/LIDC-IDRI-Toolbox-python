'''
Created by Wang Qiu Li
7/2/2018

orignize info in nodule_chara_list.csv and list3.2.csv
and save as malignancy.csv
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

def getAve(numlist):
    ave = 0
    if len(numlist) != 4:
        print(numlist)
    for num in numlist:
        ave += int(num)
    if len(numlist) == 0:
        ave = 0
    else:
        ave = ave / len(numlist)
    return ave

nodule_chara = csvTools.readCSV(csvdir + 'nodule_chara_list.csv')

list3 = csvTools.readCSV(csvdir + 'list3.2.csv')
list3 = list3[1:len(list3)]
count = 0
sign = 0

list3_2 = []
for item in list3:
    id = item[0]
    case = item[1]
    case = caseid_to_scanid(int(case))

    ldlist = []
    for ids in item[10:14]:
        item.append(ids)
        if str(ids) != '':
            ldlist.append(str(ids))
        
    if len(ldlist) == 4:
        list3_2.append(item)

for item in list3_2:

    sign = 0

    id = item[0]
    case = item[1]
    print("=================")
    case = caseid_to_scanid(int(case))        
    print(case)


    ldlist = []
    for ids in item[10:14]:
        if str(ids) != '':
            print(ids)
            ldlist.append(ids)
    
    if len(ldlist) != 4:
        print('=====')
    
    # nodule_chara that contain case
    case_chara_id = []
    for cach in nodule_chara:
        if cach[0] == case:
            case_chara_id.append(cach)
    store_subtlety = []
    store_internalStructure = []
    store_calcification = []
    store_sphericity = []
    store_margin = []
    store_lobulation = []
    store_spiculation = []
    store_texture = []
    store_malignancy = []

    # for ld in ldlist:
    #     print(ld)
    print("===")
    for ld in ldlist:
        # print('nodule id ',ld)

        for one_case_chara in case_chara_id:
            # print(type(one_case_chara))
            if ld in one_case_chara[1]:
                print('find', one_case_chara[1], one_case_chara)
                store_subtlety.append(one_case_chara[2])
                store_internalStructure.append(one_case_chara[3])
                store_calcification.append(one_case_chara[4])
                store_sphericity.append(one_case_chara[5])
                store_margin.append(one_case_chara[6])
                store_lobulation.append(one_case_chara[7])
                store_spiculation.append(one_case_chara[8])
                store_texture.append(one_case_chara[9])
                store_malignancy.append(one_case_chara[10])
                # if one_case_chara[10] == '3':
                #     sign = 1
                break


    subtlety_ave = getAve(store_subtlety)
    internalStructure_ave = getAve(store_internalStructure)
    calcification_ave = getAve(store_calcification)
    sphericity_ave = getAve(store_sphericity)
    margin_ave = getAve(store_margin)
    lobulation_ave = getAve(store_lobulation)
    spiculation_ave = getAve(store_spiculation)
    texture_ave = getAve(store_texture)
    malignancy_ave = getAve(store_malignancy)

    item.append(subtlety_ave)
    item.append(internalStructure_ave)
    item.append(calcification_ave)
    item.append(sphericity_ave)
    item.append(margin_ave)
    item.append(lobulation_ave)
    item.append(spiculation_ave)
    item.append(texture_ave)
    item.append(malignancy_ave)
    if sign == 1:
        count += 1
    # csvTools.writeCSV('malignancy.csv', item)

# print('count ', count)
# print('len ', len(list3))
csvTools.writeCSV('malignancy.csv', list3_2)