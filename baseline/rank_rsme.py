import sys
import math
from collections import defaultdict

userPool = defaultdict(int)

for line in open("../data/my/train-1m.1.txt"):
    userId, itemId, rating, time = line.strip().split(" ")
    userPool[userId] += 1

for line in open("../data/my/test-1m.1.txt"):
    userId, itemId, rating, time = line.strip().split(" ")
    userPool[userId] += 1

a = []
for userId in userPool:
    a.append([userId, userPool[userId]])

a.sort(key=lambda t:t[1])
size = len(a)

b = [set(), set(), set(), set(), set()]
for i in range(5):
    for j in range(size*i/5, size*(i+1)/5):
        b[i].add(a[j][0])

for rank in range(5):
    for cross in range(1, 6):
        testFile = "../data/my/test-1m.%d.txt"%cross
        result = []
        for line in open(testFile):
            userId, itemId, rating, time = line.strip().split(" ")
            result.append([userId, itemId, float(rating)])

        err = 0
        cnt = 0
        outFile  = "libfm/data/out-1m.%d.mcmc"%(cross)
        no = 0
        for line in open(outFile):
            no += 1
            if result[no-1][0] not in b[rank]:
                continue
            predict = float(line.strip())
            err += (predict - result[no-1][2]) ** 2
            cnt += 1
        err = math.sqrt(err/cnt)
        print("%.6f"%err)
        
        




