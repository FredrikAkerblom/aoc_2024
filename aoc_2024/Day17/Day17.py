def parse_input(data: str):
    data_parts = data.split("\n\n")
    regs = data_parts[0].splitlines()
    a = int(regs[0].split(": ")[1])
    b = int(regs[1].split(": ")[1])
    c = int(regs[2].split(": ")[1])
    instruction_data = data_parts[1].split(": ")[1].split(',')
    instructions = []
    for instruction in instruction_data:
        instructions.append(int(instruction))
    return (a, b, c, instructions)


def combo_operand(operand: int, a: int, b: int, c: int) -> int:
    if operand >= 0 and operand <= 3: return operand
    if operand == 4: return a
    if operand == 5: return b
    if operand == 6: return c
    print(f"Invalid operand: {operand}")
    return None


def execute(A, B, C, program):
    i = 0
    result = ""
    while i < len(program):
        opcode, literal = program[i], program[i + 1]
        combo = combo_operand(literal, A, B, C)
        i += 2
        if   opcode == 0: A = A >> combo
        elif opcode == 1: B = B ^ literal
        elif opcode == 2: B = combo % 8
        elif opcode == 3: i = literal if A != 0 else i
        elif opcode == 4: B = B ^ C
        elif opcode == 5: result += str(combo % 8) + ','
        elif opcode == 6: B = A >> combo
        elif opcode == 7: C = A >> combo
        else: print(f"Unknown instruction: {opcode}")
    if len(result) == 0:
        return ""
    return result[:-1]


def execute_to_target(A, B, C, program):
    i = 0
    p = 0
    result = []
    while i < len(program):
        opcode, literal = program[i], program[i + 1]
        combo = combo_operand(literal, A, B, C)
        i += 2
        if   opcode == 0: A = A >> combo
        elif opcode == 1: B = B ^ literal
        elif opcode == 2: B = combo % 8
        elif opcode == 3: i = literal if A != 0 else i
        elif opcode == 4: B = B ^ C
        elif opcode == 6: B = A >> combo
        elif opcode == 7: C = A >> combo
        elif opcode == 5:
            to_add = combo % 8
            if to_add != program[p]:
                return None
            result.append(to_add)
            p += 1
        else: print(f"Unknown instruction: {opcode}")
    if len(result) == 0 or result != program:
        return False
    return True


def part_one(data: str):
    A, B, C, program = parse_input(data)
    return execute(A, B, C, program)


def part_two(data: str):
    A, B, C, program = parse_input(data)

    program_target = ""
    for entry in program:
        program_target += str(entry) + ','
    program_target = program_target[:-1]

    current_set = [0, 1, 2, 3, 4, 5, 6, 7]
    for i in range(1, len(program)):
        next_set = []
        for possibility in current_set:
            for x in range(8):
                A = 8 * possibility + x
                program_result = execute(A, B, C, program)
                if program_result == program_target:
                    return A
                partial_program = program_target[len(program_target) - len(program_result):]
                if program_result == partial_program:
                    next_set.append(A)
        for entry in current_set:
            if entry in next_set:
                next_set.remove(entry)
        current_set = next_set
        print(current_set)
        print("==============================================")
    return "Failed"
