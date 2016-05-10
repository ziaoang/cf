import sys
import random
from collections import defaultdict

random.seed(123456789)

try:
    ratingFile = sys.argv[1]
    trainFile  = sys.argv[2]
    testFile   = sys.argv[3]
    ratio      = float(sys.argv[4])
    k_times    = int(sys.argv[5])
except:
    print("ratingFile trainFile testFile ratio k_times")
    exit()

# load rating record
userIdSet = set()
itemIdSet = set()
recordList = []

no = 0
for line in open(ratingFile):
    no += 1
    if no == 1 and ".csv" in ratingFile:
        continue
    
    splitChar = None
    if "::" in line:
        splitChar = "::"
    elif "," in line:
        splitChar = ","
    else:
        print("Rating File Format Error")
        exit()

    userIdStr, itemIdStr, ratingStr, timeStr = line.strip().split(splitChar)

    userIdSet.add(userIdStr)
    itemIdSet.add(itemIdStr)
    recordList.append([userIdStr, itemIdStr, ratingStr, timeStr])

print("%d users"%len(userIdSet))
print("%d items"%len(itemIdSet))

# turn id to index
userIdList = list(userIdSet)
itemIdList = list(itemIdSet)

userIdList.sort(key=lambda t:int(t))
itemIdList.sort(key=lambda t:int(t))

userIdToUserIndex = {}
itemIdToItemIndex = {}

for i in range(len(userIdList)):
    userIdToUserIndex[userIdList[i]] = i

for i in range(len(itemIdList)):
    itemIdToItemIndex[itemIdList[i]] = i

# generate training set and test set for k times
for i in range(k_times):
    print("%d cross"%(i+1))
    
    random.shuffle(recordList)

    trainDf = open(trainFile+".%d.txt"%(i+1), "w")
    testDf  = open(testFile+".%d.txt"%(i+1), "w")
    for record in recordList:
        userId = record[0]
        itemId = record[1]
        rating = record[2]
        time   = record[3]

        userIndex = userIdToUserIndex[userId]
        itemIndex = itemIdToItemIndex[itemId]

        if random.random() < ratio:
            trainDf.write("%d %d %s %s\n"%(userIndex, itemIndex, rating, time))
        else:
            testDf.write("%d %d %s %s\n"%(userIndex, itemIndex, rating, time))
    trainDf.close()
    testDf.close()

