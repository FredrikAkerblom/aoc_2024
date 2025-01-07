import time

def part_one(data: str):
    result = 0
    block_index = 0
    back_index = len(data) - 1
    back_read = int(data[back_index]) - 1
    back_id = back_index // 2
    for c in range(len(data)):
        if c % 2 == 0:
            # Read from front
            front_id = c // 2
            for i in range(int(data[c])):
                if front_id == back_id and i > back_read:
                    return result # Front and back read heads met
                result += block_index * front_id
                block_index += 1
        else:
            # Read from back
            for i in range(int(data[c])):
                while back_read < 0:
                    back_index -= 2
                    back_read = int(data[back_index]) - 1
                    back_id = back_index // 2
                    if front_id == back_id and i >= back_read:
                        return result # Front and back read heads met
                result += block_index * back_id
                block_index += 1
                back_read -= 1
    print("Reached end, something went wrong")
    return 0


def part_two(data: str):
    result = 0
    files = []
    for i in range(len(data)):
        file_id = i // 2
        is_empty = (i % 2) == 1
        size = int(data[i])
        files.append((file_id, is_empty, size))
    
    start_time = time.time()
    i = 0
    while i < len(files):
        file_index = len(files) - 1 - i
        file = files[file_index]
        if not file[1]:
            for j in range(file_index):
                target = files[j]
                if target[1] and target[2] >= file[2]:
                    files[file_index] = (0, True, file[2])
                    files[j] = file
                    if target[2] > file[2]:
                        files.insert(j + 1, (0, True, target[2] - file[2]))
                    break
        i += 1
    print(f"Compress Time: {time.time() - start_time}s")

    start_time = time.time()
    block_index = 0
    for f in range(len(files)):
        file = files[f]
        for i in range(file[2]):
            if not file[1]:
                result += block_index * file[0]
            block_index += 1
    print(f"Checksum Time: {time.time() - start_time}s")
    return result