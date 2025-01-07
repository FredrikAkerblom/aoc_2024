directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]

def is_fit(lock, key):
    for i in range(len(lock)):
        if lock[i] + key[i] > 5:
            return False
    return True


def parse_keys_and_locks(data: str):
    entries = data.split("\n\n")
    keys = []
    locks = []
    for entry in entries:
        lines = entry.splitlines()
        heights = []
        for x in range(len(lines[0])):
            height = 0
            for y in range(len(lines)):
                if lines[y][x] == '#':
                    height += 1
            heights.append(height - 1)
        if '#' in lines[0]:
            locks.append(heights)
        else:
            keys.append(heights)
    return keys, locks

def part_one(data: str):
    keys, locks = parse_keys_and_locks(data)
    result = 0
    for lock in locks:
        for key in keys:
            if is_fit(lock, key):
                result += 1
    return result

def part_two(data: str):
    return "Merry Christmas"