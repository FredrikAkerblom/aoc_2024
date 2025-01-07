

directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]


def in_range(x, y, width, height):
    return 0 <= x < width and 0 <= y < height


def part_one(data: str):
    result = 0
    lines = data.splitlines()
    width = len(lines[0])
    height = len(lines)
    
    grid = []
    trailheads = []
    for y in range(height):
        row = []
        for x in range(width):
            row.append(int(lines[y][x]))
            if lines[y][x] == '0':
                trailheads.append((x, y))
        grid.append(row)
        
    for start in trailheads:
        visited = set()
        search_space = { start }
        current_height = 0
        while current_height < 9 and len(search_space) > 0:
            current_height += 1
            new_search_space = set()
            for space in search_space:
                for direction in directions:
                    x = space[0] + direction[0]
                    y = space[1] + direction[1]
                    if in_range(x, y, width, height) and grid[y][x] == current_height:
                        new_search_space.add((x, y))
            search_space = new_search_space
        result += len(search_space)
    return result


def part_two(data: str):
    result = 0
    lines = data.splitlines()
    width = len(lines[0])
    height = len(lines)
    
    grid = []
    trailheads = []
    for y in range(height):
        row = []
        for x in range(width):
            row.append(int(lines[y][x]))
            if lines[y][x] == '0':
                trailheads.append((x, y))
        grid.append(row)
        
    for start in trailheads:
        visited = set()
        search_space = [ start ]
        current_height = 0
        while current_height < 9 and len(search_space) > 0:
            current_height += 1
            new_search_space = []
            for space in search_space:
                for direction in directions:
                    x = space[0] + direction[0]
                    y = space[1] + direction[1]
                    if in_range(x, y, width, height) and grid[y][x] == current_height:
                        new_search_space.append((x, y))
            search_space = new_search_space
        result += len(search_space)
    return result