directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]

def parse_computers(data: str, include_self: bool):
    lines = data.splitlines()
    computers = {}
    for line in lines:
        a, b = line.split('-')
        if a not in computers:
            computers[a] = set()
        computers[a].add(b)
        if b not in computers:
            computers[b] = set()
        computers[b].add(a)
    if include_self:
        for computer in computers:
            computers[computer].add(computer)
    return computers


def part_one(data: str):
    computers = parse_computers(data, False)
    t_circles = set()
    for computer, connections in computers.items():
        if not computer.startswith('t'):
            continue
        for other_computer in connections:
            overlaps = computers[other_computer] & connections
            for overlap in overlaps:
                circle = tuple(sorted([computer, other_computer, overlap]))
                t_circles.add(circle)
    return len(t_circles)


def part_two(data: str):
    computers = parse_computers(data, True)
    circles = set()
    for computer, connections in computers.items():
        explore = list(connections)
        for i in range(len(explore)):
            overlap = set(connections)
            for j in range(len(explore)):
                other_computer = explore[(i + j) % len(explore)]
                if other_computer in overlap:
                    overlap &= computers[other_computer]
            circles.add(tuple(sorted(overlap)))
            
    sorted_circles = sorted(circles, key=lambda x: -len(x))
        
    result = ""
    for entry in sorted_circles[0]:
        result += entry + ','
    result = result[:-1]
    return result