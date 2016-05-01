import random

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

data = []
for line in open(ratingFile):
	t = line.strip().split("::")
	userId = t[0]
	itemId = t[1]
	rating = t[2]
	time   = t[3]
	userIndex = userIdToUserIndex[userId]
	itemIndex = itemIdToItemIndex[itemId]
	data.append([userIndex, itemIndex, rating, time])
print(len(data))

trainDf = open("my/train.txt", "w")
testDf = open("my/test.txt", "w")
random.seed(123456789)
for t in data:
	if random.random() < 0.8:
		trainDf.write("%d %d %s %s\n"%(t[0], t[1], t[2], t[3]))
	else:
		testDf.write("%d %d %s %s\n"%(t[0], t[1], t[2], t[3]))
trainDf.close()
testDf.close()



