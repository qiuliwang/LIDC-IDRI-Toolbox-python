'''
Created by WangQL
12/18/2017
'''

import os

# C:\Users\WangQL\Documents\GitCode\MedicWork\Code\data
dir = "/Users/wangql/Local/GitCode/PersonalWork/DicomWork/pics"
windir = "C:\\Users\\WangQL\\Documents\\GitCode\\MedicWork\\Code\\data"
windir2 = "C:\\Users\\WangQL\\Desktop\\DOI"
strhead = "C:\\Users\\WangQL\\Documents\\GitCode\\PersonalWork\\DicomWork\\Data\\SPIE-AAPM Lung CT Challenge JPG"
strhead2 = "C:\\Users\\WangQL\\Documents\\GitCode\\PersonalWork\\DicomWork\\Data\\DOI JPG"

def listdir(path, list_name):
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if(os.path.isdir(file_path)):
            listdir(file_path, list_name)
        else:
            list_name.append(file_path)
        return list_name

# list_name = []
# listdir(dir, list_name)
# print(list_name)

# get all .dcm pics
def file_name(file_dir):
    filelist = []
    for root, dirs, files in os.walk(file_dir):
        for names in files:
            # print(len(names))
            length = len(names)
            small = names[length-4:length]
            if small == ".dcm":
                # names = root + "/"+ names
                names = root + "/"+ names
                filelist.append(names)


    return filelist

# listname = file_name(windir)
# str =  "C:\\Users\\WangQL\\Desktop\\SPIE-AAPM Lung CT Challenge\\CT-Training-BE001\\1.2.840.113704.1.111.2112.1167842143.1\\1.2.840.113704.1.111.2112.1167842347.17/000088.dcm"
# str = str[51:len(str)]
# print(str)
# print(strhead + str)

# C:\Users\WangQL\Desktop\DOI\LUNGx-CT001\1.3.50463009827345485762745999238237348347135062081\1.3.563871217806014917027594443208961765673833569714/000081.dcm
def get_res_dir(listname):
    listjpg = []
    for tempname in listname:
        # SPIE-AAPM Lung CT Challenge
        # tempname = tempname[89:len(tempname)]
        # DOI
        tempname = tempname[65:len(tempname)]
        tempname = strhead2 + tempname
        tempname = tempname[0:len(tempname) - 4]
        tempname = tempname+".jpg"
        listjpg.append(tempname)

    return listjpg

def get_two_dirs(file_dir):
    filelist = file_name(file_dir)
    jpglist = get_res_dir(filelist)
    return filelist, jpglist

# filelist, jpglist = get_two_dirs(windir)
# print(filelist[0])
# print(len(filelist))
# print(jpglist[0])

# listjpg = get_res_dir(listname)

# i = 0
# for filetemp in listjpg:
#     i = i + 1
#     if i == 2:
#         break
#     print(filetemp)

# i = 0
# for filetemp in listname:
#     i = i + 1
#     if i == 2:
#         break
#     print(filetemp)
# print(len(listname))

