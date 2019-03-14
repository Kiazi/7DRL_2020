class Equippable:
    def __init__(self, slot, power_bonus=0, defense_bonus=0, max_hp_bonus=0,
                    art_power_bonus=0, art_defense_bonus=0,
                    math_power_bonus=0, math_defense_bonus=0,
                    science_power_bonus=0, science_defense_bonus=0,
                    english_power_bonus=0, english_defense_bonus=0):
        self.slot = slot
        self.power_bonus = power_bonus
        self.defense_bonus = defense_bonus
        self.max_hp_bonus = max_hp_bonus
        self.art_power_bonus = art_power_bonus
        self.art_defense_bonus = art_defense_bonus
        self.math_power_bonus = math_power_bonus
        self.math_defense_bonus = math_defense_bonus
        self.science_power_bonus = science_power_bonus
        self.science_defense_bonus = science_defense_bonus
        self.english_power_bonus = english_power_bonus
        self.english_defense_bonus = english_defense_bonus