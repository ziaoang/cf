import sys


try:
    n       = int(sys.argv[1])
    m       = int(sys.argv[2])
    trainFile   = sys.argv[3]
    testFile    = sys.argv[4]
    dstTrainFile    = sys.argv[5]
    dstTestFile     = sys.argv[6]
    removeBias  = True if sys.argv[7] == "1" else False
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
U_fea = {}
U_cnt = {}
for i in range(1, n+1):
    t = []
    for j in range(1, m+1):
        r = MATRIX[i][j]
        if r > 0:
            t.append("%d:%d"%(j, r))
    U_fea[i] = " ".join(t)
    U_cnt[i] = len(t)


print("compute V")
V_fea = {}
V_cnt = {}
for j in range(1, m+1):
    t = []
    for i in range(1, n+1):
        r = MATRIX[i][j]
        if r > 0:
            t.append("%d:%d"%(i, r))
    V_fea[j] = " ".join(t)
    V_cnt[j] = len(t)


print("generate target trian file")
df = open(dstTrainFile, "w")
for line in open(trainFile):
    t = line.strip().split(" ")
    i = int(t[0])
    j = int(t[1])
    r = int(t[2])
    
    if U_cnt[i] == 0 and V_cnt[j] == 0:
        print("ERROR")
        exit()
    if U_cnt[i] == 0:
        df.write("%d 0 %d %d %s\n"%(r, U_cnt[i], V_cnt[j], V_fea[j]))
    elif V_cnt[j] == 0:
        df.write("%d 0 %d %d %s\n"%(r, U_cnt[i], V_cnt[j], U_fea[i]))
    else:
        df.write("%d 0 %d %d %s %s\n"%(r, U_cnt[i], V_cnt[j], U_fea[i], V_fea[j]))
df.close()


print("generate target test file")
df = open(dstTestFile, "w")
for line in open(testFile):
    t = line.strip().split(" ")
    i = int(t[0])
    j = int(t[1])
    r = int(t[2])
    
    if U_cnt[i] == 0 and V_cnt[j] == 0:
        print("ERROR")
        exit()
    if U_cnt[i] == 0:
        df.write("%d 0 %d %d %s\n"%(r, U_cnt[i], V_cnt[j], V_fea[j]))
    elif V_cnt[j] == 0:
        df.write("%d 0 %d %d %s\n"%(r, U_cnt[i], V_cnt[j], U_fea[i]))
    else:
        df.write("%d 0 %d %d %s %s\n"%(r, U_cnt[i], V_cnt[j], U_fea[i], V_fea[j]))
df.close()
















