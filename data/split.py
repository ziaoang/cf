import sys
import random
from collections import defaultdict

random.seed(123456789)

try:
    ratingFile    = sys.argv[1]
    trainFile     = sys.argv[2]
    testFile      = sys.argv[3]
    confFile      = sys.argv[4]
    subTrainFile  = sys.argv[5]
    subTestFile   = sys.argv[6]
    subConfFile   = sys.argv[7]
    ratio         = float(sys.argv[8])
except:
    print("ratingFile trainFile testFile confFile subTrainFile subTestFile subConfFile ratio")
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
    elif "\t" in line:
        splitChar = "\t"
    else:
        print("Rating File Format Error")
        exit()

    userId, itemId, rating, time = line.strip().split(splitChar)

    userIdSet.add(userId)
    itemIdSet.add(itemId)
    recordList.append([userId, itemId, rating, time])

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


trainSum = 0
trainCount = 0
subTrainSum = 0
subTrainCount = 0

userCount = len(userIdList)
itemCount = len(itemIdList)
total = len(recordList)

random.shuffle(recordList)

trainDf = open(trainFile, "w")
testDf = open(testFile, "w")
subTrainDf = open(subTrainFile, "w")
subTestDf = open(subTestFile, "w")

for i in range(total):
    record = recordList[i]

    userId = record[0]
    itemId = record[1]
    rating = record[2]
    time   = record[3]

    userIndex = userIdToUserIndex[userId]
    itemIndex = itemIdToItemIndex[itemId]
   
    out = "%d %d %s %s\n"%(userIndex, itemIndex, rating, time)

    if i < total * ratio:
        trainSum += float(rating)
        trainCount += 1
        trainDf.write(out)
        if i < total * ratio * ratio:
            subTrainSum += float(rating)
            subTrainCount += 1
            subTrainDf.write(out)
        else:
            subTestDf.write(out)
    else:
        testDf.write(out)

trainDf.close()
testDf.close()
subTrainDf.close()
subTestDf.close()

confDf = open(confFile, "w")
confDf.write("base_score = %f\n"%(trainSum/trainCount))
confDf.write("num_global = 0\n")
confDf.write("num_user   = %d\n"%userCount)
confDf.write("num_item   = %d\n"%itemCount)
confDf.write("active_type = 0\n")
confDf.close()

subConfDf = open(subConfFile, "w")
subConfDf.write("base_score = %f\n"%(subTrainSum/subTrainCount))
subConfDf.write("num_global = 0\n")
subConfDf.write("num_user   = %d\n"%userCount)
subConfDf.write("num_item   = %d\n"%itemCount)
subConfDf.write("active_type = 0\n")
subConfDf.close()

