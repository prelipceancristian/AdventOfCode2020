
def parse_line(line):
    args = line.split(" ")
    lst = []
    bounds = args[0].split("-")
    letter = args[1][0]
    lst.append(bounds[0])
    lst.append(bounds[1])
    lst.append(letter)
    lst.append(args[2])
    return lst

f = open("passwords.txt", "r")

counter = 0

for i in range(1000):
    args = parse_line(f.readline())
    if bool(args[3][int(args[0]) - 1] is args[2]) != bool(args[3][int(args[1])-1] is args[2]):
        counter += 1

print(counter)
