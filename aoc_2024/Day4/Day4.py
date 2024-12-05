
#forward_letters = ['X', 'M', 'A', 'S']
#backward_letters = ['S', 'A', 'M', 'X']

#def update_count(letter, target_letters, index, result):
#    if letter == target_letters[index]:
#        index += 1
#        if (index >= len(target_letters)):
#            index = 0
#            result += 1
#    else:
#        index = 0
#    return index, result

#def update_both_count(letter, forward, backward, result):
#    forward, result = update_count(letter, forward_letters, forward, result)
#    backward, result = update_count(letter, backward_letters, backward, result)
#    return forward, backward, result

#def part_one(data: str):
#    result = 0
#    lines = data.splitlines()
#    line_count = len(lines)
#    length = len(lines[0])

#    forward = backward = 0
#    for y in range(line_count):
#        for x in range(length):
#            forward, backward, result = update_both_count(lines[y][x], forward, backward, result)
#        forward = backward = 0
        
#    print(f"Lines {result}")

#    forward = backward = 0    
#    for x in range(length):
#        for y in range(line_count):
#            forward, backward, result = update_both_count(lines[y][x], forward, backward, result)        
#        forward = backward = 0
    
#    print(f"Rows {result}")

#    forward = backward = 0    
#    for x in range(length):
#        for i in range(min(line_count, length - x)):
#            forward, backward, result = update_both_count(lines[i][x + i], forward, backward, result)
#        forward = backward = 0
    
#    print(f"Diagonal Lines Forward {result}")
    
#    forward = backward = 0    
#    for x in range(length):
#        for i in range(min(line_count, x + 1)):
#            forward, backward, result = update_both_count(lines[i][x - i], forward, backward, result)
#        forward = backward = 0
    
#    print(f"Diagonal Lines Backward {result}")

#    forward = backward = 0    
#    for y in range(1, line_count):
#        for i in range(min(length, line_count - y)):
#            forward, backward, result = update_both_count(lines[y + i][i], forward, backward, result)
#        forward = backward = 0
    
#    print(f"Diagonal Rows Forward {result}")
    
#    forward = backward = 0    
#    for y in range(1, line_count):
#        for i in range(min(length, y + 1)):
#            forward, backward, result = update_both_count(lines[y - i][i], forward, backward, result)
#        forward = backward = 0
    
#    print(f"Diagonal Rows Backward {result}")

#    return result

letters = ['M', 'A', 'S']
directions = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
cross = [(-1, -1), (1, -1), (1, 1), (-1, 1)]

def in_range(lines, x, y):
    return x >= 0 and y >= 0 and x < len(lines[0]) and y < len(lines)

def part_one(data: str):
    result = 0
    lines = data.splitlines()
    
    width = len(lines[0])
    height = len(lines)

    for y in range(height):
        for x in range(width):
            if (lines[y][x] != 'X'):
                continue
            for direction in directions:
                p_x = x
                p_y = y
                match = 0
                for letter in letters:
                    p_x += direction[0]
                    p_y += direction[1]
                    if in_range(lines, p_x, p_y) and lines[p_y][p_x] == letter:
                        match += 1
                if match == len(letters):
                    result += 1                

    return result


def part_two(data: str):
    result = 0
    lines = data.splitlines()
    
    width = len(lines[0])
    height = len(lines)

    for y in range(height):
        for x in range(width):
            if (lines[y][x] != 'A'):
                continue
            letters = ''
            for cross_dir in cross:
                p_x = x + cross_dir[0] 
                p_y = y + cross_dir[1]
                if in_range(lines, p_x, p_y):
                    letters += lines[p_y][p_x]
            if len(letters) != 4:
                continue

            for i in range(4):
                if letters == "MMSS":
                    result += 1
                    break
                letters = letters[1:] + letters[0]
                
    return result