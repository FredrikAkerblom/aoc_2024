import re

def cramers_rule_solve(ax, ay, bx, by, tx, ty):
    determinant = ax * by - ay * bx
    if determinant == 0:
        return None

    # Cramer's rule
    a = tx * by - ty * bx
    b = ty * ax - tx * ay

    # Check if the solutions are integers
    if a % determinant == 0 and b % determinant == 0:
        a = a // determinant
        b = b // determinant
        return a * 3 + b
    else:
        return None


def part_one(data: str):
    result = 0
    entries = data.split("\n\n")
    
    for entry in entries:
        lines = entry.splitlines()
        numbers = re.findall(r'\d+', lines[0])
        ax, ay = int(numbers[0]), int(numbers[1])
        
        numbers = re.findall(r'\d+', lines[1])
        bx, by = int(numbers[0]), int(numbers[1])
        
        numbers = re.findall(r'\d+', lines[2])
        tx, ty = int(numbers[0]), int(numbers[1])
        
        answer = cramers_rule_solve(ax, ay, bx, by, tx, ty)
        if answer != None:
            result += answer
    return result


def part_two(data: str):
    result = 0
    entries = data.split("\n\n")
    
    for entry in entries:
        lines = entry.splitlines()
        numbers = re.findall(r'\d+', lines[0])
        ax, ay = int(numbers[0]), int(numbers[1])
        
        numbers = re.findall(r'\d+', lines[1])
        bx, by = int(numbers[0]), int(numbers[1])
        
        numbers = re.findall(r'\d+', lines[2])
        tx, ty = int(numbers[0]) + 10000000000000, int(numbers[1]) + 10000000000000
        
        answer = cramers_rule_solve(ax, ay, bx, by, tx, ty)
        
        if answer != None:
            result += answer
    return result