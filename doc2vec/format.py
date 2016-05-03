import sys


try:
    targetTrainFile = sys.argv[1]
    targetTestFile  = sys.argv[2]
    modelFile       = sys.argv[3]
except:
    print("targetTrainFile targetTestFile modelFile(None)")
    exit()


trainFile       = "../data/my/train.txt"
testFile        = "../data/my/test.txt"


feature = {}
try:
    for line in open(modelFile):
        t = line.strip().split(" ")
        feature[t[0]] = t[1:]
except:
    print("no model file")


def format(srcFile, dstFile):
    df = open(dstFile, "w")
    for line in open(srcFile):
        t = line.strip().split(" ")
        userId = "u" + t[0]
        itemId = "v" + t[1]
        rating = t[2]
        time   = t[3]

        userFea = "%d:1"%(int(t[0])-1)
        if userId in feature:
            for i in range(50):
                userFea += " %d:%s"%(6040+i, feature[userId][i])

        itemFea = "%d:1"%(int(t[1])-1)
        if itemId in feature:
            for i in range(50):
                itemFea += " %d:%s"%(3883+i, feature[itemId][i])

        df.write("%s 0 %d %d %s %s\n"%(rating, userFea.count(" ")+1, itemFea.count(" ")+1, userFea, itemFea))
    df.close()

format(trainFile, targetTrainFile)
format(testFile,  targetTestFile)

