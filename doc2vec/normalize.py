
def normalize(srcFile, dstFile):
    df = open(dstFile, "w")
    for line in open(srcFile):
        t = line.strip().split(" ")
        id = t[0]
        fea = []
        for i in range(1, len(t)):
            fea.append(float(t[i]))
        minV = fea[0]
        maxV = fea[0]
        for v in fea:
            minV = min(minV, v)
            maxV = max(maxV, v)
        norFea = []
        for v in fea:
            norV = (v - minV) / (maxV - minV)
            norFea.append(str(norV))
        df.write("%s %s\n"%(id, " ".join(norFea)))
    df.close()

normalize("doc2vec.model", "doc2vec.model.normalize")

