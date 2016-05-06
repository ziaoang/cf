import sys

try:
    trainFile = sys.argv[1]
    testFile = sys.argv[2]
    newTestFile = sys.argv[3]
except:
    print("trainFile testFile newTestFile")
    exit()

userSet = set()
itemSet = set()

for line in open(trainFile):
    t = line.strip().split(" ")
    userId = t[0]
    itemId = t[1]
    userSet.add(userId)
    itemSet.add(itemId)

df = open(newTestFile, "w")
for line in open(testFile):
    t = line.strip().split(" ")
    userId = t[0]
    itemId = t[1]
    if userId in userSet and itemId in itemSet:
        df.write(line)
df.close()

