
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
    sentence = gensim.models.doc2vec.LabeledSentence(words=words, labels=["u" + userId])
    sentences.append(sentence)


model = gensim.models.Doc2Vec(sentences, size=100, window=8, min_count=0, workers=4)
model.save_word2vec_format("doc2vec.model", binary=False)



