'''
Created by Wang Qiu Li
7/3/2018

divide the nodules into two groups
level 1 and 2 are classified into LMNs
level 4 and 5 are classified into HMHs
level 3 are excluded

'''

import csvTools

nodules = csvTools.readCSV('files/malignancy.csv')

# print(nodules[2][29])
# index 29 is malignancy level

lmns = []
hmns = []
mid = []

for nodule in nodules:
    level = float(nodule[29])
    if level >= 3.5:
        hmns.append(nodule)
    elif level < 2.5 :
        lmns.append(nodule)
    else:
        mid.append(nodule)

'''
in paper
lmns = 880
hmns = 495
midd = 1243

we get
867
480
1288


'''

print(len(lmns))
print(len(hmns))
print(len(mid))