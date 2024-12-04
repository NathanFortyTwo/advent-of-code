with open("input1.txt", 'r') as f:
    lines = f.readlines()
L1 = []
L2 = []

for line in lines:
    x, y=line.split("   ")
    L1.append(int(x))
    L2.append(int(y))

seen = dict()
s = 0

for x in L1:
    
    if x in seen:
        s+=seen[x]*x
    else:
        count = L2.count(x)
        seen[x] = count
        s+=count*x

print(s)