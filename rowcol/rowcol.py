import sys


try:
	n 		= int(sys.argv[1])
	m 		= int(sys.argv[2])
	trainFile 	= sys.argv[3]
	testFile 	= sys.argv[4]
	dstTrainFile 	= sys.argv[5]
	dstTestFile 	= sys.argv[6]
	removeBias 	= True if sys.argv[7] == "1" else False
except:
	print("n m trainFile testFile dstTrainFile dstTestFile removeBias(0|1)")
	exit()


MATRIX = [[0]*(m+1) for i in range(n+1)]


print("load trian file")
for line in open(trainFile):
	t = line.strip().split(" ")
	i = int(t[0])
	j = int(t[1])
	r = int(t[2])
	MATRIX[i][j] = r


print("compute U")
U = {}
for i in range(1, n+1):
	bias = 0
	if removeBias:
		total = 0
		cnt = 0
		for j in range(1, m+1):
			r = MATRIX[i][j]
			if r > 0:
				total += r
				cnt += 1
		if cnt > 0:
			bias = float(total) / cnt
	t = []
	for j in range(1, m+1):
		r = MATRIX[i][j]
		if r > 0:
			if bias == 0:
				t.append("%d:%d"%(j, r))
			else:
				t.append("%d:%f"%(j, r-bias))
	U[i] = " ".join(t)


print("compute V")
V = {}
for j in range(1, m+1):
	bias = 0
	if removeBias:
		total = 0
		cnt = 0
		for i in range(1, n+1):
			r = MATRIX[i][j]
			if r > 0:
				total += r
				cnt += 1
		if cnt > 0:
			bias = float(total) / cnt
	t = []
	for i in range(1, n+1):
		r = MATRIX[i][j]
		if r > 0:
			if bias == 0:
				t.append("%d:%d"%(m+i, r))
			else:
				t.append("%d:%f"%(m+i, r-bias))
	V[j] = " ".join(t)


print("generate dst train file")
trainDf = open(dstTrainFile, "w")
for line in open(trainFile):
	t = line.strip().split(" ")
	i = int(t[0])
	j = int(t[1])
	r = int(t[2])
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

