import sys


try:
    trainFile       = sys.argv[1]
    testFile        = sys.argv[2]
    dstTrainFile    = sys.argv[3]
    dstTestFile     = sys.argv[4]
except:
    print("trainFile testFile dstTrainFile dstTestFile")
    exit()


n = 6040
m = 3883


print("compute U and V")
U_fea = {}
U_cnt = {}
V_fea = {}
V_cnt = {}
for line in open("../libmf/1.model"):
    if line[0] == 'p':
        t = line.strip().split(" ")
        if t[1] == "T":
            userId = int(t[0][1:])
            fea = []
            for i in range(2, len(t)):
                fea.append("%d:%s"%(i-2, t[i]))
            U_fea[userId] = " ".join(fea)
            U_cnt[userId] = len(fea)
    elif line[0] == 'q':
        t = line.strip().split(" ")
        if t[1] == "T":
            itemId = int(t[0][1:])
            fea = []
            for i in range(2, len(t)):
                fea.append("%d:%s"%(i-2, t[i]))
            V_fea[itemId] = " ".join(fea)
            V_cnt[itemId] = len(fea)


print("generate target trian file")
df = open(dstTrainFile, "w")
for line in open(trainFile):
    t = line.strip().split(" ")
    i = int(t[0])
    j = int(t[1])
    r = int(t[2])
    
    if i in U_fea and j in V_fea:
        df.write("%d 0 %d %d %s %s\n"%(r, U_cnt[i], V_cnt[j], U_fea[i], V_fea[j]))
    elif i in U_fea and j not in V_fea:
        df.write("%d 0 %d %d %s\n"%(r, U_cnt[i], 0, U_fea[i]))
    elif i not in U_fea and j in V_fea:
        df.write("%d 0 %d %d %s\n"%(r, 0, V_cnt[j], V_fea[j]))
    else:
        print("ERROR")
        exit()
df.close()


print("generate target test file")
df = open(dstTestFile, "w")
for line in open(testFile):
    t = line.strip().split(" ")
    i = int(t[0])
    j = int(t[1])
    r = int(t[2])
    
    if i in U_fea and j in V_fea:
        df.write("%d 0 %d %d %s %s\n"%(r, U_cnt[i], V_cnt[j], U_fea[i], V_fea[j]))
    elif i in U_fea and j not in V_fea:
        df.write("%d 0 %d %d %s\n"%(r, U_cnt[i], 0, U_fea[i]))
    elif i not in U_fea and j in V_fea:
        df.write("%d 0 %d %d %s\n"%(r, 0, V_cnt[j], V_fea[j]))
    else:
        print("ERROR")
        exit()
df.close()



