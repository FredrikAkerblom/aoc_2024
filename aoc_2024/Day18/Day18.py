Directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def parse_grid(lines, max_read_range):
    if len(lines) < 100:
        width, height = 7, 7
    else:
        width, height = 71, 71

    grid = []
    for y in range(height):
        row = []
        for x in range(width):
            row.append(True)
        grid.append(row)

    for i in range(min(max_read_range, len(lines))):
        sx, div, sy = lines[i].partition(',')
        x, y = int(sx), int(sy)
        grid[y][x] = False
    return grid


def print_grid(grid, visited):
    width, height = len(grid[0]), len(grid)
    for y in range(height):
        line = ""
        for x in range(width):
            if (x, y) in visited:
                line += 'X'
            else:
                line += '.' if grid[y][x] else '#'
        print(line)


def find_path(grid):
    width, height = len(grid[0]), len(grid)
    #print_grid(grid, set())
    search_space = [(0, 0, [])]
    visited = {(0, 0)}
    target_x, target_y = width - 1, height - 1
    while len(search_space) > 0:
        tile = search_space.pop(0)
        for d in Directions:
            x, y, path = tile[0] + d[0], tile[1] + d[1], list(tile[2])
            path.append((x, y))
            if x == target_x and y == target_y:
                return path
            if x < 0 or x >= width or y < 0 or y >= height or not grid[y][x]:
                continue
            coord = (x, y)
            if coord in visited:
                continue
            visited.add(coord)
            search_space.append((x, y, path))
    #print_grid(grid, visited)
    return None


def part_one(data: str):
    lines = data.splitlines()
    line_count = 12 if len(lines) < 100 else 1024;
    grid = parse_grid(lines, line_count)
    return len(find_path(grid))


def part_two(data: str):
    lines = data.splitlines()
    line_count = 12 if len(lines) < 100 else 1024;
    grid = parse_grid(lines, line_count)
    path = find_path(grid)
    while path != None:
        sx, div, sy = lines[line_count].partition(',')
        x, y = int(sx), int(sy)
        grid[y][x] = False
        line_count += 1
        if (x, y) in path:
            path = find_path(grid)
    return f"{x},{y}"