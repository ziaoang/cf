
userIdPool = set()
itemIdPool = set()

for line in open("my/train.txt"):
    t = line.strip().split(" ")
    userId = t[0]
    itemId = t[1]
    rating = t[2]

    userIdPool.add(userId)
    itemIdPool.add(itemId)

print("%d unqiue userId"%len(userIdPool))
print("%d unqiue itemId"%len(itemIdPool))




