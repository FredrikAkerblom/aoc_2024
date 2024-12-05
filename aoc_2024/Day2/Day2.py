
def check_report(data):    
    direction = 0
    is_safe = True
    for i in range(len(data) - 1):
        a = int(data[i])
        b = int(data[i + 1])
        diff = b - a

        if (diff == 0) or (abs(diff) > 3):
            is_safe = False
            break
        if direction == 0:
            direction = 1 if diff > 0 else -1
        if (diff > 0) != (direction > 0):
            is_safe = False
            break
    return is_safe

def part_one(data: str):
    result = 0
    lines = data.splitlines()
    
    for line in lines:
        levels = line.split(" ")

        if check_report(levels):
            result += 1

    return result


def part_two(data: str):
    result = 0
    lines = data.splitlines()
    
    for line in lines:
        levels = line.split(" ")
        for i in range(len(levels)):
            if check_report(levels[:i] + levels[i+1:]):
                result += 1
                break

    return result