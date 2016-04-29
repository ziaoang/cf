import sys


try:
    trainFile       = sys.argv[1]
    testFile        = sys.argv[2]
    dstTrainFile    = sys.argv[3]
    dstTestFile     = sys.argv[4]
except:
    print("trainFile testFile dstTrainFile dstTestFile")
    exit()


print("generate target trian file")
df = open(dstTrainFile, "w")
for line in open(trainFile):
    t = line.strip().split(" ")
    i = int(t[0])-1
    j = int(t[1])-1
    r = int(t[2])
    df.write("%d 0 1 1 %d:1 %d:1\n"%(r, i, j))
df.close()


print("generate target test file")
df = open(dstTestFile, "w")
for line in open(testFile):
    t = line.strip().split(" ")
    i = int(t[0])-1
    j = int(t[1])-1
    r = int(t[2])
    df.write("%d 0 1 1 %d:1 %d:1\n"%(r, i, j))
df.close()



