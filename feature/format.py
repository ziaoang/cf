import sys


try:
    trainFile = sys.argv[1]
    testFile = sys.argv[2]
    featureFile = sys.argv[3]
    targetTrainFile = sys.argv[4]
    targettestFile = sys.argv[5]
except:
    print("trainFile testFile featureFile targetTrainFile targettestFile")
    exit()


featureDict = {}
for line in open(featureFile):
    t = line.strip().split(" ")
    featureDict[t[0]] = t[1:]


userSet = set()
itemSet = set()
for line in open(trainFile):
    userId, itemId, rating, time = line.strip().split(" ")
    userSet.add(userId)
    itemSet.add(itemId)
for line in open(testFile):
    userId, itemId, rating, time = line.strip().split(" ")
    userSet.add(userId)
    itemSet.add(itemId)
userNum = len(userSet)
itemNum = len(itemSet)


def add(srcFile, dstFile):
    global featureDict
    global userNum
    global itemNum

    df = open(dstFile, "w")
    for line in open(srcFile):
        userId, itemId, rating, time = line.strip().split(" ")

        userFea = "%s:1"%userId
        userVecId = "u" + userId
        if userVecId in featureDict:
            fea = featureDict[userVecId]
            for i in range(len(fea)):
                userFea += " %d:%s"%(userNum+i, fea[i])
        
        itemFea = "%s:1"%itemId
        itemVecId = "v" + itemId
        if itemVecId in featureDict:
            fea = featureDict[itemVecId]
            for i in range(len(fea)):
                itemFea += " %d:%s"%(itemNum+i, fea[i])

        df.write("%s 0 %d %d %s %s\n"%(rating, userFea.count(" ")+1, itemFea.count(" ")+1, userFea, itemFea))
    df.close()


add(trainFile, targetTrainFile)
add(testFile, targettestFile)



