from copy import deepcopy

z_dimensions = {}
w_dimensions = {}


def parse_line(_line):
    lst = []
    for ch in line:
        if ch == '.':
            lst.append(0)
        elif ch == '#':
            lst.append(1)
    return lst


with open("input17.txt", "r") as fp:
    start = []
    for line in fp:
        start.append(parse_line(line))

z_dimensions[0] = start
w_dimensions[0] = z_dimensions


def border_with_0(mx):
    rez = []
    for i in range(len(mx) + 2):
        rez.append([])
        for j in range(len(mx) + 2):
            rez[i].append(0)
    for i in range(len(mx)):
        for j in range(len(mx)):
            rez[i+1][j+1] = mx[i][j]
    return rez


def calculate_active(i, j, curr, prev, nxt):
    s = 0
    for x in range(max(0, i-1), min(len(curr)-1, i+1)+1):
        for y in range(max(0, j-1), min(len(curr)-1, j+1)+1):
            if prev[x][y] == 1:
                s += 1
            if nxt[x][y] == 1:
                s += 1
            if curr[x][y] == 1 and (x != i or y != j):
                s += 1
    return s


def generate_zero_matrix(dim):
    res = []
    for x in range(dim):
        res.append([])
        for y in range(dim):
            res[x].append(0)
    return res


def count_active_in_state(dic):
    s = 0
    for elem in dic.values():
        for row in elem:
            for x in row:
                if x == 1:
                    s += 1
    return s


for contor in range(6):
    z_dimensions[contor+1] = deepcopy(generate_zero_matrix(len(z_dimensions[0])))
    z_dimensions[-contor-1] = deepcopy(generate_zero_matrix(len(z_dimensions[0])))
    for key in z_dimensions.keys():
        z_dimensions[key] = border_with_0(z_dimensions[key])
    cpy = {}
    for key, mx in z_dimensions.items():
        res = deepcopy(mx)
        for i in range(len(mx)):
            for j in range(len(mx[0])):
                try:
                    prev = z_dimensions[abs(key-1)]
                except KeyError:
                    prev = deepcopy(generate_zero_matrix(len(z_dimensions[0])))
                try:
                    nxt = z_dimensions[abs(key+1)]
                except KeyError:
                    nxt = deepcopy(generate_zero_matrix(len(z_dimensions[0])))
                nr = calculate_active(i, j, mx, prev, nxt)
                if mx[i][j] == 1:
                    if nr == 2 or nr == 3:
                        res[i][j] = 1
                    else:
                        res[i][j] = 0
                else:
                    if nr == 3:
                        res[i][j] = 1
                    else:
                        res[i][j] = 0
        cpy[key] = res
    z_dimensions = deepcopy(cpy)

print(count_active_in_state(z_dimensions))
