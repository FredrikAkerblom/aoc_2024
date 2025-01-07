patterns = dict() # pattern_string:potential_count

def recursive_search(current: str, target: str, parts):
    remaining = target[len(current):]
    if remaining in patterns:
        return patterns[remaining]

    count = 0
    for part in parts:
        potential = current + part
        if potential == target:
            count += 1
        elif target.startswith(potential):
            count += recursive_search(potential, target, parts)
    patterns[remaining] = count
    return count


def search(target, parts):
    search_space = [""]
    while len(search_space) > 0:
        current = search_space.pop(0)
        for part in parts:
            potential = current + part
            if potential == target:
                return True
            if target.startswith(potential):
                search_space.append(potential)
    return False


def reduce_parts(parts):
    parts = sorted(parts, key=lambda x: -len(x))
    i = 0
    while i < len(parts):
        if search(parts[i], parts[i+1:]):
            parts.pop(i)
            i -= 1
        i += 1
    return parts


def part_one(data: str):
    data_split = data.split("\n\n")
    parts = data_split[0].split(", ")
    targets = data_split[1].splitlines()
    
    parts = reduce_parts(parts)
    result = 0
    for target in targets:
        if recursive_search("", target, parts) > 0:
            result += 1            
    return result


def part_two(data: str):
    data_split = data.split("\n\n")
    parts = data_split[0].split(", ")
    targets = data_split[1].splitlines()
    
    result = 0
    for target in targets:
        result += recursive_search("", target, parts)
    return result