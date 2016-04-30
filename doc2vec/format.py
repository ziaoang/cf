import sys

modelFile = "doc2vec.model"

feature = {}
for line in open(modelFile):
    t = line.strip().split(" ")
    fea = []
    for i in range(1, len(t)):
        fea.append("%d:%s"%(i-1, t[i]))
    feature[t[0]] = " ".join(fea)

trainFile = "../data/my/train.txt"
testFile = "../data/my/test.txt"
targetTrainFile = "train.doc2vec"
targetTestFile = "test.doc2vec"

def format(srcFile, dstFile):
    df = open(dstFile, "w")
    for line in open(srcFile):
        t = line.strip().split(" ")
        userId = "u" + t[0]
        itemId = "v" + t[1]
        rating = t[2]
        time   = t[3]

        userFea = None
        if userId in feature:
            userFea = feature[userId]

        itemFea = None
        if itemId in feature:
            itemFea = feature[itemId]

        if userFea == None and itemFea == None:
            print("ERROR: %s %s"%(userId, itemId))
            exit()
        elif userFea != None and itemFea == None:
            df.write("%s 0 %d %d %s\n"%(rating, userFea.count(" ")+1 , 0, userFea))
        elif userFea == None and itemFea != None:
            df.write("%s 0 %d %d %s\n"%(rating, 0, itemFea.count(" ")+1 , itemFea))
        else:
            df.write("%s 0 %d %d %s %s\n"%(rating, userFea.count(" ")+1, itemFea.count(" ")+1, userFea, itemFea))
    df.close()


format(trainFile, targetTrainFile)
format(testFile, targetTestFile)

