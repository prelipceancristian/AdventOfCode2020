parsed_data = {}
counter = 0


def check_parsed_data():
    try:
        for attribute in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]:
            _ = parsed_data[attribute]
            parsed_data[attribute].replace('\n', '')
        assert (1920 <= int(parsed_data["byr"]) <= 2002)
        assert (2010 <= int(parsed_data["iyr"]) <= 2020)
        assert (2020 <= int(parsed_data["eyr"]) <= 2030)
        if parsed_data["hgt"].count("cm") == 1:
            assert (150 <= int(parsed_data["hgt"][0:3]) <= 193)
        else:
            assert (59 <= int(parsed_data["hgt"][0:2]) <= 76)
        assert (parsed_data["hcl"][0] == "#")
        for xx in range(1, 7):
            assert ('a' <= parsed_data["hcl"][xx] <= 'f' or '0' <= parsed_data["hcl"][xx] <= '9')
        assert (parsed_data["ecl"].replace("\n", '') in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"])
        assert (len(parsed_data["pid"].replace("\n", '')) == 9 and parsed_data["pid"].replace('\n', '').isdecimal())
        return True
    except Exception:
        return False


with open("input4.txt", "r") as fp:
    for line in fp:
        if line not in ['\n', '\r\n']:
            args = line.split(" ")
            for x in args:
                elems = x.split(":")
                parsed_data[elems[0]] = elems[1]
        else:
            if check_parsed_data():
                counter += 1
            parsed_data.clear()

if check_parsed_data():
    counter += 1
parsed_data.clear()

print(counter)
