import csvTools

labels = csvTools.readCSV('files/malignancy.csv')

index = 26
countlob1 = []
countlob2 = []
countlob3 = []
countlob4 = []
countlob5 = []

for one in labels:
    sign = round(float(one[27]))
    if sign == 1:
        countlob1.append(one)
    elif sign == 2:
        countlob2.append(one)
    elif sign == 3:
        countlob3.append(one)
    elif sign == 4:
        countlob4.append(one)
    elif sign == 5:
        countlob5.append(one)

countmal1 = 0
countmal2 = 0
countmal3 = 0
countmal4 = 0
countmal5 = 0

print(len(countlob5))
for one in labels:
    sign = round(float(one[29]))
    if round(float(one[26])) == 5:
        if sign == 1:
            countmal1 += 1
        elif sign == 2:
            countmal2 += 1
        elif sign == 3:
            countmal3 += 1
        elif sign == 4:
            countmal4 += 1
        elif sign == 5:
            countmal5 += 1
print(countmal1, countmal2, countmal3, countmal4, countmal5)

'''
lob
1430
(225, 431, 677, 93, 4)

783
(40, 131, 423, 170, 19)

292
(11, 20, 102, 99, 60)

92
(3, 9, 29, 25, 26)

35
(4, 9, 14, 3, 5)



spi
1644
(225, 431, 677, 93, 4)

648
(40, 131, 423, 170, 19)

194
(11, 20, 102, 99, 60)

101
(3, 9, 29, 25, 26)

45
(4, 9, 14, 3, 5)

'''