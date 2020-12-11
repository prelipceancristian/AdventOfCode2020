from copy import deepcopy
seats = []


def convert_line_to_data(matrix_line, my_line):
    for ch in my_line:
        if ch == 'L':
            matrix_line.append(1)
        elif ch == '.':
            matrix_line.append(0)


def read_data(matrix):
    c = 0
    with open("input11.txt", "r") as fp:
        for line in fp:
            matrix.append([])
            convert_line_to_data(matrix[c], line)
            c += 1


def print_matrix(matrix):
    for row in matrix:
        print(row)


def count_occupied_seats(matrix):
    s = 0
    for line in matrix:
        for x in line:
            if x == -1:
                s += 1
    return s


def simulate(matrix):
    copie = deepcopy(matrix)
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] != 0:  # is not floor
                free_seats = 0
                occupied_seats = 0
                for x in range(max(row - 1, 0),
                               min(row + 1, len(matrix) - 1) + 1):  # obtain possible values for neighbours
                    for y in range(max(col - 1, 0), min(col + 1, len(matrix[row]) - 1) + 1):  # -//-
                        if x != row or y != col:
                            if matrix[x][y] == 1:
                                free_seats += 1
                            elif matrix[x][y] == -1:
                                occupied_seats += 1  # determine no of occupied and free seats
                if matrix[row][col] == 1 and occupied_seats == 0:
                    copie[row][col] = -1
                elif matrix[row][col] == -1 and occupied_seats >= 4:
                    copie[row][col] = 1
    return copie


def final_state(matrix):
    prev = []
    while prev != matrix:
        prev = deepcopy(matrix)
        matrix = simulate(matrix)
    return prev


def look_in_direction(matrix, row, col, x, y):
    initial_row = row
    initial_col = col
    cond = True
    while cond:
        if 0 <= row + x < len(matrix) and 0 <= col + y < len(matrix[row]):
            row += x
            col += y
            if matrix[row][col] != 0:
                cond = False
        else:
            cond = False
    if matrix[row][col] == -1 and (initial_col != col or initial_row != row):
        return 1
    return 0


def simulate2(matrix):
    """
    We apply the same idea for moving in the matrix to access the elements
    For the first seen seat there is a need for a while loop. That should take as arguments the directions to indicate
    the way of movement. The loop should go until it reaches the margin or it finds a seat. if the seat is empty or the
    margin is touched the function should consider it as an empty seat and should return 0. Otherwise it will return 1
    The main loop will count the number of occupied seats for each element and make a decision based on the problem
    conditions
    """
    copie = deepcopy(matrix)
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            occupied_seats = 0
            if matrix[row][col] != 0:  # not floor
                for x in range(-1, 2):
                    for y in range(-1, 2):  # generate directions to look at
                        if not(x == 0 and y == 0):
                            occupied_seats += look_in_direction(matrix, row, col, x, y)
                if matrix[row][col] == 1 and occupied_seats == 0:  # if it is empty and there are no seats to be seen
                    copie[row][col] = -1  # fill
                elif matrix[row][col] == -1 and occupied_seats >= 5:  # if it is filled but there are 5 or more
                    # occupied it becomes empty
                    copie[row][col] = 1
    return copie


def final_state2(matrix):
    prev = []
    while prev != matrix:
        prev = deepcopy(matrix)
        matrix = simulate2(matrix)
    return prev


read_data(seats)
seats = final_state2(seats)
print(count_occupied_seats(seats))
