import sys
import gensim
from collections import defaultdict


try:
    trainFile = sys.argv[1]
    modelFile = sys.argv[2]
except:
    print("trainFile modelFile")
    exit()


userSet = set()
itemSet = set()
userPool = defaultdict(list)

for line in open(trainFile):
    userId, itemId, rating, time = line.strip().split(" ")
    userSet.add(userId)
    itemSet.add(itemId)
    userPool[userId].append([itemId, time])


userItemList = {}
sentences = []
for userId in userPool:
    userPool[userId].sort(key=lambda t:int(t[1]))
    words = []
    for t in userPool[userId]:
        words.append("v" + t[0])
    sentences.append(words)
    userItemList["u" + userId] = words


dimension = 50
model = gensim.models.Word2Vec(sentences, size=dimension, window=5, min_count=1, workers=6)


userList = list(userSet)
itemList = list(itemSet)

userList.sort(key=lambda t:int(t))
itemList.sort(key=lambda t:int(t))

df = open(modelFile, "w")

for userId in userList:
    userVecId = "u" + userId
    userVector = [0] * dimension
    itemList = userItemList[userVecId]
    for itemVecId in itemList:
        vector = model[itemVecId]
        for i in range(dimension):
            userVector[i] += vector[i]
    t = [str(v/len(itemList)) for v in userVector]
    df.write("%s %s\n"%(userVecId, " ".join(t)))

for itemId in itemList:
    itemVecId = "v" + itemId
    vector = model[itemVecId]
    t = [str(v) for v in vector]
    df.write("%s %s\n"%(itemVecId, " ".join(t)))

df.close()



