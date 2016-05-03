


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

#scale("model/doc2vec.model", "model/doc2vec.0.1.model", 0.1)
#scale("model/doc2vec.model", "model/doc2vec.0.2.model", 0.2)
#scale("model/doc2vec.model", "model/doc2vec.0.3.model", 0.3)
#scale("model/doc2vec.model", "model/doc2vec.0.4.model", 0.4)
#scale("model/doc2vec.model", "model/doc2vec.0.5.model", 0.5)
#scale("model/doc2vec.model", "model/doc2vec.0.6.model", 0.6)
#scale("model/doc2vec.model", "model/doc2vec.0.7.model", 0.7)
#scale("model/doc2vec.model", "model/doc2vec.0.8.model", 0.8)
#scale("model/doc2vec.model", "model/doc2vec.0.9.model", 0.9)

scale("model/doc2vec.model", "model/doc2vec.2.model", 2)
scale("model/doc2vec.model", "model/doc2vec.3.model", 3)
scale("model/doc2vec.model", "model/doc2vec.4.model", 4)
scale("model/doc2vec.model", "model/doc2vec.5.model", 5)
