trainFile = "train.txt"
testFile = "test.txt"

n = 6040
m = 3883

mat = []
for i in range(n+1):
	t = []
	for j in range(m+1):
		t.append(0)
	mat.append(t)

for line in open(trainFile):
	t = line.strip().split(" ")
	i = int(t[0])
	j = int(t[1])
	r = int(t[2])
	mat[i][j] = r

u = {}
for i in range(1, n+1):
	t = []
	for j in range(1, m+1):
		r = mat[i][j]
		if r > 0:
			t.append("%d:%d"%(j, r))
	u[i] = t

v = {}
for i in range(1, m+1):
	t = []
	for j in range(1, n+1):
		r = mat[j][i]
		if r > 0:
			t.append("%d:%d"%(m+j, r))
	v[i] = t

print(len(u))
print(len(v))

trainDf = open("train.rc2", "w")
for line in open(trainFile):
	t = line.strip().split(" ")
	i = int(t[0])
	j = int(t[1])
	r = int(t[2])

	totalFea = u[i] + v[j]

	if len(totalFea) > 0:
		trainDf.write("%d %s\n"%(r, " ".join(totalFea)))
	else:
		print("ERROR: no feature for user %d item %d in train"%(i+1, j +1))
		exit()
trainDf.close()

testDf = open("test.rc2", "w")
for line in open(testFile):
	t = line.strip().split(" ")
	i = int(t[0])
	j = int(t[1])
	r = int(t[2])

	totalFea = u[i] + v[j]
		
	if len(totalFea) > 0:
		testDf.write("%d %s\n"%(r, " ".join(totalFea)))
	else:
		print("ERROR: no feature for user %d item %d in test"%(i+1, j +1))
		exit()
testDf.close()

