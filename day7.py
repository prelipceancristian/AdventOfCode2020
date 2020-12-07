master_dict = {}
bags_state = {}


def parse_line(my_line):
    s = my_line.replace("bags", "")
    s = s.replace("bag", "")  # remove the words bags and bag
    s = s.replace("\n", "")
    s = s.replace(".", "")
    s = s.split("contain")
    s[1] = s[1].split(",")
    bag_dict = {}  # the type and number of bags necessary for the current bag
    if s[1][0].count("no other") == 0:  # keep the dictionary empty if there are no other bags that need to be contained
        for bag in s[1]:
            bag_dict[bag[3:].strip()] = int(bag[:2])
    master_dict[s[0].strip()] = bag_dict
    bags_state[s[0].strip()] = 0  # default value for the overall bags_state, as it is unknown whether it will or will
    # not contain the searched bag


def bags_that_contain(searched):
    """
    Gets the number of bags that contain a given bag.
    :param searched: the name of the searched bag
    :return: the number of apparitions
    """
    counter = 0
    for bag in master_dict:
        if is_bag_valid(bag, searched) == 1:
            counter += 1
    return counter


def is_bag_valid(bag_name, searched):
    """
    Check whether a bag contains a searched bag.
    The function also sets the global parameter bags_state which prevents solving a subproblem multiple times
    :param bag_name: the bag in which to search
    :param searched: the searched bag
    :return: 1 if the bag contains the searched bag, -1 otherwise
    """
    if bags_state[bag_name] != 0:
        return True if bags_state[bag_name] == 1 else False  # if the answer is already known in the memoization dictionary, use it directly
    if master_dict[bag_name] == {}:
        bags_state[bag_name] = -1  # if the bag does not contain any other bags, it is certain that it does not contain
        # the searched bag
        return False
    if searched in master_dict[bag_name]:
        bags_state[bag_name] = 1  # if the searched bag is directly contained in the current one, than it is a valid bag
        return True
    for bag in master_dict[bag_name]:  # if everything fails, a deeper search must be done in a similar fashion,
        # as we are looking for at least one bag that contains the searched one
        if is_bag_valid(bag, searched) == 1:
            bags_state[bag_name] = 1
            return True
    bags_state[bag_name] = -1
    return False


def bags_inside(bag_name, original_search="shiny gold"):
    """
    Determine the number of bags inside a certain given bag
    :param bag_name: the given bag
    :param original_search: the name of the original bag from the first function call
    :return: the number of bags contained in the bag named bag_name
    """
    s = 0
    for bag in master_dict[bag_name]:
        s += bags_inside(bag, original_search) * master_dict[bag_name][bag]
    s += 1  # the bags themselves count towards the total
    if bag_name == original_search:
        return s - 1  # on reaching the first function call, 1 must be subtracted as not to count the original search
        # bag towards the final answer
    return s


with open("input7.txt", "r") as fp:
    for line in fp:
        parse_line(line)

print(bags_that_contain("shiny gold"))
print(bags_inside("shiny gold"))
