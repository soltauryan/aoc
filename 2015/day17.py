from aoc_utils import data_import
from itertools import combinations

raw_data = data_import.get_input()
example_data = """20
15
10
5
5"""

def data_prep(data):
    pass

def main_p1(data):
    total = 0
    for num in range(1, len(data)+1):
        for valid_combo in iterate_combos(data, num):
            total += 1

    return total

def main_p2(data):
    valid_combo_list = []
    for num in range(1, len(data)+1):
        for valid_combo in iterate_combos(data, num):
            valid_combo_list.append(valid_combo)

    min_len = 100000
    for l in valid_combo_list:
        min_len = min(len(l), min_len)
    min_len_combo_list = [l for l in valid_combo_list if len(l) == min_len]

    return len(min_len_combo_list) , min_len_combo_list

def iterate_combos(buckets, len):
    for combo in combinations(buckets, len):
        if sum(combo) == 150:
            yield list(combo)

if __name__ == "__main__":
    data = [int(num) for num in raw_data.splitlines()]
    p1_total = main_p1(data)
    print(f"P1: {p1_total}")
    p2_len, p2_combos = main_p2(data)
    print(f"P2: {p2_len}\n{p2_combos}")
