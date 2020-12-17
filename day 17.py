z_dimensions = {}


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


def border_with_0(mx):
    rez = [[0]*len(mx)]*len(mx)
    for i in range(len(mx)):
        for j in range(len(mx[0])):
            rez[i][j] = mx[i][j]
    return rez


def calculate_active(i, j, curr, prev, nxt):
    for x in range(max(0, i-1))


for contor in range(6):
    z_dimensions[contor+1] = [[0]*len(z_dimensions[0])]*len(z_dimensions[0])
    for mx in z_dimensions.values():
        mx = border_with_0(mx)
    for key, mx in z_dimensions.items():
        for i in range(len(mx)):
            for j in range(len(mx[0])):
                nr = calculate_active(i, j, mx, z_dimensions[abs(key-1)], z_dimensions[abs(key+1)])


