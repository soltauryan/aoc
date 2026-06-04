from aoc_utils import data_import

raw_data = data_import.get_input()
# data_import.preview()

def look_and_say(s):
    new_s = ""
    s_len = len(s)
    i = 0
    return_str = ""

    while i < s_len:
        j = i + 1
        curr_num = s[i:j]
        next_num = s[j:j+1]
        count = 1

        if curr_num != next_num:
            return_str += str(count) + curr_num
            i += 1
        elif curr_num == next_num:
            while curr_num == next_num:
                j += 1
                next_num = s[j:j+1]
                count += 1
            i = j
            return_str += str(count) + curr_num
        else:
            print("Shouldn't reach here", i, j, curr_num, next_num)

    return return_str


def main_p1(data):
    s = "1113122113"
    for _ in range(40):
        s = look_and_say(s)

    return len(s)
            


def main_p2(data):
    s = "1113122113"
    for _ in range(50):
        s = look_and_say(s)

    return len(s)

if __name__ == "__main__":
    p1 = main_p1(raw_data)
    p2 = main_p2(raw_data)   
    print(p1, p2)
