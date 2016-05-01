


total = 0
cnt = 0

for line in open("my/train.txt"):
    t = line.strip().split(" ")
    userId = t[0]
    itemId = t[1]
    rating = int(t[2])

    total += rating
    cnt += 1

print(total)
print(cnt)
print("%.6f"%(float(total)/cnt))


