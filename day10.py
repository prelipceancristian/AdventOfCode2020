adapters = [0]
diff = []
sums = []
s = 0
with open("input10.txt", "r") as fp:
    for line in fp:
        adapters.append(int(line))

adapters.sort()
diff_1 = 0
diff_3 = 0
adapters.append(max(adapters)+3)

prev = 0
for x in adapters:
    if prev - x == 2:
        print(prev, " ", x)
    prev = x

for x in range(len(adapters) - 1):
    d = adapters[x+1] - adapters[x]
    diff.append(d)
    if d == 3:
        diff_3 += 1
    else:
        diff_1 += 1

print(diff_1 * diff_3)


def f(n):
    return 1 + n*(n-1)/2


for x in diff:
    if x == 1:
        s += 1
    elif s != 0:
        sums.append(s)
        s = 0

p = 1
for x in sums:
    p *= f(x)

print(int(p))
