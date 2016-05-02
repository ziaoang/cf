


userSet = set()
itemSet = set()

no = 0
for line in open("ml-20m/ratings.csv"):
    no += 1
    if no == 1:
        continue

    userIdStr, itemIdStr, ratingStr, timeStr = line.strip().split(",")

    userId = int(userIdStr)
    itemId = int(itemIdStr)
    rating = float(ratingStr)
    time   = int(timeStr)
    
    userSet.add(userId)
    itemSet.add(itemId)

userList = list(userSet)
itemList = list(itemSet)

userList.sort()
itemList.sort()

print("user id count: %d"%len(userList))
print("item id count: %d"%len(itemList))

print("min user id: %d"%userList[0])
print("max user id: %d"%userList[-1])

print("min item id: %d"%itemList[0])
print("max item id: %d"%itemList[-1])



