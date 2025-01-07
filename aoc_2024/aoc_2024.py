import importlib.util
import sys
import os
import time
from datetime import datetime


def read_aoc_input(day: str, is_live: bool):
    file_name = day + ("_Input.txt" if is_live else "_Input_Example.txt")
    file_path = os.path.join(os.path.dirname(__file__), day, file_name)
    return open(file_path).read().strip();


def show_result(day: str, is_part_two: bool, is_live: bool, result: str):
    part_text = "B" if is_part_two else "A"
    type_text = "" if is_live else " (Example)"
    print(f"[{day} {part_text}{type_text}] {result}")
    
    
def run_day(day: int, is_part_two: bool, use_live_data: bool):
    module_name = f"Day{day}"
    module_path = os.path.join(module_name, f"{module_name}.py")
        
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    day_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(day_module)
        
    data = read_aoc_input(module_name, use_live_data)
        
    if (is_part_two):
        result = day_module.part_two(data)
    else:
        result = day_module.part_one(data)
            
    show_result(module_name, is_part_two, use_live_data, result)


day_to_run = datetime.today().day
# day_to_run = 22
run_day(day_to_run, False, False)
run_day(day_to_run, True, False)
print("")

start_time = time.time()
run_day(day_to_run, False, True)
print(f"{round((time.time() - start_time) * 1000, 4)}ms")
print("")

start_time = time.time()
run_day(day_to_run, True, True)
print(f"{round((time.time() - start_time) * 1000, 4)}ms")

print("")