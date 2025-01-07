directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]


def simulate(value: int, steps: int):
    for _ in range(steps):
        value ^= value << 6  # * 64
        value &= 0xFFFFFF    # % 16777216
        value ^= value >> 5  # // 32
        value &= 0xFFFFFF    # % 16777216
        value ^= value << 11 # * 2048
        value &= 0xFFFFFF    # % 16777216
    return value


def add_sequence_values(value: int, steps: int, sequences):
    prev_price = value % 10
    current_sequence = []
    seen_sequences = set()
    for _ in range(steps):
        value ^= value << 6  # * 64
        value &= 0xFFFFFF    # % 16777216
        value ^= value >> 5  # // 32
        value &= 0xFFFFFF    # % 16777216
        value ^= value << 11 # * 2048
        value &= 0xFFFFFF    # % 16777216
        
        price = value % 10
        change = price - prev_price
        prev_price = price
        
        current_sequence.append(change)
        if len(current_sequence) > 4:
            current_sequence.pop(0)
        if len(current_sequence) == 4:
            sequence = tuple(current_sequence)
            if sequence not in seen_sequences:
                seen_sequences.add(sequence)
                sequences[sequence] = sequences.get(sequence, 0) + price
    

def part_one(data: str):
    lines = data.splitlines()
    result = 0
    for line in lines:
        secret = simulate(int(line), 2000)
        # print(f"{line}: {secret}")
        result += secret
    return result


def part_two(data: str):
    lines = data.splitlines()
    result = 0
    monkeys = []
    unique_sequences = dict()
    for line in lines:
        add_sequence_values(int(line), 2000, unique_sequences)
    max_pair = max(unique_sequences.items(), key=lambda x: x[1])
    # print(f"Unique Sequences: {len(unique_sequences)}")
    # print(f"MaxPair: {max_pair}")
    return max_pair[1]