directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]


keypad = {  '7': (0, 0),
            '8': (1, 0),
            '9': (2, 0),
            '4': (0, 1),
            '5': (1, 1),
            '6': (2, 1),
            '1': (0, 2),
            '2': (1, 2),
            '3': (2, 2),
            ' ': (0, 3),
            '0': (1, 3),
            'A': (2, 3)
         }

arrowpad = { ' ': (0, 0),
             '^': (1, 0),
             'A': (2, 0),
             '<': (0, 1),
             'v': (1, 1),
             '>': (2, 1)
           }


def map_sequence(step_map, sequence: str, steps: int):
    x, y = step_map['A'] # Start point
    fx, fy = step_map[' '] # Forbidden point
    path = dict()
    for target in sequence:
        tx, ty = step_map[target] # Target point
        # Path should be flipped if the forbidden point aligns
        flip_path = (tx == fx and y == fy) or (ty == fy and x == fx)
        move = (tx - x, ty - y, flip_path)
        path[move] = path.get(move, 0) + steps
        x, y = tx, ty
    return path


def build_sequence(x: int, y: int, flip_path: bool):
    sequence = ""
    for _ in range(-x): sequence += '<'
    for _ in range(y):  sequence += 'v'
    for _ in range(-y): sequence += '^'
    for _ in range(x):  sequence += '>'    
    if flip_path:
        sequence = sequence[::-1]
    sequence += 'A'
    return sequence


def solve(data: str, robot_count: int):
    lines = data.splitlines()
    result = 0
    for line in lines:
        path = map_sequence(keypad, line, 1)
        for i in range(robot_count + 1):
            new_path = dict()
            seq_output = ""
            for (x, y, flip_path), steps in path.items():
                sequence = build_sequence(x, y, flip_path)
                seq_output += sequence
                map_result = map_sequence(arrowpad, sequence, path[(x, y, flip_path)])
                for key, step_count in map_result.items():
                    new_path[key] = new_path.get(key, 0) + step_count
            # print(seq_output)
            path = new_path
            
        code_value = int(line[:3])
        path_step_count = 0
        for (x, y, flip_path), steps in path.items():
            path_step_count += steps
        complexity = path_step_count * code_value
        print(f"Code: {line}, Steps: {path_step_count}, Num: {code_value}, Complexity: {complexity}")
        result += complexity
                    
    return result
    

def part_one(data: str):
    return solve(data, 2)


def part_two(data: str):
    return solve(data, 25)