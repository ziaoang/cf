import sys

try:
    srcFile = sys.argv[1]
    dstFile = sys.argv[2]
except:
    print("srcFile dstFile")
    exit()

df = open(dstFile, "w")
for line in open(srcFile):
    t = line.strip().split(" ")
    df.write("%s 0 1 1 %s:1 %s:1\n"%(t[2], t[0], t[1]))
df.close()

