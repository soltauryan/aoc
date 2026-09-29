from aoc_utils import data_import

raw_data = data_import.get_input()
example_data = """Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds."""

def data_prep(data):
    raw_lines = [l.split(" ") for l in data.splitlines()]
    return [[l[0], int(l[3]), int(l[6]), int(l[13])] for l in raw_lines]

def main_p1(data, second_goal):
    flight_dict = {}

    for rdeer in data:
        name = rdeer[0]
        speed = rdeer[1]
        stamina = rdeer[2]
        rest_time = rdeer[3]
        flight = []
        time_remaining = second_goal
        flying = True

        while time_remaining > 0:
            if flying:
                actions_to_take = min(time_remaining, stamina)
                flight.extend([speed] * actions_to_take)
            else:
                actions_to_take = min(time_remaining, rest_time)
                flight.extend([0] * actions_to_take)
            time_remaining = time_remaining - actions_to_take
            flying = not flying
        
        flight_dict[name] = sum(flight)
    
    return flight_dict

def return_rdeer_flights(data, second_goal):
    flight_dict = {}

    for rdeer in data:
        name = rdeer[0]
        speed = rdeer[1]
        stamina = rdeer[2]
        rest_time = rdeer[3]
        flight = []
        time_remaining = second_goal
        flying = True

        while time_remaining > 0:
            if flying:
                actions_to_take = min(time_remaining, stamina)
                flight.extend([speed] * actions_to_take)
            else:
                actions_to_take = min(time_remaining, rest_time)
                flight.extend([0] * actions_to_take)
            time_remaining = time_remaining - actions_to_take
            flying = not flying
        
        flight_dict[name] = flight
    
    return flight_dict


def update_distance_dict(distance_dict, flights, i):
    for rdeer in distance_dict.keys():
        distance_dict[rdeer] += flights[rdeer][i]
    return distance_dict


def update_score_dict(distance_dict, score_dict):
    max_distance = max(distance_dict.values())
    leaders = [rdeer for rdeer, dist in distance_dict.items() if dist == max_distance]
    
    for rdeer in leaders:
        score_dict[rdeer] += 1
    
    return score_dict

def main_p2(data, second_goal):
    flights = return_rdeer_flights(data, second_goal)
    distance_dict = {rdeer:0 for rdeer in flights.keys()}
    score_dict = {rdeer:0 for rdeer in flights.keys()}

    for i in range(second_goal):
        distance_dict = update_distance_dict(distance_dict, flights, i)
        score_dict = update_score_dict(distance_dict, score_dict)

    print(score_dict)


if __name__ == "__main__":
    data = data_prep(example_data)
    print(main_p1(data, 1000))
    data = data_prep(raw_data)
    flight_dict = main_p1(data, 2503)
    print(flight_dict)
    main_p2(data, 2503)