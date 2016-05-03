

df = open("train.txt", "w")
for line in open("../data/my/train.txt"):
    t = line.strip().split(" ")
    df.write("%s %s %s\n"%(t[0], t[1], t[2]))
df.close()


df = open("test.txt", "w")
for line in open("../data/my/test.txt"):
    t = line.strip().split(" ")
    df.write("%s %s %s\n"%(t[0], t[1], t[2]))
df.close()
