from aoc_utils import data_import
import math
from typing import List

raw_data = int(data_import.get_input())


def find_divsors(num:int) -> set:
    divisors = set()
    sqrt_num = math.isqrt(num)
    for n in range(1, sqrt_num+1):
        if num % n == 0:
            divisors.add(int(n))
            divisors.add(int(num / n))
    return sorted(divisors)


def limit_divisors(divisors:set) -> set:
    if len(divisors) > 50:
        return divisors[:50]
    else:
        return divisors


def presents_total(divisors:List)-> int:
    return sum([elf * 10 for elf in divisors])


def presents_total_p2(divisors:List)-> int:
    return sum([elf * 11 for elf in divisors])


def main_p1(data):
    goal = raw_data
    total = 0
    curr_num = 0

    while total <= goal:
        curr_num += 1
        divisors = find_divsors(curr_num)
        total = presents_total(divisors)
        if curr_num % 10_000 == 0:
            print(curr_num)
    
    print(f"Lowest House: {curr_num}")


def main_p2(data):
    goal = raw_data
    total = 0
    curr_num = 0

    while total <= goal:
        curr_num += 1
        divisors = find_divsors(curr_num)
        divisors = limit_divisors(divisors)
        total = presents_total_p2(divisors)
        if curr_num % 10_000 == 0:
            print(f"{curr_num:,}")
    
    print(f"Lowest House: {curr_num}")

if __name__ == "__main__":
    # print(math.isqrt(500000))
    main_p1(raw_data)
    # main_p2(raw_data)
    # main_p2(raw_data)   
    # num = 776160 
    # divisors = find_divsors(num)
    # presents = presents_total(divisors)
    # print(divisors)
    # print(f"{presents:,}")
    # print(f"{33100000:,}")
