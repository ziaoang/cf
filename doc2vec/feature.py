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


sentences = []
for userId in userPool:
    userPool[userId].sort(key=lambda t:int(t[1]))
    words = []
    for t in userPool[userId]:
        words.append("v" + t[0])
    sentence = gensim.models.doc2vec.TaggedDocument(words=words, tags=["u" + userId])
    sentences.append(sentence)


model = gensim.models.Doc2Vec(sentences, size=50, window=10, min_count=1, workers=1, sample=1e-5, dm=1, seed=123456789)


userList = list(userSet)
itemList = list(itemSet)

userList.sort(key=lambda t:int(t))
itemList.sort(key=lambda t:int(t))

df = open(modelFile, "w")

for userId in userList:
    userVecId = "u" + userId
    vector = model.docvecs[userVecId]
    t = [str(v) for v in vector]
    df.write("%s %s\n"%(userVecId, " ".join(t)))

for itemId in itemList:
    itemVecId = "v" + itemId
    vector = model[itemVecId]
    t = [str(v) for v in vector]
    df.write("%s %s\n"%(itemVecId, " ".join(t)))

df.close()



