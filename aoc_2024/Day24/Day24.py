import math
from graphviz import Digraph

directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]


AND = 0
OR = 1
XOR = 2
    

def parse_gates(data: str):
    lines = data.splitlines()
    gates = []    
    for line in lines:
        parts = line.split(" -> ")
        target = parts[1]
        if " AND " in parts[0]:
            a, b = parts[0].split(" AND ")
            gates.append((a, b, AND, target))
        elif " OR " in parts[0]:
            a, b = parts[0].split(" OR ")
            gates.append((a, b, OR, target))
        elif " XOR " in parts[0]:
            a, b = parts[0].split(" XOR ")
            gates.append((a, b, XOR, target))
        else:
            print(f"Unknown gate: {line}")
    return gates
            

def simulate(state, gates, swapped_wires = None):
    has_activity = True
    state = dict(state)
    gates = list(gates)
    while has_activity and len(gates) > 0:
        has_activity = False
        i = 0
        while i < len(gates):
            gate = gates[i]
            if gate[3] in state:
                has_activity = True
                gates.pop(i)
                i -= 1
            elif gate[0] in state and gate[1] in state:
                has_activity = True
                a, b = state[gate[0]], state[gate[1]]
                target_wire = gate[3]
                if swapped_wires != None and len(swapped_wires) > 0:
                   if target_wire in swapped_wires:
                        target_wire = swapped_wires[target_wire]
                if gate[2] == AND: state[target_wire] = a and b
                elif gate[2] == OR: state[target_wire] = a or b
                elif gate[2] == XOR: state[target_wire] = a != b
                else: print(f"Unknown Gate: {gate[2]}")
                gates.pop(i)
                i -= 1
            i += 1
    return state


def parse_start(data: str):
    lines = data.splitlines()
    start_state = dict()
    for line in lines:
        key, value = line.split(": ")
        start_state[key] = value == '1'
    return start_state


def read_value(state, index, skip_print = False):
    z_pairs = []
    for entry in state:
        if entry.startswith(index):
            z_pairs.append((entry, state[entry]))
            
    sorted_z = sorted(z_pairs, key=lambda x: x[0])
    binary_string = ""
    for entry in sorted_z:
        binary_string = ('1' if entry[1] else '0') + binary_string
    if len(binary_string) == 0:
        if not skip_print:
            print(f"{index}: Empty")
        return None
    value = int(binary_string, 2)
    if not skip_print:
        print(f"{index}: {binary_string} = {value}")
    return int(binary_string, 2)


def read_result(state):
    return read_value(state, 'z')


def part_one(data: str):
    parts = data.split("\n\n")
    state = parse_start(parts[0])
    gates = parse_gates(parts[1])
    
    state = simulate(state, gates)
    return read_result(state)


def get_connected_gates(gates, start_point):
    search_space = [f"x{start_point:02}"]
    connected = set()
    while len(search_space) > 0:
        wire = search_space.pop(0)
        for gate in gates:
            if gate[0] == wire or gate[1] == wire:
                if gate[3] not in connected:
                    connected.add(gate[3])
                    search_space.append(gate[3])
    return sorted(list(connected))


def get_feed_gates(gates, end_point):
    search_space = [f"z{end_point:02}"]
    connected = set()
    while len(search_space) > 0:
        wire = search_space.pop(0)
        for gate in gates:
            if gate[3] == wire:
                if gate[0] not in connected:
                    connected.add(gate[0])
                    search_space.append(gate[0])
                if gate[1] not in connected:
                    connected.add(gate[1])
                    search_space.append(gate[1])
    return sorted(list(connected))
    

def create_test_state(i, length, fill=False, secondary=False):
    test_state = {}
    for j in range(length):
        test_state[f"x{j:02}"] = (j <= i) if fill else (j == i)
        test_state[f"y{j:02}"] = secondary    
    return test_state


def solve_wires(faulty, bit_count, gates, swapped_wires):
    spaces = ""
    for i in range(4 - len(faulty)):
        spaces += "  "
    if len(faulty) == 0:
        print(f"{spaces}-")
        return
    
    entry = faulty[0]
    test_state = create_test_state(entry, bit_count, False, False)
    
    x = read_value(test_state, 'x')
    y = read_value(test_state, 'y')
    sim_state = simulate(test_state, gates, swapped_wires)
    z = read_value(sim_state, 'z')
        
    if z == 0:
        print(f"{spaces}0")
        return

    power_f = math.log2(z)
    
    if power_f != round(power_f):
        print(f"{spaces}~")
        return
    
    power = int(power_f)
        
    inputs = set(get_connected_gates(gates, entry))
    current_feed = get_feed_gates(gates, entry)
    wanted_feed = get_feed_gates(gates, power)
    current_feed = list(inputs & set(current_feed))
    wanted_feed  = list(inputs & set(wanted_feed))
    for current in current_feed:
        for wanted in wanted_feed:
            if current == wanted or current in swapped_wires or wanted in swapped_wires:
                continue
            test_swap = dict(swapped_wires)
            test_swap[current] = wanted
            test_swap[wanted] = current
            sim_state = simulate(test_state, gates, test_swap)
            z = read_value(sim_state, 'z', True)
            if x + y == z:
                swap = tuple(sorted([wanted, current]))
                print(f"{spaces}{current}-{wanted}")
                solve_wires(faulty[1:], bit_count, gates, test_swap)


