equations = []


def solve_clean_equation(eq):
    eq = eq.split(' ')
    res = int(eq[0])
    eq.pop(0)
    while len(eq) != 0:
        op = eq[0]
        t2 = eq[1]
        if op == '*':
            res *= int(t2)
        else:
            res += int(t2)
        eq = eq[2:]
    return res


def solve_clean_advanced_equation(eq):
    eq = eq.split(' ')
    while '+' in eq:
        for ind, elem in enumerate(eq):
            if elem == '+':
                e = eq[ind - 1] + ' ' + eq[ind] + ' ' + eq[ind + 1]
                _ = eq.pop(ind)
                _ = eq.pop(ind)
                eq[ind-1] = str(solve_clean_equation(e))
    s = ''
    for elem in eq:
        s += elem
        s += ' '
    s = s[:-1]
    return solve_clean_equation(s)


def solve_advanced_equation(eq):
    left_bracket_pos = -1
    right_bracket_pos = -1
    while '(' in eq:
        for ind, elem in enumerate(eq):
            if elem == '(':
                left_bracket_pos = ind
            if elem == ')':
                right_bracket_pos = ind
                expression = eq[left_bracket_pos:right_bracket_pos + 1]
                expression_without_brackets = eq[left_bracket_pos + 1:right_bracket_pos]
                eq = eq.replace(expression, str(solve_clean_advanced_equation(expression_without_brackets)))
                break
    return solve_clean_advanced_equation(eq)


def solve_equation(eq):
    left_bracket_pos = -1
    right_bracket_pos = -1
    while eq.find('(') != -1:
        for ind, ch in enumerate(eq):
            if ch == '(':
                left_bracket_pos = ind
            if ch == ')':
                right_bracket_pos = ind
                expression = eq[left_bracket_pos:right_bracket_pos+1]
                expression_without_brackets = eq[left_bracket_pos+1:right_bracket_pos]
                eq = eq.replace(expression, str(solve_clean_equation(expression_without_brackets)))
                break
    return solve_clean_equation(eq)


def parse_data(_line):
    # _line = _line.replace(" ", "")
    _line = _line.strip()
    equations.append(_line)


with open("input18.txt", "r") as fp:
    for line in fp:
        parse_data(line)

print(sum(map(solve_advanced_equation, equations)))
# print(sum(map(solve_equation, equations)))
