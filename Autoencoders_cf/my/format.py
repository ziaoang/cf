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
for line in open("U.mid"):
    t = line.strip().split(" ")
    U_fea[int(t[0])] = t[1:]

V_fea = {}
for line in open("V.mid"):
    t = line.strip().split(" ")
    V_fea[int(t[0])] = t[1:]

print("generate target trian file")
df = open(dstTrainFile, "w")
for line in open(trainFile):
    t = line.strip().split(" ")
    i = int(t[0])
    j = int(t[1])
    r = int(t[2])
   
    userFea = "%d:1"%(i-1)
    if i in U_fea:
        for k in range(100):
            userFea += " %d:%s"%(6040+k, U_fea[i][k])

    itemFea = "%d:1"%(j-1)
    if j in V_fea:
        for k in range(100):
            itemFea += " %d:%s"%(3883+k, V_fea[j][k])
    
    df.write("%d 0 %d %d %s %s\n"%(r, userFea.count(" ")+1, itemFea.count(" ")+1, userFea, itemFea))
df.close()


print("generate target test file")
df = open(dstTestFile, "w")
for line in open(testFile):
    t = line.strip().split(" ")
    i = int(t[0])
    j = int(t[1])
    r = int(t[2])

    userFea = "%d:1"%(i-1)
    if i in U_fea:
        for k in range(100):
            userFea += " %d:%s"%(6040+k, U_fea[i][k])

    itemFea = "%d:1"%(j-1)
    if j in V_fea:
        for k in range(100):
            itemFea += " %d:%s"%(3883+k, V_fea[j][k])
    
    df.write("%d 0 %d %d %s %s\n"%(r, userFea.count(" ")+1, itemFea.count(" ")+1, userFea, itemFea))
df.close()



