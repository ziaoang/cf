import sys


try:
	raw = sys.argv[1]
	sgd = sys.argv[2]
	als = sys.argv[3]
	mcmc = sys.argv[4]
	out = sys.argv[5]
except:
	print("raw sgd als mcmc out")
	exit()


rawSf = open(raw, "r")
sgdSf = open(sgd, "r")
alsSf = open(als, "r")
mcmcSf = open(mcmc, "r")

df = open(out, "w")
while True:
	rawLine = rawSf.readline()
	sgdLine = sgdSf.readline()
	alsLine = alsSf.readline()
	mcmcLine = mcmcSf.readline()

	if not rawLine or not sgdLine or not alsLine or not mcmcLine:
		break

	t = rawLine.strip().split(" ")
	
	df.write("%s 1:%s 2:%s 3:%s\n"%(t[0], sgdLine.strip(), alsLine.strip(), mcmcLine.strip()))
df.close()



