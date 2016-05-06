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


resultList = []
for line in open(resultFile):
    t = line.strip().split(" ")
    rating = float(t[resultIndex])
    resultList.append(rating)

submitList = []
for line in open(submitFile):
    t = line.strip().split(" ")
    rating = float(t[submitIndex])
    submitList.append(rating)

if len(resultList) != len(submitList):
    print("ERROR: not same length")
    exit()

err = 0
cnt = len(resultList)
for i in range(cnt):
    result = resultList[i]
    submit = submitList[i]
    err += (result - submit) ** 2
err = math.sqrt(err/cnt)
print("%.6f"%err)

