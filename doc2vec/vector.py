
import gensim
from collections import defaultdict

trainFile = "../data/my/train.txt"

userPool = defaultdict(list)

for line in open(trainFile):
    t = line.strip().split(" ")
    userId = t[0]
    itemId = t[1]
    rating = t[2]
    time   = t[3]
    userPool[userId].append([itemId, time])
 
sentences = []
for userId in userPool:
    userPool[userId].sort(key=lambda t:int(t[1]))
    words = []
    for t in userPool[userId]:
        words.append("v" + t[0])
    sentence = gensim.models.doc2vec.TaggedDocument(words=words, tags=["u" + userId])
    sentences.append(sentence)

model = gensim.models.Doc2Vec(sentences, size=100, window=8, min_count=0, workers=4, dm=1)

df = open("doc2vec.model", "w")
for i in range(6040):
    userVecId = "u%d"%(i+1)
    if userVecId in model.docvecs:
        vector = model.docvecs[userVecId]
        t = [str(v) for v in vector]
        df.write("%s %s\n"%(userVecId, " ".join(t)))

for i in range(3883):
    itemVecId = "v%d"%(i+1)
    if itemVecId in model:
        vector = model[itemVecId]
        t = [str(v) for v in vector]
        df.write("%s %s\n"%(itemVecId, " ".join(t)))
df.close()



