def convert_word_to_binary(llst):
    binn = []
    for letter in llst:
        binn.append(0 if letter == "F" or letter == "L" else 1)
    return binn


def convert_bin_list_to_number(bin_list):
    s = 0
    p = 1
    rev = bin_list[::-1]
    for nr in rev:
        s += nr*p
        p *= 2
    return s


def get_seat_id(r, c):
    return 8*r+c


with open("input5.txt", "r") as fp:
    lst = [0] * 927
    for line in fp:
        row = line[0:7]
        column = line[7:10]
        row = convert_word_to_binary(row)
        column = convert_word_to_binary(column)
        row = convert_bin_list_to_number(row)
        column = convert_bin_list_to_number(column)
        lst[get_seat_id(row, column)] = 1
    print(lst.index(0, 80))
