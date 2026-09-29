from aoc_utils import data_import
from itertools import permutations, combinations

raw_data = data_import.get_input()
example_data = """Alice would gain 54 happiness units by sitting next to Bob.
Alice would lose 79 happiness units by sitting next to Carol.
Alice would lose 2 happiness units by sitting next to David.
Bob would gain 83 happiness units by sitting next to Alice.
Bob would lose 7 happiness units by sitting next to Carol.
Bob would lose 63 happiness units by sitting next to David.
Carol would lose 62 happiness units by sitting next to Alice.
Carol would gain 60 happiness units by sitting next to Bob.
Carol would gain 55 happiness units by sitting next to David.
David would gain 46 happiness units by sitting next to Alice.
David would lose 7 happiness units by sitting next to Bob.
David would gain 41 happiness units by sitting next to Carol."""

def determine_sign(sign_str: str, num: str) -> int:
    if sign_str == "gain":
        return int(num)
    else:
        return -1 * int(num)

def data_prep(raw_data):
    raw_list = [l.split(" ") for l in raw_data.splitlines()]
    trimmed_list = [[l[0], determine_sign(l[2], l[3]), l[10][:-1]] for l in raw_list]
    score_lookup = {f"{l[0]}->{l[2]}": l[1] for l in trimmed_list}
    return trimmed_list, score_lookup


def determine_combinations(data):
    people = set([l[0] for l in data])
    return list(permutations(people))


def score_seating_map(seating_map: tuple, score_dict) -> int:
    score = 0
    seat_map_prior = 0
    seat_map_after = 0

    for i, person in enumerate(seating_map):
        # Identify which person is sitting to their left and right
        if i == 0:
            seat_map_prior = -1
            seat_map_after = i + 1
        elif i == len(seating_map) - 1:
            seat_map_prior = i - 1
            seat_map_after = 0
        else:
            seat_map_prior = i - 1
            seat_map_after = i + 1
        # print(seat_map_prior, seat_map_after)

        score += score_dict[f"{person}->{seating_map[seat_map_prior]}"]
        score += score_dict[f"{person}->{seating_map[seat_map_after]}"]
    
    return score




def main_p1(data, happiness_dict):
    possible_seating_maps = determine_combinations(data)

    score_dict = {}
    for sm in possible_seating_maps:
        score_dict[sm] = score_seating_map(sm, happiness_dict)

    return max(score_dict.values())


def p2_data_prep(data):
    me = "Ryan"
    people = set([l[0] for l in data])
    for peep in people:
        data.append([peep, 0, me])
        data.append([me, 0, peep])
    
    score_lookup = {f"{l[0]}->{l[2]}": l[1] for l in data}

    return data, score_lookup

def main_p2(data, happiness_dict):
    
    data, happiness_dict = p2_data_prep(data)
    possible_seating_maps = determine_combinations(data)

    score_dict = {}
    for sm in possible_seating_maps:
        score_dict[sm] = score_seating_map(sm, happiness_dict)


    return max(score_dict.values())

if __name__ == "__main__":
    data, score_dict = data_prep(raw_data)
    p1 = main_p1(data, score_dict)
    p2 = main_p2(data, score_dict)
    print(f"Part 1: {p1:,}")
    print(f"Part 2: {p2:,}")
    