from day12 import calculate_manhattan_distance, parse_line

waypoint_x = 10
waypoint_y = 1
boat_x = 0
boat_y = 0
instructions = []


def read_data():
    with open("input12.txt", "r") as fp:
        for line in fp:
            instructions.append(parse_line(line))


if __name__ == '__main__':
    read_data()
    for instr in instructions:
        if instr[0] == 'F':
            dx = waypoint_x * instr[1]
            dy = waypoint_y * instr[1]
            boat_x += dx
            boat_y += dy
        elif instr[0] in ['N', 'S', 'E', 'W']:
            if instr[0] == 'N':
                waypoint_y += instr[1]
            elif instr[0] == 'S':
                waypoint_y -= instr[1]
            elif instr[0] == 'E':
                waypoint_x += instr[1]
            else:
                waypoint_x -= instr[1]
        elif instr[0] in ['R', 'L']:
            if instr[0] == 'R':  # clockwise
                d1 = 1
                d2 = -1
            else:  # counter clockwise
                d1 = -1
                d2 = 1
            for _ in range(int(instr[1]/90)):
                wx = waypoint_x
                waypoint_x = waypoint_y * d1
                waypoint_y = wx * d2

    print(calculate_manhattan_distance(boat_x, boat_y))
