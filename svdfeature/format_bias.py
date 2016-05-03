import sys
from collections import defaultdict

try:
    trainFile       = sys.argv[1]
    testFile        = sys.argv[2]
    dstTrainFile    = sys.argv[3]
    dstTestFile     = sys.argv[4]
except:
    print("trainFile testFile dstTrainFile dstTestFile")
    exit()

def mean(t):
    total = 0.0
    cnt = 0
    for v in t:
        total += v
        cnt += 1
    return total / cnt

userSet = set()
itemSet = set()

globalRatingList = []
userRatingList = defaultdict(list)
itemRatingList = defaultdict(list)

for line in open(trainFile):
    t = line.strip().split(" ")
    
    userId = t[0]
    itemId = t[1]
    rating = float(t[2])
    
    userSet.add(userId)
    itemSet.add(itemId)
    
    globalRatingList.append(rating)
    userRatingList[userId].append(rating)
    itemRatingList[itemId].append(rating)

for line in open(testFile):
    t = line.strip().split(" ")
    
    userId = t[0]
    itemId = t[1]
    
    userSet.add(userId)
    itemSet.add(itemId)
    
globalBias = mean(globalRatingList)
userBias = {}
for userId in userRatingList:
    userBias[userId] = mean(userRatingList[userId])
itemBias = {}
for itemId in itemRatingList:
    itemBias[itemId] = mean(itemRatingList[itemId])

user_num = len(userSet)
item_num = len(itemSet)

df = open(dstTrainFile, "w")
for line in open(trainFile):
    t = line.strip().split(" ")
    userId = t[0]
    itemId = t[1]
    rating = t[2]
    userMean = userBias[userId]
    itemMean = itemBias[itemId]
    df.write("%s 1 2 2 0:%f %s:1 %d:%f %s:1 %d:%f\n"%(rating, globalBias, userId, user_num, userMean, itemId, item_num, itemMean))
df.close()

df = open(dstTestFile, "w")
for line in open(testFile):
    t = line.strip().split(" ")
    userId = t[0]
    itemId = t[1]
    rating = t[2]

    if userId in userBias and itemId in itemBias:
        userMean = userBias[userId]
        itemMean = itemBias[itemId]
        df.write("%s 1 2 2 0:%f %s:1 %d:%f %s:1 %d:%f\n"%(rating, globalBias, userId, user_num, userMean, itemId, item_num, itemMean))
    elif userId not in userBias and itemId in itemBias:
        itemMean = itemBias[itemId]
        df.write("%s 1 1 2 0:%f %s:1 %s:1 %d:%f\n"%(rating, globalBias, userId, itemId, item_num, itemMean))
    elif userId in userBias and itemId not in itemBias:
        userMean = userBias[userId]
        df.write("%s 1 2 1 0:%f %s:1 %d:%f %s:1\n"%(rating, globalBias, userId, user_num, userMean, itemId))
    else:
        df.write("%s 1 1 1 0:%f %s:1 %s:1\n"%(rating, globalBias, userId, itemId))
df.close()

