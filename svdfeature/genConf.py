import sys

try:
    trainFile = sys.argv[1]
    testFile = sys.argv[2]
    confFile = sys.argv[3]
except:
    print("trainFile testFile confFile")
    exit()

globalSet = set()
userSet = set()
itemSet = set()

total = 0
cnt = 0
for line in open(trainFile):
    t = line.strip().split(" ")
    
    y = float(t[0])
    
    global_num = int(t[1])
    user_num = int(t[2])
    item_num = int(t[3])
    
    for i in range(4, 4+global_num):
        tt = t[i].split(":")
        globalSet.add(tt[0])
    
    for i in range(4+global_num, 4+global_num+user_num):
        tt = t[i].split(":")
        userSet.add(tt[0])
    
    for i in range(4+global_num+user_num, 4+global_num+user_num+item_num):
        tt = t[i].split(":")
        itemSet.add(tt[0])

    total += y
    cnt += 1

for line in open(testFile):
    t = line.strip().split(" ")
    
    y = float(t[0])
    
    global_num = int(t[1])
    user_num = int(t[2])
    item_num = int(t[3])
    
    for i in range(4, 4+global_num):
        tt = t[i].split(":")
        globalSet.add(tt[0])
    
    for i in range(4+global_num, 4+global_num+user_num):
        tt = t[i].split(":")
        userSet.add(tt[0])
    
    for i in range(4+global_num+user_num, 4+global_num+user_num+item_num):
        tt = t[i].split(":")
        itemSet.add(tt[0])


globalList = [int(v) for v in globalSet]
userList = [int(v) for v in userSet]
itemList = [int(v) for v in itemSet]

globalList.sort()
userList.sort()
itemList.sort()

num_global = globalList[-1]+1 if len(globalList) > 0 else 0
num_user = userList[-1]+1 if len(userList) > 0 else 0
num_item = itemList[-1]+1 if len(itemList) > 0 else 0

df = open(confFile, "w")

df.write("base_score = %f\n"%(total/cnt))
df.write("num_global = %d\n"%num_global)
df.write("num_user   = %d\n"%num_user)
df.write("num_item   = %d\n"%num_item)

df.write("active_type = 0\n")
df.write("num_factor  = 256\n")

df.write("learning_rate = 0.004\n")
df.write("wd_item       = 0.028\n")
df.write("wd_user       = 0.028\n")

df.close()



