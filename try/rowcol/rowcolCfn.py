import sys

try:
        trainFile       = sys.argv[1]
        testFile        = sys.argv[2]
        dstTrainFile    = sys.argv[3]
        dstTestFile     = sys.argv[4]
except:
        print("trainFile testFile dstTrainFile dstTestFile")
        exit()

print("compute U")
U = {}
for line in open("../Autoencoders_cf/src/U.mid"):
	t = line.strip().split(" ")
	userId = int(t[0])
	fea = []
	for i in range(1, len(t)):
		fea.append("%d:%s"%(i, t[i]))
	U[userId] = " ".join(fea)

print("compute V")
V = {}
for line in open("../Autoencoders_cf/src/V.mid"):
	t = line.strip().split(" ")
	itemId = int(t[0])
	fea = []
	for i in range(1, len(t)):
		fea.append("%d:%s"%(i + 700, t[i]))
	V[itemId] = " ".join(fea)

print(len(U))
print(len(V))
	


print("generate dst train file")
trainDf = open(dstTrainFile, "w")
for line in open(trainFile):
	t = line.strip().split(" ")
	i = int(t[0])
	j = int(t[1])
	r = int(t[2])
	
	if i not in U:
		U[i] = ""
	if j not in V:
		V[j] = ""

	if U[i] == "" and V[j] == "":
		print("ERROR: no feature for user %d item %d in train"%(i, j))
		exit()
	if U[i] == "":
		trainDf.write("%d %s\n"%(r, V[j]))
	elif V[j] == "":
		trainDf.write("%d %s\n"%(r, U[i]))
	else:
		trainDf.write("%d %s %s\n"%(r, U[i], V[j]))
trainDf.close()

print("generate dst test file")
testDf = open(dstTestFile, "w")
for line in open(testFile):
	t = line.strip().split(" ")
	i = int(t[0])
	j = int(t[1])
	r = int(t[2])
	
	if i not in U:
		U[i] = ""
	if j not in V:
		V[j] = ""
	
	if U[i] == "" and V[j] == "":
		print("ERROR: no feature for user %d item %d in train"%(i, j))
		exit()
	if U[i] == "":
		testDf.write("%d %s\n"%(r, V[j]))
	elif V[j] == "":
		testDf.write("%d %s\n"%(r, U[i]))
	else:
		testDf.write("%d %s %s\n"%(r, U[i], V[j]))
testDf.close()


