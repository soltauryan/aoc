from dataclasses import dataclass


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
        self,
        hit_points: int,
        damage: int,
        mana_points: int,
    ):
        self.hit_points = hit_points
        self.damage = damage
        self.current_effect = []
        self.mana_points = mana_points
        self.mana_spent = 0

    def 


def p1_data_prep() -> list[Entity]:
    magic_missle = Effect(
        "Magic Missle",
        mana_cost=53,
        mana_recharge_per_turn=0,
        damage_per_turn=4,
        healing_per_turn=0,
        armor_per_turn=0,
        turn_duration=0,
    )
    drain = Effect(
        "Drain",
        mana_cost=73,
        mana_recharge_per_turn=0,
        damage_per_turn=2,
        healing_per_turn=2,
        armor_per_turn=0,
        turn_duration=0,
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
        damage_per_turn=4,
        healing_per_turn=0,
        armor_per_turn=0,
        turn_duration=5,
    )

    return (magic_missle, drain, shield, poison, recharge)


def main_p1() -> int:
    effects = p1_data_prep()
    player = Entity(50, 0, 500)
    boss = Entity(71, 10, 0)


def main_p2(data):
    pass


if __name__ == "__main__":
    main_p1()
    # main_p2(raw_data)
