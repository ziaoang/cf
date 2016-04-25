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
	df.write(t[0])
	for i in range(1, len(t)):
		tt = t[i].split(":")
		index = int(tt[0])
		value = tt[1]
		df.write(" %d:%s"%(index+1, value))
	df.write("\n")
df.close()
