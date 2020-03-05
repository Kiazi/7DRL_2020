import tcod as libtcod

from game_messages import Message

class Fighter:
    def __init__(self, hp, defense, power, name, xp=0, element=None,
                    blank_power=0, blank_defense=0,
                    fire_power=0, fire_defense=0,
                    air_power=0, air_defense=0,
                    ice_power=0, ice_defense=0,
                    lightning_power=0, lightning_defense=0,
                    earth_power=0, earth_defense=0,
                    psychic_power=0, psychic_defense=0,
                    water_power=0, water_defense=0):
        self.base_max_hp = hp
        self.hp = hp
        self.base_defense = defense
        self.base_power = power
        self.name = name
        self.xp = xp
        self.element = element
        #self.art_power = art_power
        #self.art_defense = art_defense
        #self.math_power = math_power
        #self.math_defense = math_defense
        #self.science_power = science_power
        #self.science_defense = science_defense
        #self.english_power = english_power
        #self.english_defense = english_power
        
    @property
    def max_hp(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.max_hp_bonus
        else:
            bonus = 0

        return self.base_max_hp + bonus

    @property
    def power(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.power_bonus
        else:
            bonus = 0

        return self.base_power + bonus
        
    @property
    def blank_power(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.blank_power_bonus
        else:
            bonus = 0

        return bonus
        
    @property
    def fire_power(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.fire_power_bonus
        else:
            bonus = 0

        return bonus
        
    @property
    def air_power(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.air_power_bonus
        else:
            bonus = 0

        return bonus
        
    @property
    def ice_power(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.ice_power_bonus
        else:
            bonus = 0

        return bonus
        
    @property
    def lightning_power(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.lightning_power_bonus
        else:
            bonus = 0

        return bonus
        
    @property
    def earth_power(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.earth_power_bonus
        else:
            bonus = 0

        return bonus
        
    @property
    def psychic_power(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.psychic_power_bonus
        else:
            bonus = 0

        return bonus
        
    @property
    def water_power(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.water_power_bonus
        else:
            bonus = 0

        return bonus

    @property
    def defense(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.defense_bonus
        else:
            bonus = 0

        return self.base_defense + bonus
        
    @property
    def blank_defense(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.blank_defense_bonus
        else:
            bonus = 0

        return bonus
    
    @property
    def fire_defense(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.fire_defense_bonus
        else:
            bonus = 0

        return bonus
        
    @property
    def air_defense(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.air_defense_bonus
        else:
            bonus = 0

        return bonus
        
    @property
    def ice_defense(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.ice_defense_bonus
        else:
            bonus = 0

        return bonus
        
    @property
    def lightning_defense(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.lightning_defense_bonus
        else:
            bonus = 0

        return bonus
        
    @property
    def earth_defense(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.earth_defense_bonus
        else:
            bonus = 0

        return bonus
        
    @property
    def psychic_defense(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.psychic_defense_bonus
        else:
            bonus = 0

        return bonus
        
    @property
    def water_defense(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.water_defense_bonus
        else:
            bonus = 0

        return bonus
        
    def take_damage(self, amount):
        results = []
    
        self.hp -= amount
        
        if self.hp <= 0:
            results.append({'dead': self.owner, 'xp': self.xp})
        
        return results
        
    def heal(self, amount):
        self.hp += amount
        
        if self.hp > self.max_hp:
            self.hp = self.max_hp
        
    def attack(self, target):
        results = []
        
        # Attacking element
        if target.fighter.element != None:
            #calculate all of the damages dealt by element
            base_damage = self.power
            blank_damage = self.blank_power
            fire_damage = self.fire_power*((target.ice_defense)/(target.ice_defense+target.fire_defense)-0.25)*4/3
            air_damage = self.air_power*((target.psychic_defense)/(target.psychic_defense+target.air_defense)-0.25)*4/3
            ice_damage
            lightning_damage
            earth_damage
            psychic_damage
            water_damage
            
            #sum all damage to get total damage dealt
            damage = (base_damage+
            blank_damage+
            fire_damage+
            air_damage+
            ice_damage+
            lightning_damage+
            earth_damage+
            psychic_damage+
            water_damage
            )
            
            #determine the damage type. This can then be printed with str(damage_type)
            if base_damage > max(blank_damage,fire_damage,air_damage,ice_damage,lightning_damage,earth_damage,psychic_damage,water_damage):
                damage_type = 'physical'
                
            elif blank_damage > max(base_damage):
                damage_type = 'true'
            #self.power + self.art_power - target.fighter.defense - target.fighter.art_defense
        
        # Attacking Guardian/player
        elif target.fighter.name == 'Guardian':
            damage = 1
        
        else:
            damage = 0
            
        if damage > 0:
            if self.name == 'Guardian':
                #Add in str(damage_type) as a fourth variable {4} to use. i.e. The Guardian deals 4 fire damage to the ice elemental.
                results.append({'message': Message('The {0} deals {2} damage to the {1}.'.format(
                    self.owner.name.capitalize(), target.name, str(damage)), libtcod.light_green)})
                results.extend(target.fighter.take_damage(damage))
            else:
                results.append({'message': Message('The {0} damages the {1} inflicting {2} damage!'.format(
                    self.owner.name.capitalize(), target.name, str(damage)), libtcod.red)})
                results.extend(target.fighter.take_damage(damage))
        else:
            if self.name == 'Guardian':
                results.append({'message': Message('The {0} can\'t damage the {1}!'.format(
                    self.owner.name.capitalize(), target.name, str(damage)), libtcod.light_red)})
            else:
                results.append({'message': Message('The {0} heals the {1} for {2} health!'.format(
                    self.owner.name.capitalize(), target.name, str(damage)), libtcod.green)})
                
        return results