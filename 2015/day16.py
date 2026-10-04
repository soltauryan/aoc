from aoc_utils import data_import
from dataclasses import dataclass, fields

@dataclass
class Sue:
    name: str
    children: int | None = None
    cats: int | None = None
    samoyeds: int | None = None
    pomeranians: int| None = None
    akitas: int | None = None
    vizslas: int | None = None
    goldfish: int | None = None
    trees: int | None = None
    cars: int | None = None
    perfumes: int | None = None

our_sue = """Our Sue!: children: 3, cats: 7, samoyeds: 2, pomeranians: 3, akitas: 0, vizslas: 0, goldfish: 5, trees: 3, cars: 2, perfumes: 1"""

raw_data = data_import.get_input()

def process_one_sue(sue:str) -> Sue:
    first_colon = sue.find(":")
    sue_id, compounds = sue[:first_colon], sue[first_colon+2:]
    c_dict = {}
    for c in compounds.split(","):
        name, num = c.split(":")
        c_dict[name.strip()] = int(num.strip())
    return Sue(
        name = sue_id,
        **c_dict
    )

def data_prep(data):
    return [process_one_sue(sue) for sue in data.splitlines()]




def main_p1(sue_list):
    sue_prime = process_one_sue(our_sue)
    matching_sues = sue_list.copy()
    for field in fields(sue_prime):
        filtered_sues = []
        if field.name == "name":
            continue
        sue_prime_val = getattr(sue_prime, field.name)
        for s in matching_sues:
            if s.name == "Sue 373":
                print("yeah")
            if getattr(s, field.name) is None:
                filtered_sues.append(s)
            elif field.name in ('cats', 'trees') and getattr(s, field.name) > sue_prime_val:
                filtered_sues.append(s)
            elif field.name in ('pomeranians', 'goldfish') and getattr(s, field.name) < sue_prime_val:
                filtered_sues.append(s)
            elif field.name not in ('cats', 'trees', 'pomeranians', 'goldfish') and getattr(s, field.name) == sue_prime_val:
                filtered_sues.append(s)
            else:
                print("huh?")
        
        print(len(matching_sues), len(filtered_sues))
        matching_sues = filtered_sues.copy()
    return matching_sues




def main_p2(sue_list):
    sue_prime = process_one_sue(our_sue)

if __name__ == "__main__":
    # print(process_one_sue(raw_data.splitlines()[0]))
    sue_list = data_prep(raw_data)
    print(main_p1(sue_list))