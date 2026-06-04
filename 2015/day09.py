from aoc_utils import data_import
from itertools import permutations

raw_data = data_import.get_input()


def data_prep(data):
    dist_dict = {}
    unique_cities = set()
    for line in data.splitlines():
        cities, dist = line.split(" = ")
        origin, dest = cities.split(" to ")

        dist_dict[(origin, dest)] = int(dist)
        unique_cities.add(origin)
        unique_cities.add(dest)

    return dist_dict, unique_cities


def get_distance(route, dist_dict):
    sum = 0
    for i in range(len(route) - 1):
        j = i + 1

        if (route[i], route[j]) in dist_dict.keys():
            sum += dist_dict[(route[i], route[j])]
        elif (route[j], route[i]) in dist_dict.keys():
            sum += dist_dict[(route[j], route[i])]

    return sum


def main_p1(data):
    dist_dict, cities = data_prep(raw_data)
    combos = list(permutations(cities, len(cities)))

    route_dist_dict = {}
    for route in combos:
        route_dist_dict[route] = get_distance(route, dist_dict)
    
    return route_dist_dict[min(route_dist_dict, key=route_dist_dict.get)]

def main_p2(data):
    dist_dict, cities = data_prep(raw_data)
    combos = list(permutations(cities, len(cities)))

    route_dist_dict = {}
    for route in combos:
        route_dist_dict[route] = get_distance(route, dist_dict)
    
    return route_dist_dict[max(route_dist_dict, key=route_dist_dict.get)]


if __name__ == "__main__":
    print(main_p1(raw_data))
    print(main_p2(raw_data))
