import sys


try:
	ratingFile   = sys.argv[1]
	trainFile    = sys.argv[2]
	testFile     = sys.argv[3]
	newTrainFile = sys.argv[4]
	newTestFile  = sys.argv[5]
except:
	print("ratingFile trainFile testFile newTrainFile newTestFile")
	exit()


pool = {}
index = 0
def getIndex(id):
	global pool
	global index
	if id not in pool:
		pool[id] = index
		index += 1
	return pool[id]

no = 0
for line in open(ratingFile):
    no += 1
    if no == 1 and ".csv" in ratingFile:
        continue
    
    splitChar = None
    if "::" in line:
        splitChar = "::"
    elif "," in line:
        splitChar = "," 
    else:
        print("Rating File Format Error")
        exit()

    userIdStr, itemIdStr, ratingStr, timeStr = line.strip().split(splitChar)

    userIndex = getIndex("u" + userIdStr)
    itemIndex = getIndex("v" + itemIdStr)


df = open(newTrainFile, "w")
for line in open(trainFile):
	userIdStr, itemIdStr, ratingStr, timeStr = line.strip().split(" ")
	userIndex = getIndex("u" + userIdStr)
	itemIndex = getIndex("v" + itemIdStr)
	df.write("%s %d:1 %d:1\n"%(ratingStr, userIndex, itemIndex))
df.close()

df = open(newTestFile, "w")
for line in open(testFile):
	userIdStr, itemIdStr, ratingStr, timeStr = line.strip().split(" ")
	userIndex = getIndex("u" + userIdStr)
	itemIndex = getIndex("v" + itemIdStr)
	df.write("%s %d:1 %d:1\n"%(ratingStr, userIndex, itemIndex))
df.close()