# Pain, misery, and failure
# def part_two(data: str):
#     parts = data.split("\n\n")
#     state = parse_start(parts[0])
#     gates = parse_gates(parts[1])
#     if len(gates) < 40:
#         return "Not Applicable"
    
#     x_state = dict()
#     y_state = dict()

#     for key in state:
#         if key.startswith('x'):
#             x_state[key] = True
#             y_state[key] = False
#         elif key.startswith('y'):
#             y_state[key] = True
#             x_state[key] = False
#     print(f"BitCount: {len(state)}")
    
#     all_wires_set = set()
#     for gate in gates:
#         all_wires_set.add(gate[0])
#         all_wires_set.add(gate[1])
#         all_wires_set.add(gate[3])
#     all_wires = sorted(list(all_wires_set))
#     print(f"AllWires({len(all_wires)}): {all_wires}")
    
#     faulty = []

#     for i in range(len(state) // 2):
#         print(f"--- {i} ---")
#         test_state = create_test_state(i, len(state) // 2)
#         x = read_value(test_state, 'x')
#         y = read_value(test_state, 'y')
#         sim_state = simulate(test_state, gates)
#         z = read_value(sim_state, 'z')
#         print(f"{x + y == z}")
#         if x + y != z:
#             faulty.append(i)
#             print("    Faulty")
#         print()
    
#     print()

#     print(f"Faulty: {faulty}")
        
#     swapped_wires = dict()
#     possible_swaps = set()
    
#     bit_count = len(state) // 2
    
#     print("=== Solve ===")
#     solve_wires(faulty, bit_count, gates, swapped_wires)

#     # for entry in faulty:
#     #     print(f"=== Solve Faulty {entry} ===")
#     #     in_wires = faulty[entry]
        
#     #     test_state = create_test_state(entry, bit_count, False, False)
#     #     x = read_value(test_state, 'x')
#     #     y = read_value(test_state, 'y')
#     #     sim_state = simulate(test_state, gates, swapped_wires)
#     #     z = read_value(sim_state, 'z')
#     #     print(f"-> {format(x + y, f'0{bit_count+1}b')}")
#     #     power = int(math.log2(z))
#     #     print(f"Wanted: {entry}    Current: {power}")
#     #     print()
        
#     #     valid_swaps = set()
#     #     inputs = set(get_connected_gates(gates, entry))
#     #     current_feed = get_feed_gates(gates, entry)
#     #     wanted_feed = get_feed_gates(gates, power)
#     #     print(f"WantGates: {len(wanted_feed)}, CurGates: {len(current_feed)}")
#     #     current_feed = list(inputs & set(current_feed))
#     #     wanted_feed  = list(inputs & set(wanted_feed))
#     #     print(f"Filtered WantGates: {len(wanted_feed)}, CurGates: {len(current_feed)}")
#     #     for current in current_feed:
#     #         for wanted in wanted_feed:
#     #             if current == wanted:
#     #                 continue
#     #             test_swap = dict(swapped_wires)
#     #             test_swap[current] = wanted
#     #             test_swap[wanted] = current
#     #             sim_state = simulate(test_state, gates, test_swap)
#     #             z = read_value(sim_state, 'z', True)
#     #             if x + y == z:
#     #                 swap = tuple(sorted([wanted, current]))
#     #                 valid_swaps.add(swap)
#     #                 # print(f"Valid Swap: {current} - {wanted}")
#     #     print(f"ValidSwaps: {len(valid_swaps)}")

#     #     print()
#     # print(f"PossibleSwaps({len(possible_swaps)})")

#     result = ""
#     # for wire in sorted(swapped_wires):
#     #     result += wire + ','
#     # result = result[:-1]
#     # print(result)
#     return result

def part_two(data: str):
    parts = data.split("\n\n")
    
    dot = Digraph()
    added_nodes = set()
    op_index = 0
    for gate in parts[1].splitlines():
        # print(gate)
        gate = gate.replace(" -> ", " ")
        a, op, b, t = gate.split(' ')
        if not a in added_nodes:            
            dot.node(a)
            added_nodes.add(a)
        if not b in added_nodes:
            dot.node(b)
            added_nodes.add(b)
        if not t in added_nodes:
            dot.node(t)
            added_nodes.add(t)
        op_node = str(op_index)
        op_index += 1
        dot.node(op_node, op)
        dot.edge(a, op_node)
        dot.edge(b, op_node)
        dot.edge(op_node, t)
        print(f"{a} -> {t}")
        print(f"{b} -> {t}")
    # With the commented out part_two failed version we can see that [10, 17, 32, 39] are faulty, inspect the relevant nodes manually in the graph:
    dot.render("day24_graph.png", view=True)
    return 0