from equipment_slots import EquipmentSlots


class Equipment:
    def __init__(self, main_hand=None, off_hand=None):
        self.main_hand = main_hand
        self.off_hand = off_hand

    @property
    def max_hp_bonus(self):
        bonus = 0

        if self.main_hand and self.main_hand.equippable:
            bonus += self.main_hand.equippable.max_hp_bonus

        if self.off_hand and self.off_hand.equippable:
            bonus += self.off_hand.equippable.max_hp_bonus

        return bonus

    @property
    def max_blank_element_bonus(self):
        bonus = 0

        if self.main_hand and self.main_hand.equippable:
            bonus += self.main_hand.equippable.max_blank_element_bonus

        if self.off_hand and self.off_hand.equippable:
            bonus += self.off_hand.equippable.max_blank_element_bonus

        return bonus

    @property
    def max_fire_element_bonus(self):
        bonus = 0

        if self.main_hand and self.main_hand.equippable:
            bonus += self.main_hand.equippable.max_fire_element_bonus

        if self.off_hand and self.off_hand.equippable:
            bonus += self.off_hand.equippable.max_fire_element_bonus

        return bonus

    @property
    def max_hp_bonus(self):
        bonus = 0

        if self.main_hand and self.main_hand.equippable:
            bonus += self.main_hand.equippable.max_hp_bonus

        if self.off_hand and self.off_hand.equippable:
            bonus += self.off_hand.equippable.max_hp_bonus

        return bonus

    @property
    def max_air_element_bonus(self):
        bonus = 0

        if self.main_hand and self.main_hand.equippable:
            bonus += self.main_hand.equippable.max_air_element_bonus

        if self.off_hand and self.off_hand.equippable:
            bonus += self.off_hand.equippable.max_air_element_bonus

        return bonus

    @property
    def max_ice_element_bonus(self):
        bonus = 0

        if self.main_hand and self.main_hand.equippable:
            bonus += self.main_hand.equippable.max_ice_element_bonus

        if self.off_hand and self.off_hand.equippable:
            bonus += self.off_hand.equippable.max_ice_element_bonus

        return bonus

    @property
    def max_lightning_element_bonus(self):
        bonus = 0

        if self.main_hand and self.main_hand.equippable:
            bonus += self.main_hand.equippable.max_lightning_element_bonus

        if self.off_hand and self.off_hand.equippable:
            bonus += self.off_hand.equippable.max_lightning_element_bonus

        return bonus

    @property
    def max_earth_element_bonus(self):
        bonus = 0

        if self.main_hand and self.main_hand.equippable:
            bonus += self.main_hand.equippable.max_earth_element_bonus

        if self.off_hand and self.off_hand.equippable:
            bonus += self.off_hand.equippable.max_earth_element_bonus

        return bonus

    @property
    def max_psychic_element_bonus(self):
        bonus = 0

        if self.main_hand and self.main_hand.equippable:
            bonus += self.main_hand.equippable.max_psychic_element_bonus

        if self.off_hand and self.off_hand.equippable:
            bonus += self.off_hand.equippable.max_psychic_element_bonus

        return bonus

    @property
    def max_water_element_bonus(self):
        bonus = 0

        if self.main_hand and self.main_hand.equippable:
            bonus += self.main_hand.equippable.max_water_element_bonus

        if self.off_hand and self.off_hand.equippable:
            bonus += self.off_hand.equippable.max_water_element_bonus

        return bonus

    @property
    def power_bonus(self):
        bonus = 0

        if self.main_hand and self.main_hand.equippable:
            bonus += self.main_hand.equippable.power_bonus

        if self.off_hand and self.off_hand.equippable:
            bonus += self.off_hand.equippable.power_bonus

        return bonus
        
    @property
    def blank_power_bonus(self):
        bonus = 0

        if self.main_hand and self.main_hand.equippable:
            bonus += self.main_hand.equippable.blank_power_bonus

        if self.off_hand and self.off_hand.equippable:
            bonus += self.off_hand.equippable.blank_power_bonus

        return bonus
        
    @property
    def fire_power_bonus(self):
        bonus = 0

        if self.main_hand and self.main_hand.equippable:
            bonus += self.main_hand.equippable.fire_power_bonus

        if self.off_hand and self.off_hand.equippable:
            bonus += self.off_hand.equippable.fire_power_bonus

        return bonus
        
    @property
    def air_power_bonus(self):
        bonus = 0

        if self.main_hand and self.main_hand.equippable:
            bonus += self.main_hand.equippable.air_power_bonus

        if self.off_hand and self.off_hand.equippable:
            bonus += self.off_hand.equippable.air_power_bonus

        return bonus
        
    @property
    def ice_power_bonus(self):
        bonus = 0

        if self.main_hand and self.main_hand.equippable:
            bonus += self.main_hand.equippable.ice_power_bonus

        if self.off_hand and self.off_hand.equippable:
            bonus += self.off_hand.equippable.ice_power_bonus

        return bonus
        
    @property
    def lightning_power_bonus(self):
        bonus = 0

        if self.main_hand and self.main_hand.equippable:
            bonus += self.main_hand.equippable.lightning_power_bonus

        if self.off_hand and self.off_hand.equippable:
            bonus += self.off_hand.equippable.lightning_power_bonus

        return bonus
        
    @property
    def earth_power_bonus(self):
        bonus = 0

        if self.main_hand and self.main_hand.equippable:
            bonus += self.main_hand.equippable.earth_power_bonus

        if self.off_hand and self.off_hand.equippable:
            bonus += self.off_hand.equippable.earth_power_bonus

        return bonus
        
    @property
    def psychic_power_bonus(self):
        bonus = 0

        if self.main_hand and self.main_hand.equippable:
            bonus += self.main_hand.equippable.psychic_power_bonus

        if self.off_hand and self.off_hand.equippable:
            bonus += self.off_hand.equippable.psychic_power_bonus

        return bonus
        
    @property
    def water_power_bonus(self):
        bonus = 0

        if self.main_hand and self.main_hand.equippable:
            bonus += self.main_hand.equippable.water_power_bonus

        if self.off_hand and self.off_hand.equippable:
            bonus += self.off_hand.equippable.water_power_bonus

        return bonus

    @property
    def defense_bonus(self):
        bonus = 0

        if self.main_hand and self.main_hand.equippable:
            bonus += self.main_hand.equippable.defense_bonus

        if self.off_hand and self.off_hand.equippable:
            bonus += self.off_hand.equippable.defense_bonus

        return bonus
        
    @property
    def blank_defense_bonus(self):
        bonus = 0

        if self.main_hand and self.main_hand.equippable:
            bonus += self.main_hand.equippable.blank_defense_bonus

        if self.off_hand and self.off_hand.equippable:
            bonus += self.off_hand.equippable.blank_defense_bonus

        return bonus
        
    @property
    def fire_defense_bonus(self):
        bonus = 0

        if self.main_hand and self.main_hand.equippable:
            bonus += self.main_hand.equippable.fire_defense_bonus

        if self.off_hand and self.off_hand.equippable:
            bonus += self.off_hand.equippable.fire_defense_bonus

        return bonus
        
    @property
    def air_defense_bonus(self):
        bonus = 0

        if self.main_hand and self.main_hand.equippable:
            bonus += self.main_hand.equippable.air_defense_bonus

        if self.off_hand and self.off_hand.equippable:
            bonus += self.off_hand.equippable.air_defense_bonus

        return bonus
        
    @property
    def ice_defense_bonus(self):
        bonus = 0

        if self.main_hand and self.main_hand.equippable:
            bonus += self.main_hand.equippable.ice_defense_bonus

        if self.off_hand and self.off_hand.equippable:
            bonus += self.off_hand.equippable.ice_defense_bonus

        return bonus
        
    @property
    def lightning_defense_bonus(self):
        bonus = 0

        if self.main_hand and self.main_hand.equippable:
            bonus += self.main_hand.equippable.lightning_defense_bonus

        if self.off_hand and self.off_hand.equippable:
            bonus += self.off_hand.equippable.lightning_defense_bonus

        return bonus
        
    @property
    def earth_defense_bonus(self):
        bonus = 0

        if self.main_hand and self.main_hand.equippable:
            bonus += self.main_hand.equippable.earth_defense_bonus

        if self.off_hand and self.off_hand.equippable:
            bonus += self.off_hand.equippable.earth_defense_bonus

        return bonus
        
    @property
    def psychic_defense_bonus(self):
        bonus = 0

        if self.main_hand and self.main_hand.equippable:
            bonus += self.main_hand.equippable.psychic_defense_bonus

        if self.off_hand and self.off_hand.equippable:
            bonus += self.off_hand.equippable.psychic_defense_bonus

        return bonus
        
    @property
    def water_defense_bonus(self):
        bonus = 0

        if self.main_hand and self.main_hand.equippable:
            bonus += self.main_hand.equippable.water_defense_bonus

        if self.off_hand and self.off_hand.equippable:
            bonus += self.off_hand.equippable.water_defense_bonus

        return bonus

    def toggle_equip(self, equippable_entity):
        results = []

        slot = equippable_entity.equippable.slot

        if slot == EquipmentSlots.MAIN_HAND:
            if self.main_hand == equippable_entity:
                self.main_hand = None
                results.append({'dequipped': equippable_entity})
            else:
                if self.main_hand:
                    results.append({'dequipped': self.main_hand})

                self.main_hand = equippable_entity
                results.append({'equipped': equippable_entity})
        elif slot == EquipmentSlots.OFF_HAND:
            if self.off_hand == equippable_entity:
                self.off_hand = None
                results.append({'dequipped': equippable_entity})
            else:
                if self.off_hand:
                    results.append({'dequipped': self.off_hand})

                self.off_hand = equippable_entity
                results.append({'equipped': equippable_entity})

        return results