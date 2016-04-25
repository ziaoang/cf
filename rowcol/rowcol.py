

trainFile = "train.txt"
testFile = "test.txt"

n = 6040
m = 3883

mat = []
for i in range(n):
	t = []
	for j in range(m):
		t.append(0)
	mat.append(t)

for line in open(trainFile):
	t = line.strip().split(" ")
	i = int(t[0]) - 1
	j = int(t[1]) - 1
	r = int(t[2])
	mat[i][j] = r

u = {}
for i in range(n):
	t = []
	for j in range(m):
		r = mat[i][j]
		if r > 0:
			t.append("%d:%d"%(j, r))
	u[i] = t

v = {}
for i in range(m):
	t = []
	for j in range(n):
		r = mat[j][i]
		if r > 0:
			t.append("%d:%d"%(m+j, r))
	v[i] = t

print(len(u))
print(len(v))

trainDf = open("train.rc", "w")
for line in open(trainFile):
	t = line.strip().split(" ")
	i = int(t[0]) - 1
	j = int(t[1]) - 1
	r = int(t[2])
	
	totalFea = []
			
	targetRow = "%d:%d"%(j, r)
	targetCol = "%d:%d"%(m+i, r)

	cnt = 0
	rowFea = u[i]
	for fea in rowFea:
		if fea == targetRow:
			cnt += 1
		else:
			totalFea.append(fea)
	if cnt != 1:
		print("ERROR: row featrue in train")
	
	cnt = 0
	colFea = v[j]
	for fea in colFea:
		if fea == targetCol:
			cnt += 1
		else:
			totalFea.append(fea)
	if cnt != 1:
		print("ERROR: col featrue in train")
	

	if len(totalFea) > 0:
		trainDf.write("%d %s\n"%(r, " ".join(totalFea)))
	else:
		print("ERROR: no feature for user %d item %d in train"%(i+1, j +1))
		exit()
trainDf.close()


testDf = open("test.rc", "w")
for line in open(testFile):
	t = line.strip().split(" ")
	i = int(t[0]) - 1
	j = int(t[1]) - 1
	r = int(t[2])
	
	totalFea = []
			
	targetRow = "%d:%d"%(j, r)
	targetCol = "%d:%d"%(m+i, r)

	cnt = 0
	rowFea = u[i]
	for fea in rowFea:
		if fea == targetRow:
			cnt += 1
		else:
			totalFea.append(fea)
	if cnt != 0:
		print("ERROR: row featrue in test")
		
	cnt = 0
	colFea = v[j]
	for fea in colFea:
		if fea == targetCol:
			cnt += 1
		else:
			totalFea.append(fea)
	if cnt != 0:
		print("ERROR: col featrue in test")
		
	if len(totalFea) > 0:
		testDf.write("%d %s\n"%(r, " ".join(totalFea)))
	else:
		print("ERROR: no feature for user %d item %d in test"%(i+1, j +1))
		exit()
testDf.close()
