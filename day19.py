from copy import deepcopy

rules = {}
messages = []


def parse_rule(_line):
    _line = _line.strip()
    _line = _line.split(':')
    if '|' in _line[1]:
        _line[1] = _line[1].split('|')
        set1 = _line[1][0].strip().split(' ')
        set2 = _line[1][1].strip().split(' ')
        for ind, elem in enumerate(set1):
            set1[ind] = int(elem)
        for ind, elem in enumerate(set2):
            set2[ind] = int(elem)
        rules[int(_line[0])] = [set1, set2]
    elif '"' not in _line[1]:
        set1 = _line[1].strip()
        set1 = set1.split(' ')
        for ind, elem in enumerate(set1):
            set1[ind] = int(elem)
        rules[int(_line[0])] = set1
    else:
        rules[int(_line[0])] = _line[1].replace('"', '').strip()


def check_message(msg, rule_number):
    if isinstance(rules[rule_number], str):
        if msg[0] != rules[rule_number]:
            return [False, msg]
        else:
            return [True, msg[1:]]
    if isinstance(rules[rule_number][0], int):
        var = True
        for rule_nr in rules[rule_number]:
            f_c = check_message(msg, rule_nr)
            msg = f_c[1]
            var = var and f_c[0]
        return [var, msg]
    if isinstance(rules[rule_number][0], list):
        state1 = True
        state2 = True
        for rule_nr in rules[rule_number][0]:
            msgc = deepcopy(msg)
            f_c = check_message(msg, rule_nr)
            msg = f_c[1]
            state1 = state1 and f_c[0]
            msg = msgc
        for rule_nr in rules[rule_number][1]:
            f_c = check_message(msg, rule_nr)
            msg = f_c[1]
            state2 = state2 and f_c[0]
        return [state1 or state2, msg]


gl_rule = 'abbbab'


def check_message2(r):
    global gl_rule
    if isinstance(rules[r], str):
        if gl_rule[0] != rules[r]:
            return False
        else:
            gl_rule = gl_rule[1:]
    elif isinstance(rules[r][0], int):
        for rule in rules[r]:
            if check_message(rule) is False:
                return False
    pass
    # nvm not good

valids = [""]

def generate_all_valid_messages():
    for rule in rules[0]:



with open("input19.txt", "r") as fp:
    for line in fp:
        if line != '\n':
            parse_rule(line)
        else:
            break
    for line in fp:
        line = line.strip()
        messages.append(line)

print(rules)

print(check_message2(0))
