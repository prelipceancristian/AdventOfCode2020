from copy import deepcopy

condition_notes = []
my_ticket = []
nearby_tickets = []
condition_links = {}

with open("input16.txt", "r") as fp:
    line = fp.readline()
    while line != "\n":
        line = line.split(" ")
        pair1 = line[1].split('-')
        pair1 = [int(pair1[0]), int(pair1[1])]
        pair2 = line[3].split('-')
        pair2 = [int(pair2[0]), int(pair2[1])]
        condition_notes.append([line[0], pair1, pair2])
        line = fp.readline()
    line = fp.readline()
    line = fp.readline()
    line = line.split(',')
    for value in line:
        my_ticket.append(int(value))
    line = fp.readline()
    line = fp.readline()
    line = fp.readline()
    while line not in ['\n', '']:
        line = line.split(',')
        lst = []
        for value in line:
            lst.append(int(value))
        nearby_tickets.append(lst)
        line = fp.readline()

ticket_scanning_error_rate = 0
c = deepcopy(nearby_tickets)
for tk in nearby_tickets:
    valid_ticket = True
    for value in tk:
        valid = False
        for condition in condition_notes:
            r1 = range(condition[1][0], condition[1][1] + 1)
            r2 = range(condition[2][0], condition[2][1] + 1)
            if value in r1 or value in r2:
                valid = True
        if not valid:
            ticket_scanning_error_rate += value
            valid_ticket = False  # if one value is invalid, the whole ticket is invalid
    if not valid_ticket:
        c.remove(tk)

nearby_tickets = deepcopy(c)

for condition in condition_notes:
    r1 = range(condition[1][0], condition[1][1] + 1)
    r2 = range(condition[2][0], condition[2][1] + 1)
    valid_spots = []
    for i in range(len(nearby_tickets[0])):
        valid = True
        for tk in nearby_tickets:
            if tk[i] not in r1 and tk[i] not in r2:
                valid = False
                break
        if valid is True:
            valid_spots.append(i)
    condition_links[condition[0]] = valid_spots
p = 1

clc = deepcopy(condition_links)
final_dict = {}
# clc = sorted(clc.items(), key=lambda x: x[1], reverse=True)
# final_dict = sorted(clc.items(), key=lambda x: x[1], reverse=True)
# print(clc)

# determine the key with the largest list:
s = 0
k = ""
for key, val in clc.items():
    if len(val) > s:
        s = len(val)
        k = key

while len(clc[k]) > 0:
    for key, val in clc.items():
        if len(val) == 1:
            final_dict[key] = val[0]
            to_delete = val[0]
            for key2, val2 in clc.items():
                if to_delete in val2:
                    val2.remove(to_delete)

for key, val in final_dict.items():
    if key.find('departure') != -1:
        p *= my_ticket[val]

print(p)


