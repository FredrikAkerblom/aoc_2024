from functools import cmp_to_key

def parse_rules(data):    
    rules = {}
    for rule in data.splitlines():
        a_data, b_data = rule.split('|')
        a = int(a_data)
        b = int(b_data)        
        if b not in rules:
            rules[b] = {a}
        else:
            rules[b].add(a)
    return rules


def is_ordered(rules, numbers):    
    is_valid = True
    for i in range(len(numbers)):
        current = numbers[i]
        if current in rules:
            remaining = set(numbers[i:])
            if rules[current].intersection(remaining):
                is_valid = False
                break
    return is_valid


rules = {}
def sort_by_rules(a, b):
    if a in rules and b in rules[a]:
        return 1
    if b in rules and a in rules[b]:
        return -1
    return 0


def part_one(data: str):
    result = 0
    rule_data, task_data = data.split("\n\n")
    rules = parse_rules(rule_data)

    for task in task_data.splitlines():
        numbers = [int(num) for num in task.split(',')]
        if is_ordered(rules, numbers):
            result += numbers[len(numbers) // 2]

    return result


def part_two(data: str):
    result = 0
    rule_data, task_data = data.split("\n\n")
    global rules
    rules = parse_rules(rule_data)

    for task in task_data.splitlines():
        numbers = [int(num) for num in task.split(',')]
        if is_ordered(rules, numbers):
            continue
        numbers = sorted(numbers, key=cmp_to_key(sort_by_rules))
        result += numbers[len(numbers) // 2]

    return result