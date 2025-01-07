
directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]


def part_one(data: str):
    result = 0
    lines = data.splitlines()
    width = len(lines[0])
    height = len(lines)
    visited = set()

    for y in range(height):
        for x in range(width):
            if (x, y) in visited:
                continue
            c = lines[y][x]
            space = [(x, y)]
            visited.add((x, y))
            area = 0
            perimiter = 0
            while len(space) > 0:
                current = space[0]
                space.remove(current)
                area += 1
                for direction in directions:
                    xd = current[0] + direction[0]
                    yd = current[1] + direction[1]
                    if xd < 0 or xd >= width or yd < 0 or yd >= height or lines[yd][xd] != c:
                        perimiter += 1
                    elif (xd, yd) not in visited:
                        visited.add((xd, yd))
                        space.append((xd, yd))
            result += area * perimiter

    return result


def part_two(data: str):
    result = 0
    lines = data.splitlines()
    width = len(lines[0])
    height = len(lines)
    visited = set()

    for y in range(height):
        for x in range(width):
            if (x, y) in visited:
                continue
            c = lines[y][x]
            search_space = [(x, y)]
            visited.add((x, y))
            region = [(x, y)]
            area = 0
            edge_tiles = []
            start_x = width + 1
            start_y = height + 1
            while len(search_space) > 0:
                current = search_space[0]
                search_space.remove(current)
                area += 1
                for direction in directions:
                    xd = current[0] + direction[0]
                    yd = current[1] + direction[1]
                    if xd < 0 or xd >= width or yd < 0 or yd >= height or lines[yd][xd] != c:
                        if not current in edge_tiles:
                            edge_tiles.append(current)
                        if yd < start_y or (yd == start_y and xd < start_x):
                            start_x = xd
                            start_y = yd
                    elif (xd, yd) not in visited:
                        visited.add((xd, yd))
                        search_space.append((xd, yd))
                        region.append((xd, yd))

            wall_count = 0
            
            # Go over each tile in the region, if they have a wall in a direction follow that wall and mark all tiles facing that direction as seen
            seen = set()
            for tile in region:
                for d in range(len(directions)):
                    direction = directions[d]
                    check = directions[(d + 1) % len(directions)]
                    tx = tile[0]
                    ty = tile[1]
                    if (tx, ty, direction) in seen:
                        continue
                    if (tx + check[0], ty + check[1]) not in region:
                        wall_count += 1
                        while (tx + check[0], ty + check[1]) not in region and (tx, ty) in region:
                            seen.add((tx, ty, direction))
                            tx += direction[0]
                            ty += direction[1]
                        tx -= direction[0]
                        ty -= direction[1]
                        while (tx + check[0], ty + check[1]) not in region and (tx, ty) in region:
                            seen.add((tx, ty, direction))
                            tx -= direction[0]
                            ty -= direction[1]
                        tx += direction[0]
                        ty += direction[1]

            result += area * wall_count
    return result