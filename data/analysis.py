import sys
from collections import defaultdict

try:
    trainFile = sys.argv[1]
except:
    print("trainFile")
    exit()

userItemList = defaultdict(list)
for line in open(trainFile):
    userId, itemId, rating, time = line.strip().split(" ")
    userItemList[userId].append(itemId)

lengthCntDict = defaultdict(int)
for userId in userItemList:
    length = len(userItemList[userId])
    lengthCntDict[length] += 1

pool = []
for length in lengthCntDict:
    pool.append([length, lengthCntDict[length]])

pool.sort(key=lambda t:t[0])

for t in pool:
    print("%d\t%d"%(t[0], t[1]))
