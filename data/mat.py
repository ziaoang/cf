


row = {}
for i in range(6040):
	row[i] = 0
col = {}
for i in range(3883):
	col[i] = 0

mat = [[0]*3883 for i in range(6040)]

for line in open("my/train.txt"):
	t = line.strip().split(" ")
	userId = int(t[0]) - 1
	itemId = int(t[1]) - 1
	rating = int(t[2])
	mat[userId][itemId] = rating

	row[userId] = 1
	col[itemId] = 1


cnt = 0
for i in range(6040):
	cnt += row[i]
print("%d/%d"%(cnt, 6040))


cnt = 0
for i in range(3883):
	cnt += col[i]
print("%d/%d"%(cnt, 3883))

