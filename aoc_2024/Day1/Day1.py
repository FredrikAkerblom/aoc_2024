
def part_one(data: str):
    left = []
    right = []
    lines = data.splitlines()
    
    for line in lines:
        a, sep, b = line.partition("   ")
        left.append(a)
        right.append(b)
        
    left.sort()
    right.sort()
    result = 0    

    for i in range(len(left)):
        result += abs(int(left[i]) - int(right[i]))
            
    return result


def part_two(data: str):
    left = []
    locations = {}
    lines = data.splitlines()
    
    for line in lines:
        a, sep, b = line.partition("   ")
        left.append(a)
        locations[b] = locations.setdefault(b, 0) + 1
    
    result = 0
    
    for entry in left:
        result += int(entry) * locations.get(entry, 0)

    return result
        