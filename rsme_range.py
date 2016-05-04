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

ratingSet = set()

resultList = []
for line in open(resultFile):
    t = line.strip().split(" ")
    rating = float(t[resultIndex])
    resultList.append(rating)
    ratingSet.add(rating)

submitList = []
for line in open(submitFile):
    t = line.strip().split(" ")
    rating = float(t[submitIndex])
    submitList.append(rating)

if len(resultList) != len(submitList):
    print("ERROR: not same length")
    exit()

ratingList = list(ratingSet)
ratingList.sort()
minV = ratingList[0]
maxV = ratingList[-1]

err = 0
cnt = len(resultList)
for i in range(cnt):
    result = resultList[i]
    submit = submitList[i]

    if submit < minV:
        submit = minV
    if submit > maxV:
        submit = maxV

    err += (result - submit) ** 2

err = math.sqrt(err/cnt)

print("%.6f"%err)



