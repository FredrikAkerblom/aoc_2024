Empty = 0
Wall = 1
Box = 2
BoxR = 3
directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]


def parse_map(data: str, scale_up:bool):
    lines = data.splitlines()
    width = len(lines[0])
    height = len(lines)
    grid = []
    for y in range(height):
        row = []
        for x in range(width):
            c = lines[y][x]
            if c == '#':
                row.append(Wall)
                if scale_up:
                    row.append(Wall)
            elif c == 'O':
                row.append(Box)
                if scale_up:
                    row.append(BoxR)
            elif c == '@':
                robot_x = x
                robot_y = y
                row.append(Empty)
                if scale_up:
                    robot_x *= 2
                    row.append(Empty)
            else:
                row.append(Empty)
                if scale_up:
                    row.append(Empty)
        grid.append(row)    
    return grid, robot_x, robot_y


def parse_instructions(data: str):
    data = data.replace('\n', '')
    instructions = []
    for c in data:
        if c == '<':
            instructions.append(directions[1])
        elif c == '^':
            instructions.append(directions[0])
        elif c == '>':
            instructions.append(directions[3])
        elif c == 'v':
            instructions.append(directions[2])
        else:
            print(f"Unhandled instruction: {c}")
    return instructions


def print_grid(grid, robot_x, robot_y, is_large):
    width, height = len(grid[0]), len(grid)
    for y in range(height):
        row = ""
        for x in range(width):
            c = grid[y][x]
            if (x == robot_x and y == robot_y):
                row += '@'
            elif c == Box:
                row += ('O' if not is_large else '[')
            elif c == BoxR:
                row += ']'
            elif c == Wall:
                row += '#'
            else:
                row += '.'
        print(row)
    print()
    

def calculate_score(grid):
    result = 0
    width, height = len(grid[0]), len(grid)
    for y in range(height):
        for x in range(width):
            if grid[y][x] == Box:
                result += y * 100 + x
    return result
    

def part_one(data: str):
    parts = data.split("\n\n")
    grid, x, y = parse_map(parts[0], False)
    instructions = parse_instructions(parts[1])
    width, height = len(grid[0]), len(grid)
    # print_grid(grid, x, y, False)
    for move in instructions:
        cx, cy = x, y
        has_open = False
        while not has_open and grid[cy][cx] != Wall:
            cx += move[0]
            cy += move[1]
            has_open = grid[cy][cx] == Empty
        if not has_open:
            continue
        while cx != x or cy != y:
            grid[cy][cx] = grid[cy - move[1]][cx - move[0]]
            cx -= move[0]
            cy -= move[1]
        x += move[0]
        y += move[1]
        # print_grid(grid, x, y, False)
    
    return calculate_score(grid)


def part_two(data: str):
    parts = data.split("\n\n")
    grid, x, y = parse_map(parts[0], True)
    instructions = parse_instructions(parts[1])
    width, height = len(grid[0]), len(grid)
    # print_grid(grid, x, y, True)
    step = 0
    for move in instructions:
        cx, cy = x, y
        has_open = False
        step += 1
        if move[1] == 0:
            while not has_open and grid[cy][cx] != Wall:
                cx += move[0]
                cy += move[1]
                has_open = grid[cy][cx] == Empty
            if not has_open:
                continue
            while cx != x or cy != y:
                grid[cy][cx] = grid[cy - move[1]][cx - move[0]]
                cx -= move[0]
                cy -= move[1]
        else:
            has_open = False
            has_wall = False
            x_layout = [ {cx} ]
            
            while not has_open and not has_wall:
                cy += move[1]                
                has_open = True
                next_layout = set()
                for sx in x_layout[-1]:
                    c = grid[cy][sx]
                    if c != Empty:
                        has_open = False
                    if c == Wall:
                        has_wall = True
                        break
                    if c == Box:
                        next_layout.add(sx)
                        next_layout.add(sx + 1)
                    elif c == BoxR:
                        next_layout.add(sx)
                        next_layout.add(sx - 1)
                if len(next_layout) > 0:
                    x_layout.append(next_layout)
            if not has_open:
                continue
            
            while cy != y:
                layout = x_layout.pop()
                for sx in layout:
                    grid[cy][sx] = grid[cy - move[1]][sx]
                    grid[cy - move[1]][sx] = Empty
                cy -= move[1]
                
        x += move[0]
        y += move[1]
    # print_grid(grid, x, y, True)
    return calculate_score(grid)