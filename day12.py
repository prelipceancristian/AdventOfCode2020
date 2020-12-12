g_vertical_coordinates = 0
g_horizontal_coordinates = 0
g_direction = 0
g_instructions = []
g_dict_directions = {'N': 1, 'E': 1, 'S': -1, 'W': -1}
g_list_of_directions = ['E', 'S', 'W', 'N']


def calculate_manhattan_distance(x, y):
    return abs(x) + abs(y)


def parse_line(line):
    return [line[0], int(line[1:])]


def read_data():
    with open("input12.txt", "r") as fp:
        for line in fp:
            g_instructions.append(parse_line(line))


read_data()


def interpret_data():
    vertical_coordinates = 0
    horizontal_coordinates = 0
    direction = 0
    instructions = g_instructions
    dict_directions = {'N': 1, 'E': 1, 'S': -1, 'W': -1}
    list_of_directions = ['E', 'S', 'W', 'N']
    for instr in instructions:
        if instr[0] in ['N', 'S']:
            vertical_coordinates += instr[1] * dict_directions[instr[0]]  # add to the vert coordinate the current nr
        elif instr[0] in ['E', 'W']:
            horizontal_coordinates += instr[1] * dict_directions[instr[0]]  # add to horizontal coord the current nr
        elif instr[0] in ['R', 'L']:  # change of direction
            if instr[0] == 'R':
                df = 1  # move to the right in the directions list
            else:
                df = -1  # move to the left
            mvm = (instr[1]/90) % 4   # convert to movement in the list
            direction = (direction + df * int(mvm)) % 4  # modify the direction with the movement and the way to move
        elif instr[0] == 'F':
            if list_of_directions[direction] in ['N', 'S']:
                vertical_coordinates += dict_directions[list_of_directions[direction]] * instr[1]
            else:
                horizontal_coordinates += dict_directions[list_of_directions[direction]] * instr[1]
    print(calculate_manhattan_distance(vertical_coordinates, horizontal_coordinates))


if __name__ == '__main__':
    interpret_data()
