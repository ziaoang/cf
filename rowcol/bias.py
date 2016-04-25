

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
uBias = {}
for i in range(1, n+1):
	total = 0
	cnt = 0
	for j in range(1, m+1):
		r = mat[i][j]
		if r > 0:
			total += r
			cnt += 1
	bias = float(total) / cnt if cnt > 0 else 0
	
	t = []
	for j in range(1, m+1):
		r = mat[i][j]
		if r > 0:
			t.append("%d:%f"%(j, r - bias))
	
	u[i] = t
	uBias[i] = bias


v = {}
vBias = {}
for i in range(1, m+1):
	total = 0
	cnt = 0
	for j in range(1, n+1):
		r = mat[j][i]
		if r > 0:
			total += r
			cnt += 1
	bias = float(total) / cnt if cnt > 0 else 0
	
	t = []
	for j in range(1, n+1):
		r = mat[j][i]
		if r > 0:
			t.append("%d:%f"%(m+j, r - bias))
	
	v[i] = t
	vBias[i] = bias


print(len(u))
print(len(v))

trainDf = open("train.rc", "w")
for line in open(trainFile):
	t = line.strip().split(" ")
	i = int(t[0])
	j = int(t[1])
	r = int(t[2])
	
	totalFea = []
			
	targetRow = "%d:%f"%(j, r - uBias[i])
	targetCol = "%d:%f"%(m+i, r - vBias[j])

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
	i = int(t[0])
	j = int(t[1])
	r = int(t[2])
	
	totalFea = []
			
	targetRow = "%d:%f"%(j, r - uBias[i])
	targetCol = "%d:%f"%(m+i, r - vBias[j])

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
