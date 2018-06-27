'''
Created by Wang Qiu Li
6/27/2018
'''

import csvTools

listnodules = csvTools.readCSV('csv_xls/list3.2.csv')
print(len(listnodules))
# 1 + 2635 = 2636
print(listnodules[0])

'''
['id', 'case', 'scan', 'roi', 'volume', 'eq. diam.', 'x loc.', 'y loc.', 'slice no.', '', 'nodIDs', '', '', '', '', '', '']
'''