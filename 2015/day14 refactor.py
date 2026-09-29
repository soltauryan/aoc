from aoc_utils import data_import
from dataclasses import dataclass

@dataclass
class Reindeer:
    name: str
    speed: int
    stamina: int
    rest_time: int

raw_data = data_import.get_input("day14.txt")
example_data = """Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds."""


def data_prep(input_data):
    raw_lines = [l.split(" ") for l in input_data.splitlines()]

    reindeer = []
    for l in raw_lines:
        reindeer.append(
            Reindeer(
                name = l[0],
                speed = int(l[3]),
                stamina = int(l[6]),
                rest_time = int(l[13])
            )
        )

    return reindeer


def distance_after(reindeer, seconds):
    cycle = reindeer.stamina + reindeer.rest_time
    full_cycles, remainder = divmod(seconds, cycle)

    flying_seconds = (
        full_cycles * reindeer.stamina
        + min(remainder, reindeer.stamina)
    )

    return flying_seconds * reindeer.speed

def main_p1(input_data, seconds):
    data = data_prep(input_data)
    return {
        rdeer.name: distance_after(rdeer, seconds)
        for rdeer in data
    }

def main_p2(input_data, seconds):
    reindeer = data_prep(input_data)
    scores = {r.name: 0 for r in reindeer}
    
    for second in range(1, seconds + 1):
        distances = {
            r.name: distance_after(r, second)
            for r in reindeer
        }

        lead_distance = max(distances.values())

        for name, distance in distances.items():
            if distance == lead_distance:
                scores[name] += 1

    return scores

p1 = main_p1(raw_data, 2503)
print(p1)
p2 = main_p2(raw_data, 2503)
print(p2)