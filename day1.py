f = open("numbers.txt", "r")

lst = []

for _ in range(200):
    lst.append(int(f.readline()))

lst.sort()

up = len(lst) - 1
down = 0

while down < up:
    s = lst[up] + lst[down]
    if s > 2020:
        up -= 1
    elif s < 2020:
        down += 1
    else:
        print(lst[up], " ", lst[down])
        print(lst[up] * lst[down])
        down = up

for i in range(200):
    for j in range(i + 1, 200):
        for k in range(j + 1, 200):
            if lst[i] + lst[j] + lst[k] == 2020:
                print(lst[i]*lst[j]*lst[k])