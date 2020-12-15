fp = open("input15.txt", "r")
data = fp.readline()
data = data.split(',')
master_dict = {}
turn = 1
last_spoken_number = int(data[-1])
spoken_number = -1
for elem in data:
    master_dict[int(elem)] = turn
    turn += 1
del master_dict[int(data[-1])]
while turn <= 30000000:
    try:
        val = master_dict[last_spoken_number]
        spoken_number = turn - val - 1
        master_dict[last_spoken_number] = turn - 1
        last_spoken_number = spoken_number
    except KeyError:
        master_dict[last_spoken_number] = turn - 1
        spoken_number = 0
        last_spoken_number = spoken_number
    turn += 1
# spoken number might be useless but i'm too lazy to refactor the code
print(spoken_number)
