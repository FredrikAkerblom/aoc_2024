def build_antenna_map(lines):
    width = len(lines[0])
    height = len(lines)    
    antenna_map = {}

    for y in range(height):
        for x in range(width):
            symbol = lines[y][x]
            if symbol == '.':
                continue
            if symbol not in antenna_map:
                antenna_map[symbol] = []
            antenna_map[symbol].append((x, y))
    return antenna_map


def in_range(x, y, width, height):
    return 0 <= x < width and 0 <= y < height


def part_one(data: str):
    lines = data.splitlines()
    width = len(lines[0])
    height = len(lines)
    
    antenna_map = build_antenna_map(lines)
    
    antinodes = set()
    for symbol in antenna_map:
        antennas = antenna_map[symbol]
        for i in range(len(antennas)):
            for j in range(len(antennas)):
                if i == j:
                    continue
                x = antennas[i][0] + (antennas[i][0] - antennas[j][0])
                y = antennas[i][1] + (antennas[i][1] - antennas[j][1])
                if in_range(x, y, width, height):
                    antinodes.add((x, y))
                
    return len(antinodes)


def part_two(data: str):
    lines = data.splitlines()
    width = len(lines[0])
    height = len(lines)
    
    antenna_map = build_antenna_map(lines)
    
    antinodes = set()
    for symbol in antenna_map:
        antennas = antenna_map[symbol]
        for i in range(len(antennas)):
            for j in range(len(antennas)):
                if i == j:
                    continue
                x, y = antennas[i][0], antennas[i][1]
                dx = antennas[i][0] - antennas[j][0]
                dy = antennas[i][1] - antennas[j][1]
                while in_range(x, y, width, height):
                    antinodes.add((x, y))
                    x += dx
                    y += dy
                
    return len(antinodes)