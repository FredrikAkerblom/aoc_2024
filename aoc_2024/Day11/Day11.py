def update_simple(values):
    result = []
    for value in values:
        if value == '0':
            result.append('1')
        elif len(value) % 2 == 0:
            mid = len(value) // 2
            result.append(value[:mid])
            result.append(str(int(value[mid:])))
        else:
            result.append(str(int(value) * 2024))
    return result

def update_value(value):
    result = []
    if value == '0':
        result.append('1')
    elif len(value) % 2 == 0:
        mid = len(value) // 2
        result.append(value[:mid])
        result.append(str(int(value[mid:])))
    else:
        result.append(str(int(value) * 2024))
    return result    

step_map = { }
def count_after_steps(value, step):
    if step == 0:
        return 1
    if (value, step) in step_map:
        return step_map[(value, step)]
    
    updated_values = update_value(value)
    result = 0
    for entry in updated_values:
        result += count_after_steps(entry, step - 1)        
    step_map[(value, step)] = result
    return result

def part_one(data: str):
    values = data.split(' ')
    result = 0
    for value in values:
        result += count_after_steps(value, 25)
    return result


def part_two(data: str):
    values = data.split(' ')
    result = 0
    for value in values:
        result += count_after_steps(value, 75)
    return result