import sys

try:
    trainFile       = sys.argv[1]
    testFile        = sys.argv[2]
    targetTrainFile = sys.argv[3]
    targetTestFile  = sys.argv[4]
except:
    print("trainFile testFile targetTrainFile targetTestFile")
    exit()

df = open(targetTrainFile, "w")
for line in open(trainFile):
    t = line.strip().split(" ")
    df.write("%s %s %s\n"%(t[0], t[1], t[2]))
df.close()

df = open(targetTestFile, "w")
for line in open(testFile):
    t = line.strip().split(" ")
    df.write("%s %s %s\n"%(t[0], t[1], t[2]))
df.close()

