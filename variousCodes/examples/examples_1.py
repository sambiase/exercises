import numpy as np

strArr = ["[5, 2, 3]", "[2, 2, 3, 10, 6]"]
resArr = []
listResInt = []
listSumRes = []
aux = 0
res = 0

# remove spaces and brackets
for i in range(0, len(strArr)):
    resArr.append(strArr[i].replace(']', '').replace('[', '').replace(' ', '').split(','))

# map to Int
for i in range(0, len(resArr)):
    listResInt.append(list(map(int, resArr[i])))



