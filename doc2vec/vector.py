import gensim
from collections import defaultdict

trainFile = "../data/my/train.txt"

# load data
userIdSet = set()
itemIdSet = set()
userPool = defaultdict(list)

for line in open(trainFile):
    userId, itemId, rating, time  = line.strip().split(" ")
    userIdSet.add(userId)
    itemIdSet.add(itemId)
    userPool[userId].append([itemId, time])

# generate sentences
sentences = []
for userId in userPool:
    userPool[userId].sort(key=lambda t:int(t[1]))
    words = []
    for t in userPool[userId]:
        words.append("v" + t[0])
    sentence = gensim.models.doc2vec.TaggedDocument(words=words, tags=["u" + userId])
    sentences.append(sentence)

# train doc2vec
model = gensim.models.Doc2Vec(sentences, size=50, window=10, min_count=1, workers=6, sample=1e-5, dm=1)

# save model
df = open("model/doc2vec.model", "w")

for userId in userIdSet:
    userVecId = "u" + userId
    vector = model.docvecs[userVecId]
    t = [str(v) for v in vector]
    df.write("%s %s\n"%(userVecId, " ".join(t)))

for itemId in itemIdSet:    
    itemVecId = "v" + itemId
    vector = model[itemVecId]
    t = [str(v) for v in vector]
    df.write("%s %s\n"%(itemVecId, " ".join(t)))

df.close()



