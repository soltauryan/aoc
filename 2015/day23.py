from aoc_utils import data_import
from dataclasses import dataclass
raw_data = data_import.get_input()

@dataclass
class TuringMachine:
    a:int = 0
    b:int = 0

    def get_register_value(self, register):
        return getattr(self, register)

    def set_register_value(self, register, new_value):
        setattr(self, register, max(0, new_value))

    def process_instruction(register):
        # Parse String
        offset = 0
        i_str, r = instruction_str.split(" ", 1)
        if ", " in r:
            r, offset = r.split(", ")
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
            r = None
        elif i_str == "jie":
            if getattr(self, register) % 2 != 0:
                offset = 1
        elif i_str == "jio":
            if getattr(self, register) != 1:
                offset = 1
        
        return offset



def parse_instruction(index:int, instruction_str:str):
    
    


    # return instruction, register, value_delta, next_index

def data_prep(data):
    pass

def main_p1(data):
    pass

def main_p2(data):
    pass

if __name__ == "__main__":
    parse_instruction(0, "jio a, +2")
    parse_instruction(0, "tpl a")
