from typing import Tuple

Directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]


class Node:
    def __init__(self, x, y) -> None:
        self.paths = [None, None, None, None]
        self.coord = (x, y)


def count_paths(node: Node):
    result = 0
    for path in node.paths:
        if path != None:
            result += 1
    return result

def print_node(node: Node):
    if node == None:
        print("None")
        return
    output = f"{node.coord}: "
    for path in node.paths:
        if path == None:
            output += "None "
        else:
            output += f"({path[0].coord}, {path[1]}) "
    print(output)


def print_graph(start_node: Node):
    seen = {start_node}
    search_space = [start_node]
    while len(search_space) > 0:
        node = search_space.pop(0)
        print_node(node)
        for path in node.paths:
            if path == None:
                continue
            if path[0] not in seen:
                seen.add(path[0])
                search_space.append(path[0])
    print(f"Total Nodes: {len(seen)}")


def parse_graph(data: str) -> Tuple[Node, Node]:
    lines = data.splitlines()
    height, width = len(lines), len(lines[0])
    grid = []
    start_node = None
    end_node = None
    # Create nodes
    for y in range(height):
        row = []
        for x in range(width):
            c = lines[y][x]
            if c != '#':
                row.append(Node(x, y))
            else:
                row.append(None)
            if c == 'S':
                start_node = row[-1]
            elif c == 'E':
                end_node = row[-1]
        grid.append(row)
    
    # Connect nodes
    line_nodes = []
    single_nodes = []
    for y in range(height):
        for x in range(width):
            node = grid[y][x]
            if node == None:
                continue
            connection_count = 0
            for d in range(len(Directions)):
                to = grid[y + Directions[d][1]][x  + Directions[d][0]]
                if to != None:
                    node.paths[d] = (to, 1)
                    connection_count += 1

            if connection_count == 2 and node.paths[0] != None and node.paths[2] != None:
                line_nodes.append(node)
            elif connection_count == 2 and node.paths[1] != None and node.paths[3] != None:
                line_nodes.append(node)
            elif connection_count == 1:
                single_nodes.append(node)

    # Collapse graph, shortening all straight-line nodes
    for node in line_nodes:
        if node.paths[0] != None:
            a, b = node.paths[0], node.paths[2]
            dist = a[1] + b[1]
            a[0].paths[2] = (b[0], dist)
            b[0].paths[0] = (a[0], dist)
        else:
            a, b = node.paths[1], node.paths[3]
            dist = a[1] + b[1]
            a[0].paths[3] = (b[0], dist)
            b[0].paths[1] = (a[0], dist)
            
    # Prune paths that have a single connection (unless it's the start or end node)
    for node in single_nodes:
        while count_paths(node) == 1 and node != start_node and node != end_node:
            d = -1
            for path in node.paths:
                d += 1
                if path != None:
                    connection_path = path
                    break
            d = (d + 2) % len(Directions)
            connection_path[0].paths[d] = None
            node = connection_path[0]
            
    return (start_node, end_node)


def find_short_path_cost(start_node: Node, end_node: Node):
    visited = {(start_node, 0) : 0} # (Node, Direction): Distance
    search_space = [(start_node, 0, 0)] # (Node, Direction, Distance)
    while len(search_space) > 0:
        node, direction, distance = search_space.pop(0)
        skip = (direction + 2) % len(Directions)
        for d in range(len(Directions)):
            if d == skip or node.paths[d] == None:
                continue
            path_node, path_distance = node.paths[d]
            walk_distance = path_distance
            if d != direction:
                walk_distance += 1000
            total_distance = distance + walk_distance
            new_state = (path_node, d)
            if new_state in visited and visited[new_state] <= total_distance:
                continue # The path has already been visited in the direction with a lower distance
            visited[new_state] = total_distance
            search_space.append((path_node, d, total_distance))

    result = None
    for d in range(len(Directions)):
        if (end_node, d) in visited:
            distance = visited[(end_node, d)]
            if result == None or distance < result:
                result = distance
    return result


def part_one(data: str):
    start_node, end_node = parse_graph(data)
    return find_short_path_cost(start_node, end_node)


def sign_zero(number: int):
    if number > 0:
        return 1
    if number < 0:
        return -1
    return 0


def part_two(data: str):
    start_node, end_node = parse_graph(data)
    short_path_cost = find_short_path_cost(start_node, end_node)
    
    visited = {(start_node, 0) : 0} # (Node, Direction): Distance
    search_space = [(start_node, 0, 0, [start_node])] # (Node, Direction, Distance, Nodes)
    valid_paths = []
    while len(search_space) > 0:
        node, direction, distance, path = search_space.pop(0)
        skip = (direction + 2) % len(Directions)
        for d in range(len(Directions)):
            if d == skip or node.paths[d] == None:
                continue
            path_node, path_distance = node.paths[d]

            walk_distance = path_distance
            if d != direction:
                walk_distance += 1000
            total_distance = distance + walk_distance
            if total_distance > short_path_cost:
                continue
            new_state = (path_node, d)
            if new_state in visited and visited[new_state] < total_distance:
                continue # The path has already been visited in the direction with a lower distance
            visited[new_state] = total_distance
            
            new_path = list(path)
            new_path.append(path_node)
            new_entry = (path_node, d, total_distance, new_path)
            if path_node == end_node:
                valid_paths.append(new_path)
            else:
                search_space.append(new_entry)
    result_nodes = set()
    for path in valid_paths:
        for n in range(len(path) - 1):
            a, b = path[n], path[n + 1]
            x, y = a.coord[0], a.coord[1]
            tx, ty = b.coord[0], b.coord[1]
            dx = sign_zero(tx - x)
            dy = sign_zero(ty - y)
            while x != tx or y != ty:
                result_nodes.add((x, y))
                x += dx
                y += dy
            result_nodes.add((x, y))
    return len(result_nodes)