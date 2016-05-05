import sys

try:
    trainFile       = sys.argv[1]
    testFile        = sys.argv[2]
    dstTrainFile    = sys.argv[3]
    dstTestFile     = sys.argv[4]
except:
    print("trainFile testFile dstTrainFile dstTestFile")
    exit()

df = open(dstTrainFile, "w")
for line in open(trainFile):
    t = line.strip().split(" ")
    df.write("%s 0 1 1 %s:2 %s:2\n"%(t[2], t[0], t[1]))
df.close()

df = open(dstTestFile, "w")
for line in open(testFile):
    t = line.strip().split(" ")
    df.write("%s 0 1 1 %s:2 %s:2\n"%(t[2], t[0], t[1]))
df.close()

