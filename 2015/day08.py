from aoc_utils import data_import
import ast

# raw_data = data_import.get_input()
data_import.preview()

def data_prep(data):
    pass

def main_p1():
    total_code_chars = 0
    total_memory_chars = 0
    
    with open("2015/input/day08.txt") as f:
        for line in f:
            line = line.strip()
            memory_str = ast.literal_eval(line)

            total_code_chars += len(line)
            total_memory_chars += len(memory_str)
    
    return total_code_chars - total_memory_chars

def main_p2():
    total_code_chars = 0
    total_memory_chars = 0
    
    with open("2015/input/day08.txt") as f:
        for line in f:
            line = line.strip()
            encoded_line = fr"\"{line}\""
            memory_str = ast.literal_eval(line)
            print(encoded_line, len(encoded_line))
            total_code_chars += len(encoded_line)
            total_memory_chars += len(memory_str)
    
    return total_code_chars - total_memory_chars

if __name__ == "__main__":
    print(main_p1())
    print(main_p2())