preamble = []
all_numbers = []


def find_irregularity(pre, nr):
    left = 0
    prev = sorted(pre)
    right = len(prev) - 1
    while left < right:
        if prev[left] + prev[right] < nr:
            left += 1
        elif prev[left] + prev[right] > nr:
            right -= 1
        else:
            pre.pop(0)
            pre.append(nr)
            return False
    return True


def find_subseq_with_sum(lst, nr):
    if lst == [] and nr == 0:
        return True
    find_subseq_with_sum(lst[1:], nr-lst[0])
    find_subseq_with_sum(lst[1:], nr)


def quick_and_dirty_solve(lst, nr):
    for i in range(len(lst) - 1):
        for j in range(i+1, len(lst) - 1):
            if sum(lst[i:j]) == nr:
                return min(lst[i:j]) + max(lst[i:j])


def first_problem():
    with open("input9.txt", "r") as fp:
        for x in range(25):
            nr = int(fp.readline())
            preamble.append(nr)
            all_numbers.append(nr)
        for line in fp:
            nr = int(line)
            all_numbers.append(nr)
            if find_irregularity(preamble, nr):
                # print(int(line))
                return quick_and_dirty_solve(all_numbers, int(line))


print(first_problem())
