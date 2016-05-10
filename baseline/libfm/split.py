import random

trainDf = open("train.libfm", "w")
testDf = open("test.libfm", "w")

random.seed(123456789)
for line in open("ratings.dat.libfm"):
	if random.random() < 0.9:
		trainDf.write(line)
	else:
		testDf.write(line)

trainDf.close()
testDf.close()



