import random
from collections import defaultdict

userFile   = "ml-1m/users.dat"
itemFile   = "ml-1m/movies.dat"
ratingFile = "ml-1m/ratings.dat"


userIdToUserIndex = {}
userIndex = 0
for line in open(userFile):
	userIndex += 1
	t = line.strip().split("::")
	userId = t[0]
	userIdToUserIndex[userId] = userIndex
print(userIndex)

itemIdToItemIndex = {}
itemIndex = 0
for line in open(itemFile):
	itemIndex += 1
	t = line.strip().split("::")
	itemId = t[0]
	itemIdToItemIndex[itemId] = itemIndex
print(itemIndex)

data = defaultdict(list)
for line in open(ratingFile):
	t = line.strip().split("::")
	userId = t[0]
	itemId = t[1]
	rating = int(t[2])
	time   = int(t[3])
	userIndex = userIdToUserIndex[userId]
	itemIndex = itemIdToItemIndex[itemId]
	data[userIndex].append([userIndex, itemIndex, rating, time])


trainDf = open("my/train.txt", "w")
testDf = open("my/test.txt", "w")
for userIndex in data:
    t = data[userIndex]
    if len(t) < 10:
        continue
    t.sort(key=lambda t:t[3])
    length = len(t)
    for i in range(length):
        if i < length * 9 / 10:
            trainDf.write("%d %d %d %d\n"%(t[i][0], t[i][1], t[i][2], t[i][3]))
        else:
            testDf.write("%d %d %d %d\n"%(t[i][0], t[i][1], t[i][2], t[i][3]))
trainDf.close()
testDf.close()

