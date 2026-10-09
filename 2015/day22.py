from aoc_utils.performance import time_function
from dataclasses import dataclass
import random


@dataclass
class Effect:
    name: str
    mana_cost: int
    mana_recharge_per_turn: int
    damage_per_turn: int
    healing_per_turn: int
    armor_per_turn: int
    turn_duration: int


class Entity:
    def __init__(
        self, hit_points: int, damage: int, mana_points: int, is_player: bool = True
    ):
        self.hit_points = hit_points
        self.damage = damage
        self.current_effects = []
        self.mana_points = mana_points
        self.mana_spent = 0
        self.is_player = is_player

    def add_effect(self, effect: Effect) -> None:
        self.current_effects.append(effect)

    def process_effects(self, other: "Entity"):
        next_turn_effects = []
        # Reset armor to 0 for each turn for the player
        self.armor = 0

        for effect in self.current_effects:
            other.hit_points -= effect.damage_per_turn
            self.hit_points += effect.healing_per_turn
            self.armor += effect.armor_per_turn

            effect.turn_duration -= 1
            if effect.turn_duration > 0:
                next_turn_effects.append(effect)

        self.current_effects = next_turn_effects

    def attack(self, other: "Entity") -> None:
        other.hit_points -= max(self.damage - other.armor, 1)


def turn(player: Entity, boss:Entity, effects: list[Effect]):
    next_effect = random.choice(effects)
    player.add_effect(next_effect)
    player.process_effects(boss)
    boss.attack(player)

    


def p1_data_prep() -> list[Effect]:
    magic_missle = Effect(
        "Magic Missle",
        mana_cost=53,
        mana_recharge_per_turn=0,
        damage_per_turn=4,
        healing_per_turn=0,
        armor_per_turn=0,
        turn_duration=1,
    )
    drain = Effect(
        "Drain",
        mana_cost=73,
        mana_recharge_per_turn=0,
        damage_per_turn=2,
        healing_per_turn=2,
        armor_per_turn=0,
        turn_duration=1,
    )
    shield = Effect(
        "Shield",
        mana_cost=113,
        mana_recharge_per_turn=0,
        damage_per_turn=0,
        healing_per_turn=0,
        armor_per_turn=7,
        turn_duration=6,
    )
    poison = Effect(
        "Poison",
        mana_cost=173,
        mana_recharge_per_turn=0,
        damage_per_turn=3,
        healing_per_turn=0,
        armor_per_turn=0,
        turn_duration=6,
    )
    recharge = Effect(
        "Recharge",
        mana_cost=229,
        mana_recharge_per_turn=101,
        damage_per_turn=0,
        healing_per_turn=0,
        armor_per_turn=0,
        turn_duration=5,
    )

    return [magic_missle, drain, shield, poison, recharge]


@time_function
def main_p1() -> int:
    effects = p1_data_prep()
    player = Entity(50, 0, 500)
    boss = Entity(71, 10, 0)

    turn(player, boss, effects)


@time_function
def main_p2(data):
    pass


if __name__ == "__main__":
    main_p1()
    # main_p2(raw_data)
