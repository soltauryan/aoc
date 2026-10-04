from aoc_utils import data_import
from typing import List
import re
import random

raw_data = data_import.get_input()
example_data = """H => HO
H => OH
O => HH

HOH"""

example_data_p2 = """e => H
e => O
H => HO
H => OH
O => HH

HOH"""


def data_prep(data):
    replacement_list = []
    for l in data.splitlines()[:-2]:
        val = l.split(" => ")
        replacement_list.append([val[0], val[1]])
    molecule = data.splitlines()[-1]
    return replacement_list, molecule.strip()


def find_match_positions(substring:str, text:str) -> List[int]:
    return [match.start() for match in re.finditer(substring, text)]


def new_molecule(text:str,
                old_substring:str,
                substring: str,
                position:int) -> str:
    return text[:position] + substring + text[position+len(old_substring):]

def main_p1(data):
    distinct_molecules = set()
    replacement_list, molecule = data_prep(data)
    for rule in replacement_list:
        find_str, replacement_str = rule[0].strip(), rule[1].strip()
        substring_positions = find_match_positions(find_str, molecule)
        for s in substring_positions:
            distinct_molecules.add(new_molecule(molecule, find_str, replacement_str, s))
    return len(distinct_molecules)

import random

def main_p2(data):
    replacement_list, target_molecule = data_prep(data)

    reverse_rules = [
        (replacement.strip(), original.strip())
        for original, replacement in replacement_list
    ]

    while True:
        current_molecule = target_molecule
        steps = 0

        random.shuffle(reverse_rules)

        while current_molecule != "e":
            for find_str, replacement_str in reverse_rules:
                position = current_molecule.find(find_str)

                if position != -1:
                    current_molecule = new_molecule(
                        current_molecule,
                        find_str,
                        replacement_str,
                        position
                    )
                    steps += 1
                    break
            else:
                # Dead end: restart from the original molecule
                break

        if current_molecule == "e":
            return steps

if __name__ == "__main__":
    print(main_p1(raw_data))
    print(main_p2(raw_data))
