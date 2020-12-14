mask = []
mem = [0] * pow(2, 16)
mem_dict = {}


def dec_to_bin_list(nr):
    lst = [0] * 36
    contor = 0
    while nr:
        lst[contor] = nr % 2
        nr //= 2
        contor += 1
    return lst[::-1]


def prob_1():
    with open("input14.txt", "r") as fp:
        for line in fp:
            line = line.split(" ")
            if line[0] == 'mask':
                mask = line[2].strip()
            else:
                mem_pos = int(line[0][line[0].find('[')+1:line[0].find(']')])
                number = dec_to_bin_list(int(line[2]))
                res = 0
                p = 1
                for c in range(36):
                    if mask[35-c] == 'X':
                        res = res + number[35-c]*p
                    else:
                        res = res + int(mask[35-c])*p
                    p *= 2
                mem[mem_pos] = res
    print(sum(mem))


def interpret_address(mem_address, val):
    x_counter = True  # assume there are no Xs in the memory address
    nr = 0
    while x_counter and nr < len(mem_address): # until we reach the end or we find an x
        if mem_address[nr] == 'X':  # if we found one
            adr_1 = mem_address[:nr] + ['1'] + mem_address[nr+1:]  # replace found x with 1
            adr_0 = mem_address[:nr] + ['0'] + mem_address[nr+1:]  # replace found x with 0
            interpret_address(adr_1, val)  # try for those addresses
            interpret_address(adr_0, val)
            x_counter = False  # set counter
        nr += 1  # increment nr, no matter the outcome of the if
    if x_counter:  # if x_counter is true, it means there were no Xs in the memory address and therefore it is valid
        str_mem_address = ''.join([str(elem) for elem in mem_address])
        # mem[int(str_mem_address, 2)] = val  # mem address is string which represents a binary val, should be converted
        mem_dict[int(str_mem_address, 2)] = val


def prob_2():
    with open("input14.txt", "r") as fp:
        for line in fp:
            line = line.split(" ")
            if line[0] == 'mask':
                mask = line[2].strip()
            else:
                mem_pos = line[0][line[0].find('[')+1:line[0].find(']')]
                number = int(line[2].strip())
                bin_list_mem_pos = dec_to_bin_list(int(mem_pos))
                res = []
                for x in range(36):
                    if mask[x] in ['1', 'X']:
                        res.append(mask[x])
                    else:
                        res.append(bin_list_mem_pos[x])
                interpret_address(res, number)
        s = 0
        for elem in mem_dict.values():
            s += elem
        print(s)


prob_2()
