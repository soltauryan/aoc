from aoc_utils import data_import
from dataclasses import dataclass
from enum import Enum
from itertools import combinations, product

raw_data = data_import.get_input()
store_text = """Weapons:    Cost  Damage  Armor
Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0

Armor:      Cost  Damage  Armor
Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5

Rings:      Cost  Damage  Armor
Damage+1    25     1       0
Damage+2    50     2       0
Damage+3   100     3       0
Defense+1   20     0       1
Defense+2   40     0       2
Defense+3   80     0       3"""

class ItemType(Enum):
    WEAPON = "weapon"
    ARMOR = "armor"
    RING = "ring"

@dataclass
class Item:
    itemtype: ItemType
    name: str
    cost: int
    damage: int
    armor: int


class Entity:
    def __init__(self,
                    hit_points:int,
                    damage:int,
                    armor:int,
                ):
        self.hit_points = hit_points
        self.damage = damage
        self.armor = armor
        self.current_items = []
        self.item_cost = 0

    def __repr__(self):
        return f"""Hit Points: {self.hit_points}\nDamage: {self.damage}\nArmor: {self.armor}"""

    def add_item(self, item:Item) -> None:
        self.current_items.append(item)
        self.damage += item.damage
        self.armor += item.armor
        self.item_cost += item.cost

    def take_damage(self, damage:int) -> None:
        self.damage -= damage

    def calc_attack(self, enemy_armor:int) -> int:
        return max(self.damage - enemy_armor, 1)



def store_data_prep(store_text:str) -> (list[Item], list[Item], list[Item]):
    weapon_str, armor_str, ring_str = store_text.split("\n\n")
    weapons, armors, rings = [], [], []

    for l in weapon_str.splitlines()[1:]:
        name, cost, damage, armor = l.split()
        weapons.append(
            Item(
                ItemType.WEAPON,
                name,
                int(cost),
                int(damage),
                int(armor),
                )
            )

    for l in armor_str.splitlines()[1:]:
        name, cost, damage, armor = l.split()
        armors.append(
            Item(
                ItemType.ARMOR,
                name,
                int(cost),
                int(damage),
                int(armor),
                )
            )

    for l in ring_str.splitlines()[1:]:
        name, cost, damage, armor = l.split()
        rings.append(
            Item(
                ItemType.RING,
                name,
                int(cost),
                int(damage),
                int(armor),
                )
            )

    weapons_choices = combinations(weapons, 1)
    armor_choices = chose_items_up_to(armors, 1)
    ring_choices = chose_items_up_to(rings, 2)

    possible_combos = [
        a + b + c
        for a, b, c in product(weapons_choices, armor_choices, ring_choices)
    ]

    return weapons, armors, rings, possible_combos
        
        
def chose_items_up_to(items, max_n):
    return [
        combo
        for n in range(max_n +1)
        for combo in combinations(items, n)
    ]


def turn(player:Entity, boss:Entity, player_turn:bool):
    if player_turn:
        boss.hit_points -= player.calc_attack(boss.armor)
    else:
        player.hit_points -= boss.calc_attack(player.armor)


def battle(player, boss, print_battle=False):
    player_turn = True
    game_turn = 1
    while player.hit_points > 0 and boss.hit_points > 0:
        if print_battle:
            print(f"Turn {game_turn}")
            print(player,"\n", boss)
            print()
        turn(player, boss, player_turn)
        player_turn = not player_turn
        game_turn += 1
    if player.hit_points <= 0:
        return "Boss Victory"
    else:
        return "Player Victory"

def main_p1():
    weapons, armors, rings, possible_combos = store_data_prep(store_text)
    winning_combos_costs = []

    # Add items to player
    for c in possible_combos:
        player = Entity(100, 0, 0)
        boss = Entity(109, 8, 2)

        # Add items to player
        for item in c:
            player.add_item(item)
        
        if battle(player, boss) == "Player Victory":
            winning_combos_costs.append(player.item_cost)
            if player.item_cost == 8:
                print(c)
                break
  
    print(f"P1 Min Winning Cost: {min(winning_combos_costs)}")

        

def main_p2():
    weapons, armors, rings, possible_combos = store_data_prep(store_text)
    losing_combos_costs = []

    # Add items to player
    for c in possible_combos:
        player = Entity(100, 0, 0)
        boss = Entity(109, 8, 2)

        # Add items to player
        for item in c:
            player.add_item(item)
        
        if battle(player, boss) == "Boss Victory":
            losing_combos_costs.append(player.item_cost)
  
    print(f"P2 Max Losing Cost: {max(losing_combos_costs)}")

if __name__ == "__main__":
    demo = False
    weapons, armors, rings, possible_combos = store_data_prep(store_text)
    main_p1()
    main_p2()

    if demo:
        player = Entity(8, 5, 5)
        boss = Entity(12, 7, 2)
        print(battle(player, boss))
