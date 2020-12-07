def parse_data(matrix, new_line):
    lst = []
    for x in new_line:
        if x == '#':
            lst.append(1)
        else:
            lst.append(0)
    matrix.append(lst)


mx = []
right_step = 3
down_step = 1


def read_data():
    with open("input3.txt") as fp:
        for line in fp:
            parse_data(mx, line)


read_data()
width = len(mx[0]) - 1


def calculate_sudden_arboreal_stops(r, d):
    down = right = counter = 0
    while down < len(mx) - d:
        down += d
        right += r
        right = right % width
        if mx[down][right] == 1:
            counter += 1
    return counter


print(calculate_sudden_arboreal_stops(1, 1) *
      calculate_sudden_arboreal_stops(3, 1) *
      calculate_sudden_arboreal_stops(5, 1) *
      calculate_sudden_arboreal_stops(7, 1) *
      calculate_sudden_arboreal_stops(1, 2))
