from copy import deepcopy

instructions = []
visited = []
accumulator = 0
pos = 0


with open("input8.txt", "r") as fp:
    for line in fp:
        instructions.append(line.strip())

visited = [False] * len(instructions)


def interpret_line():
    global pos
    global accumulator
    keyword = instructions[pos][0:3]
    argument = int(instructions[pos][4:])
    if keyword == 'acc':
        accumulator += argument
        pos += 1
    elif keyword == 'jmp':
        pos += argument
    else:
        pos += 1


def determine_accumulator():
    while True:
        if visited[pos] or pos == len(visited) - 1:
            return accumulator
        visited[pos] = True
        interpret_line()


def simulate(lst):
    visited = [False] * len(lst)
    pos = 0
    while not visited[pos] and pos != len(lst) - 1:  # either get to the end or start another loop
        visited[pos] = True
        if lst[pos][0:3] == 'jmp':
            pos += int(lst[pos][4:])
        else:
            pos += 1
    if pos == len(lst) - 1:
        return True
    return False


def determine_instr_to_change():
    global instructions
    for x in range(len(instructions) - 1):
        c = deepcopy(instructions)
        keyword = c[x][0:3]
        if keyword == 'nop':
            keyword = 'jmp'
        elif keyword == 'jmp':
            keyword = 'nop'
        new_command = keyword + " " + c[x][4:]
        if new_command != c[x]:
            c[x] = new_command  # assign the new command to the correct place in the list of instructions
            res = simulate(c)
            if res:
                instructions = deepcopy(c)
                return determine_accumulator()

# don t run at the same time
# print(determine_accumulator())
print(determine_instr_to_change())
