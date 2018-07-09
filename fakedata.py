'''
Created by Wang Qiu Li

7/6/2018

general fake data for model testing

'''

import numpy as np
# x = np.zeros((30, 32, 32))
# print(x[0][0][0])

# y = np.ones((30, 32, 32))
# print(y[0][0][0])

for sign in range(0,1000):
    if sign % 2 == 0:
        name = str(sign) + '_fake.npy'
        x = np.zeros([30, 32, 32])
    else:
        name = str(sign) + '_real.npy'
        x = np.ones([30, 32, 32])
    np.save('D:/Data/LIDC-IDRI/NPY/' + name, x)