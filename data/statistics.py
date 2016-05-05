import sys

try:
    trainFile = sys.argv[1]
    testFile  = sys.argv[2]
except:
    print("trainFile testFile")
    exit()

ratingCnt = 0
userSet = set()
itemSet = set()

total = 0
cnt = 0
for line in open(trainFile):
    ratingCnt += 1
    userIdStr, itemIdStr, ratingStr, timeStr = line.strip().split(" ")
    userSet.add(userIdStr)
    itemSet.add(itemIdStr)
    total += float(ratingStr)
    cnt += 1

for line in open(testFile):
    ratingCnt += 1
    userIdStr, itemIdStr, ratingStr, timeStr = line.strip().split(" ")
    userSet.add(userIdStr)
    itemSet.add(itemIdStr)

userList = list(userSet)
itemList = list(itemSet)

userList.sort(key=lambda t:int(t))
itemList.sort(key=lambda t:int(t))

userCnt = len(userList)
itemCnt = len(itemList)
sparsity = 100*(1 - float(ratingCnt) / (userCnt * itemCnt))

print("user id count: %d"%userCnt)
print("item id count: %d"%itemCnt)
print("rating count: %d"%ratingCnt)
print("Sparsity: %.2f"%sparsity)

print("min user id: %s"%userList[0])
print("max user id: %s"%userList[-1])

print("min item id: %s"%itemList[0])
print("max item id: %s"%itemList[-1])

print("mean rating in train file: %.6f"%(total/cnt))

