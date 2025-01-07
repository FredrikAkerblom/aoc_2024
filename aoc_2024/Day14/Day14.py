def print_grid(px, py, width, height):
    positions = {}
    center_x = (width // 2)
    center_y = (height // 2)
    for i in range(len(px)):
        positions[(px[i], py[i])] = positions.get((px[i], py[i]), 0) + 1
    
    for y in range(height):
        line = ""
        for x in range(width):
            # if x == center_x or y == center_y:
            #     line += ' '
            #     continue
            if (x, y) in positions:
                line += str(positions[(x, y)])
            else:
                line += '.'
        print(line)


def has_many_adjacent(px, py, width):
    space = set()
    for i in range(len(px)):
        space.add((px[i], py[i]))
    for tile in space:
        line_length = 0
        for x in range(tile[0], width):
            if (x, tile[1]) in space and (x, tile[1] - 1) in space and (x, tile[1] + 1) in space:
                line_length += 1
                if line_length > 5:
                    return True
            else:
                break
    return False


def part_one(data: str):
    lines = data.splitlines()
    if len(lines) < 15:
        width = 11
        height = 7
    else:
        width = 101
        height = 103
    
    px, py, vx, vy = [], [], [], []
    for line in lines:
        parts = line.split(' ')
        parts[0] = parts[0][2:]
        parts[1] = parts[1][2:]
        spx, div, spy = parts[0].partition(',')
        svx, div, svy = parts[1].partition(',')
        px.append(int(spx))
        py.append(int(spy))
        vx.append(int(svx))
        vy.append(int(svy))
        
    center_x = (width // 2)
    center_y = (height // 2)
    quadrants = [0, 0, 0, 0]
    
    for i in range(len(lines)):
        px[i] = (px[i] + vx[i] * 100) % width
        py[i] = (py[i] + vy[i] * 100) % height
        if px[i] == center_x or py[i] == center_y:
            continue
        x = 0 if px[i] < center_x else 1
        y = 0 if py[i] < center_y else 2
        quadrants[x + y] += 1
        # print(f"({px[i]}, {py[i]})")
    # print_grid(px, py, width, height)
    return quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3]


def part_two(data: str):
    lines = data.splitlines()
    if len(lines) < 15:
        return "Not applicable"
    else:
        width = 101
        height = 103
    
    px, py, vx, vy = [], [], [], []
    for line in lines:
        parts = line.split(' ')
        parts[0] = parts[0][2:]
        parts[1] = parts[1][2:]
        spx, div, spy = parts[0].partition(',')
        svx, div, svy = parts[1].partition(',')
        px.append(int(spx))
        py.append(int(spy))
        vx.append(int(svx))
        vy.append(int(svy))
        
    center_x = (width // 2)
    center_y = (height // 2)
        
    step = 0
    while True:
        step += 1
        for i in range(len(lines)):
            px[i] = (px[i] + vx[i]) % width
            py[i] = (py[i] + vy[i]) % height
        if has_many_adjacent(px, py, width):
            # print_grid(px, py, width, height)
            # print(f"Step: {step}")
            # input()
            return step