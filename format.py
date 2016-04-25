import sys


try:
	srcFile = sys.argv[1]
	dstFile = sys.argv[2]
except:
	print("srcFile dstFile")
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

df = open(dstFile, "w")
for line in open(srcFile):
	t = line.strip().split("::")
	
	userId = t[0]
	itemId = t[1]
	rating = t[2]

	userIndex = getIndex("u" + userId)
	itemIndex = getIndex("v" + itemId)

	df.write("%s %d:1 %d:1\n"%(rating, userIndex, itemIndex))
df.close()
