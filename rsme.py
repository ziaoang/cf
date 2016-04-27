import sys
import math

try:
	resultFile  = sys.argv[1]
	submitFile  = sys.argv[2]
	resultIndex = int(sys.argv[3])
	submitIndex = int(sys.argv[4])
except:
	print("resultFile submitFile resultIndex submitIndex")
	exit()

err = 0
cnt = 0

resSf = open(resultFile, "r")
subSf = open(submitFile, "r")

while True:
	resLine = resSf.readline()
	subLine = subSf.readline()
	
	if not resLine or not subLine:
		break
	
	real = float(resLine.strip().split(" ")[resultIndex])
	predict = float(subLine.strip().split(" ")[submitIndex])

	err += (real - predict) ** 2
	cnt += 1

err = math.sqrt(err/cnt)

print("%.6f"%err)



