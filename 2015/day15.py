from aoc_utils import data_import
import math
from dataclasses import dataclass
from itertools import combinations_with_replacement

@dataclass
class Ingredient:
    name: str
    capacity: int
    durability: int
    flavor: int
    texture: int
    calories: int


raw_data = data_import.get_input()
# data_import.preview()

example_data = """Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3"""

def data_prep(data):
    ing_list = []
    for line in data.splitlines():
        ingredient_dict = {}
        name, ingredients = line.split(":")
        ingredients = [i.strip() for i in ingredients.split(",")]
        final_ing = Ingredient(
            name,
            int(ingredients[0].split(" ")[1]),
            int(ingredients[1].split(" ")[1]),
            int(ingredients[2].split(" ")[1]),
            int(ingredients[3].split(" ")[1]),
            int(ingredients[4].split(" ")[1]),
        )
        ing_list.append(final_ing)
    
    return ing_list

        
def p1_calc_score(ingredients, amount_dict):
    capacity_sum = max(0, sum([i.capacity*amount_dict[i.name] for i in ingredients]))
    durability_sum = max(0, sum([i.durability*amount_dict[i.name] for i in ingredients]))
    flavor_sum = max(0, sum([i.flavor*amount_dict[i.name] for i in ingredients]))
    texture_sum = max(0, sum([i.texture*amount_dict[i.name] for i in ingredients]))

    return capacity_sum * durability_sum * flavor_sum * texture_sum 

def p2_calc_score(ingredients, amount_dict):
    capacity_sum = max(0, sum([i.capacity*amount_dict[i.name] for i in ingredients]))
    durability_sum = max(0, sum([i.durability*amount_dict[i.name] for i in ingredients]))
    flavor_sum = max(0, sum([i.flavor*amount_dict[i.name] for i in ingredients]))
    texture_sum = max(0, sum([i.texture*amount_dict[i.name] for i in ingredients]))
    calories_sum = max(0, sum([i.calories*amount_dict[i.name] for i in ingredients]))

    return capacity_sum * durability_sum * flavor_sum * texture_sum, calories_sum


def p1_return_combos(ingredients):
    amount_counts = []
    for l in combinations_with_replacement([i.name for i in ingredients], 100):
        amount_dict = {}
        for i in ingredients:
            amount_dict[i.name] = l.count(i.name)
        amount_counts.append(amount_dict)
    return amount_counts

def main_p1(ingredients, combos):
    max_score = 0
    best_dict = {}

    for c in combos:
        score = p1_calc_score(ingredients, c)

        if score > max_score:
            max_score = score
            best_dict = c
    
    return max_score, best_dict


def main_p2(ingredients, combos):
    max_score = 0
    best_dict = {}

    for c in combos:
        score, calories = p2_calc_score(ingredients, c)

        if score > max_score and calories == 500:
            max_score = score
            best_dict = c
    
    return max_score, best_dict

if __name__ == "__main__":
    data = data_prep(raw_data)
    combos = p1_return_combos(data)
    print(main_p1(data, combos))
    print(main_p2(data, combos))
