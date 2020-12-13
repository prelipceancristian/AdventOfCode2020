from functools import reduce

"""
For the second problem:
Finding the timestamp at which the conditions are met can be done by finding t such that:
t + bus_code_offset = bus_code * k
for every bus_code in the input
Using the chinese reminder theorem it is possible to find the number using the sets of coprime dividers as the bus codes
and the reminders as the offsets 
"""


def prob_1():
    best_bus = -1
    best_wait_time = 0
    with open("input13.txt", "r") as fp:
        eta = int(fp.readline())
        best_wait_time = eta
        buses = (fp.readline()).split(',')
        for line in buses:
            if 'x' not in line:
                if eta / int(line) == 0 and best_bus != 0:
                    best_bus = int(line)
                    best_wait_time = 0
                elif int(line) + int(eta / int(line)) * int(line) - eta < best_wait_time:
                    best_bus = int(line)
                    best_wait_time = int(line) + int(eta / int(line)) * int(line) - eta
        print(best_bus * best_wait_time)


def prob_2():

    def chinese_remainder(n, a):
        sum = 0
        prod = reduce(lambda a, b: a * b, n)
        for n_i, a_i in zip(n, a):
            p = prod // n_i
            sum += a_i * mul_inv(p, n_i) * p
        return sum % prod

    def mul_inv(a, b):
        b0 = b
        x0, x1 = 0, 1
        if b == 1: return 1
        while a > 1:
            q = a // b
            a, b = b, a % b
            x0, x1 = x1 - q * x0, x0
        if x1 < 0: x1 += b0
        return x1

    n = []
    a = []
    with open("input13.txt", "r") as fp:
        _ = fp.readline()
        line = fp.readline()
        line = line.split(',')
        rem = 0
        for x in line:
            if x != 'x':
                n.append(int(x))
                a.append(-rem)
            rem += 1
    print(chinese_remainder(n, a))


prob_2()
