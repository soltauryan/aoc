from aoc_utils import data_import

raw_data = data_import.get_input()

right_dict = {"N": "E", "E": "S", "S": "W", "W": "N"}
left_dict = {"N": "W", "E": "N", "S": "E", "W": "S"}
travel_dict = {"N": (0, 1), "E": (1, 0), "S": (0, -1), "W": (-1, 0)}

def data_prep(data):
    dirs = data.split(", ")
    return dirs

def main_p1(data):
    x = 0
    y = 0
    curr_dir = "N"
    
    dirs = data_prep(data)
    for dir in dirs:
        card, distance = dir[0], int(dir[1:])
        
        if card == "R":
            curr_dir = right_dict[curr_dir]
        elif card == "L":
            curr_dir = left_dict[curr_dir]
        else:
            raise ValueError

        x += distance * travel_dict[curr_dir][0]
        y += distance * travel_dict[curr_dir][1]
    
    print(x, y)
    print(abs(x) + abs(y))
    return abs(x) + abs(y)


def main_p2(data):
    x = 0
    y = 0
    curr_dir = "N"
    visited_coords = set()
    
    dirs = data_prep(data)
    for dir_i in dirs:
        card, distance = dir_i[0], int(dir_i[1:])
        
        if card == "R":
            curr_dir = right_dict[curr_dir]
        elif card == "L":
            curr_dir = left_dict[curr_dir]
        else:
            raise ValueError

        for _ in range(distance):
            x += 1 * travel_dict[curr_dir][0]
            y += 1 * travel_dict[curr_dir][1]
            
            if (x, y) in visited_coords:
                print(x, y)
                print(abs(x) + abs(y))
                return (abs(x) + abs(y))

            visited_coords.add((x, y))


if __name__ == "__main__":
    main_p1(raw_data)
    main_p2(raw_data)   
