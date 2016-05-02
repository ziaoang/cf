import random
from collections import defaultdict

ratingFile = "ml-20m/ratings.csv"


userIdSet = set()
itemIdSet = set()

no = 0
for line in open(ratingFile):
    no += 1
    if no == 1:
        continue

    userIdStr, itemIdStr, ratingStr, timeStr = line.strip().split(",")

    userId = int(userIdStr)
    itemId = int(itemIdStr)
    rating = float(ratingStr)
    time   = int(timeStr)

    userIdSet.add(userId)
    itemIdSet.add(itemId)

userIdList = list(userIdSet)
itemIdList = list(itemIdSet)

userIdList.sort()
itemIdList.sort()

userIdToUserIndex = {}
itemIdToItemIndex = {}

for i in range(len(userIdList)):
    userIdToUserIndex[userIdList[i]] = i + 1

for i in range(len(itemIdList)):
    itemIdToItemIndex[itemIdList[i]] = i + 1


data = defaultdict(list)

no = 0
for line in open(ratingFile):
    no += 1
    if no == 1:
        continue

    userIdStr, itemIdStr, ratingStr, timeStr = line.strip().split(",")

    userId = int(userIdStr)
    itemId = int(itemIdStr)
    rating = float(ratingStr)
    time   = int(timeStr)

    userIndex = userIdToUserIndex[userId]
    itemIndex = itemIdToItemIndex[itemId]
    
    data[userIndex].append([userIndex, itemIndex, ratingStr, time])


trainDf = open("my/train.txt", "w")
testDf  = open("my/test.txt", "w")
for userIndex in data:
    t = data[userIndex]
    length = len(t)
    if length < 10:
        continue
    t.sort(key=lambda t:t[3])
    for i in range(length):
        if i < length * 9 / 10:
            trainDf.write("%d %d %s %d\n"%(t[i][0], t[i][1], t[i][2], t[i][3]))
        else:
            testDf.write("%d %d %s %d\n"%(t[i][0], t[i][1], t[i][2], t[i][3]))
trainDf.close()
testDf.close()

