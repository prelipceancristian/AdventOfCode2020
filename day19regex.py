import re

def parse_input():
    rules = {}
    with open("input19.txt", "r") as fp:
        for line in fp:
            if line == "\n":
                break
            rule_id, options = line.split(": ")
            rule_id = int(rule_id)

            if '"' in options:
                rule = options[1]
            else:
                rule = []
                for option in options.split("| "):
                    rule.append(tuple(map(int, option.split())))

            rules[rule_id] = rule

    return rules


def build_regexp(rules, rule=0):
    rule = rules[rule]
    if type(rule) is str:
        return rule
    options = []
    for option in rule:
        r = ''
        for sub_rule in option:
            r += build_regexp(rules, sub_rule)
        options.append(r)
    return '(' + '|'.join(options) + ')'


rules = parse_input()
rexp = re.compile('^' + build_regexp(rules) + '$')
valid = 0

with open("input19.txt", "r") as fp:
    for line in fp:
        if rexp.match(line):
            valid += 1
print(rules)
print(valid)

# rules[8] = [(42), (42, 8)]
# rules[11] = [(42, 31), (42, 11, 31)]
