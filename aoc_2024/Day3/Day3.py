import re

def part_one(data: str):
    result = 0

    pattern = r"mul\(\d{1,3},\d{1,3}\)"
    matches = re.findall(pattern, data)
    
    for entry in matches:
        x, sep, y = entry[4:-1].partition(",")
        result += int(x) * int(y)
    return result


def part_two(data: str):
    result = 0

    pattern = r"do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\)"
    matches = re.findall(pattern, data)
    is_enabled = True
    
    for entry in matches:
        if entry == "do()":
            is_enabled = True
        elif entry == "don't()":
            is_enabled = False
        elif is_enabled:
            x, sep, y = entry[4:-1].partition(",")
            result += int(x) * int(y)
    return result