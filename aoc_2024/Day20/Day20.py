directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
cheats = [(0, -2), (-2, 0), (0, 2), (2, 0)]

# class Point:
#     def __init__(self, x, y, path_length):
#         self.x = x
#         self.y = y
#         self.path_length = -1


def parse_grid(data: str):
    lines = data.splitlines()
    grid = []
    width, height = len(lines[0]), len(lines)
    for y in range(height):
        row = []
        for x in range(width):
            c = lines[y][x]
            if c == '.':
                row.append(-1)
            elif c == 'S':
                row.append(-1)
                start = (x, y)
            elif c == 'E':
                row.append(-1)
                end = (x, y)
            else:
                row.append(None)
        grid.append(row)
    return grid, start, end


def explore_grid(grid, start, end):
    width, height = len(grid[0]), len(grid)
    search_space = [end]
    grid[end[1]][end[0]] = 0
    while len(search_space) > 0:
        tile = search_space.pop(0)
        distance = grid[tile[1]][tile[0]]
        for d in directions:
            x = tile[0] + d[0]
            y = tile[1] + d[1]
            if 0 <= x < width and 0 <= y < height and grid[y][x] == -1:
                grid[y][x] = distance + 1
                search_space.append((x, y))
    print(f"Path length: {grid[start[1]][start[0]]}")


def find_cheats_short(grid):
    width, height = len(grid[0]), len(grid)
    results = dict()
    for iy in range(height):
        for ix in range(width):
            if grid[iy][ix] == None:
                continue
            dist = grid[iy][ix]
            for c in cheats:
                x = ix + c[0]
                y = iy + c[1]
                if 0 <= x < width and 0 <= y < height and grid[y][x] != None:
                    skip = dist - grid[y][x] - 2
                    if skip > 0:
                        results[skip] = results.get(skip, 0) + 1
    return results


def find_cheats_long(grid):
    width, height = len(grid[0]), len(grid)
    results = dict()
    for iy in range(height):
        for ix in range(width):
            if grid[iy][ix] == None:
                continue
            dist = grid[iy][ix]
            for cy in range(-20, 21):
                for cx in range(-20, 21):
                    x = ix + cx
                    y = iy + cy
                    length = abs(cy) + abs(cx)
                    if length > 20:
                        continue
                    if 0 <= x < width and 0 <= y < height and grid[y][x] != None:
                        skip = (dist - grid[y][x]) - length
                        if skip > 0:
                            results[skip] = results.get(skip, 0) + 1
    return results


def part_one(data: str):
    grid, start, end = parse_grid(data)
    explore_grid(grid, start, end)
    found_cheats = find_cheats_short(grid)
    result = 0
    for key in sorted(found_cheats.keys()):
        # print(f"{key}: {found_cheats[key]}")
        if key >= 100:
            result += found_cheats[key]
    return result


def part_two(data: str):
    grid, start, end = parse_grid(data)
    explore_grid(grid, start, end)
    found_cheats = find_cheats_long(grid)
    result = 0
    for key in sorted(found_cheats.keys()):
        print(f"{key}: {found_cheats[key]}")
        if key >= 100:
            result += found_cheats[key]
    return result