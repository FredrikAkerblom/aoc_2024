def evaluate(numbers, target, include_concatenation):
    possibles = set([target])
    new_possibles = set()
    for i in range(len(numbers)):
        n = len(numbers) - i - 1
        number = numbers[n]
        for potential in possibles:
            # Multiplication
            if potential % number == 0:
                new_possibles.add(potential // number)
            
            # Addition
            if potential - number >= 0:
                new_possibles.add(potential - number)
            
            if include_concatenation:
                # Concatenation
                number_str = str(number)
                potential_str = str(potential)
                if len(potential_str) > len(number_str) and potential_str.endswith(number_str):
                    new_possibles.add(int(potential_str[:-len(number_str)]))
        possibles.clear()
        possibles = set(new_possibles)
        new_possibles.clear()
    return 0 in possibles


def solve(data: str, include_concatenation: bool):
    result = 0
    lines = data.splitlines()
    
    for line in lines:
        target_data, number_data = line.split(':')
        target = int(target_data)
        numbers = list(map(int, number_data.strip().split(' ')))
        if evaluate(numbers, target, include_concatenation):
            result += target
    return result


def part_one(data: str):
    return solve(data, False)


def part_two(data: str):
    return solve(data, True)