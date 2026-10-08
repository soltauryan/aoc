from aoc_utils import data_import
from dataclasses import dataclass

raw_data = data_import.get_input()

example = """inc a
jio a, +2
tpl a
inc a"""

@dataclass
class TuringMachine:
    a:int = 0
    b:int = 0

    def get_register_value(self, register):
        return getattr(self, register)

    def set_register_value(self, register, new_value):
        setattr(self, register, max(0, new_value))

    def process_instruction(self, instruction_str):
        # Parse String
        offset = 0
        i_str, register = instruction_str.split(" ", 1)
        if ", " in register:
            register, offset = register.split(", ")
            offset = int(offset)

        # Apply instruction logic
        if i_str == "hlf":
            r = self.set_register_value(register, getattr(self, register) // 2)
            offset = 1
        elif i_str == "tpl":
            r = self.set_register_value(register, getattr(self, register) * 3)
            offset = 1
        elif i_str == "inc":
            r = self.set_register_value(register, getattr(self, register) + 1)
            offset = 1
        elif i_str == "jmp":
            offset = int(register)
        elif i_str == "jie":
            if getattr(self, register) % 2 != 0:
                offset = 1
        elif i_str == "jio":
            if getattr(self, register) != 1:
                offset = 1
        
        return offset

def parse_instruction_string(input_str) -> list:
    return input_str.splitlines()


def main_p1():
    instructs = parse_instruction_string(raw_data)
    offset = 0
    machine = TuringMachine()

    while offset >= 0 and offset < len(instructs):
        try:
            current_instruct = instructs[offset]
        except:
            print("The while loop failed!")
            raise ArithmeticError

        offset += machine.process_instruction(current_instruct)
    
    print(f"Register A: {machine.a}")
    print(f"Register B: {machine.b}")
        

def main_p2():
    instructs = parse_instruction_string(raw_data)
    offset = 0
    machine = TuringMachine(1, 0)

    while offset >= 0 and offset < len(instructs):
        try:
            current_instruct = instructs[offset]
        except:
            print("The while loop failed!")
            raise ArithmeticError

        offset += machine.process_instruction(current_instruct)
    
    print(f"Register A: {machine.a}")
    print(f"Register B: {machine.b}")

if __name__ == "__main__":
    print("Part 1")
    main_p1()
    print("\nPart 2")
    main_p2()