questionnaire = [0] * 26
counter = 0
no_of_members = 0

with open("input6.txt", "r") as fp:
    for line in fp:
        if line not in ['\n', '\r\n']:
            no_of_members += 1
            for letter in line.replace('\n', ''):
                questionnaire[ord(letter) - ord('a')] += 1
        else:
            counter += len(list(filter(lambda x: x == no_of_members, questionnaire)))
            questionnaire = [0 for _ in range(26)]
            no_of_members = 0

counter += len(list(filter(lambda x: x == no_of_members, questionnaire)))

print(counter)
