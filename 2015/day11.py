from aoc_utils import data_import

raw_data = data_import.get_input()
data_import.preview()

def increment_letter(ord_num):
    if ord_num != 122:
        return ord_num + 1, False
    else:
        return 97, True

def test():
    r1 = "az"
    ord_list = [ord(char) for char in r1]
    print(l)
    print(122 )

def data_prep(data):
    pass

def main_p1(data):
    pass

def main_p2(data):
    pass

if __name__ == "__main__":
    test()
    # main_p1(raw_data)
    # main_p2(raw_data)   
    pass
