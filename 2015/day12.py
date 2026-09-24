from aoc_utils import data_import
import json

raw_data = data_import.get_input()

def data_prep(data):
    json_data = json.loads(data)
    return json_data


def sum_numbers_p1(data):
    total = 0

    if isinstance(data, dict):
        for value in data.values():
            total += sum_numbers_p1(value)
    
    elif isinstance(data, (list, tuple)):
        for item in data:
            total += sum_numbers_p1(item)

    elif isinstance(data, int):
        total += data

    return total


def sum_numbers_p2(data):
    total = 0

    if isinstance(data, dict):
        # check for red in object before adding
        red_value = False
        for value in data.values():
            if value == "red":
                red_value = True
        
        if red_value:
            total += 0
        else:
            for value in data.values():
                total += sum_numbers_p2(value)

    elif isinstance(data, (list, tuple)):
        for item in data:
            total += sum_numbers_p2(item)

    elif isinstance(data, int):
        total += data

    return total
 
def main_p1(data):
    data = data_prep(data)
    return sum_numbers_p1(data)
 
def main_p2(data):
    data = data_prep(data)
    return sum_numbers_p2(data)
 
 
if __name__ == "__main__":
    p1 = main_p1(raw_data)
    print(f"Part 1: {p1:,}")
    p2 = main_p2(raw_data)
    print(f"Part 2: {p2:,}")
