import sys

try:
    srcFile = sys.argv[1]
    dstFile = sys.argv[2]
    ratio   = float(sys.argv[3])
except:
    print("srcFile dstFile ratio")
    exit()

def scale(srcFile, dstFile, ratio):
    df = open(dstFile, "w")
    for line in open(srcFile):
        t = line.strip().split(" ")
        id = t[0]
        fea = []
        for i in range(1, len(t)):
            oldValue = float(t[i])
            newValue = ratio * oldValue
            fea.append(str(newValue))
        df.write("%s %s\n"%(id, " ".join(fea)))
    df.close()

scale(srcFile, dstFile, ratio)
