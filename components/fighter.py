import tcod as libtcod

from game_messages import Message

class Fighter:
    def __init__(self, hp, defense, power, name, xp=0, subject=None,
                    art_power=0, art_defense=0,
                    math_power=0, math_defense=0,
                    science_power=0, science_defense=0,
                    english_power=0, english_defense=0):
        self.base_max_hp = hp
        self.hp = hp
        self.base_defense = defense
        self.base_power = power
        self.name = name
        self.xp = xp
        self.subject = subject
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
    def art_power(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.art_power_bonus
        else:
            bonus = 0

        return bonus
        
    @property
    def math_power(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.math_power_bonus
        else:
            bonus = 0

        return bonus
        
    @property
    def science_power(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.science_power_bonus
        else:
            bonus = 0

        return bonus
        
    @property
    def english_power(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.english_power_bonus
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
    def art_defense(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.art_defense_bonus
        else:
            bonus = 0

        return bonus
    
    @property
    def math_defense(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.math_defense_bonus
        else:
            bonus = 0

        return bonus
        
    @property
    def science_defense(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.science_defense_bonus
        else:
            bonus = 0

        return bonus
        
    @property
    def english_defense(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.english_defense_bonus
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
        
        # player attack
        if target.fighter.subject == 'art':
            damage = self.power + self.art_power - target.fighter.defense - target.fighter.art_defense
        
        # player attack
        elif target.fighter.subject == 'math':
            damage = self.power + self.math_power - target.fighter.defense - target.fighter.math_defense
        
        # player attack
        elif target.fighter.subject == 'science':
            damage = self.power + self.science_power - target.fighter.defense - target.fighter.science_defense
        
        # player attack
        elif target.fighter.subject == 'english':
            damage = self.power + self.english_power - target.fighter.defense - target.fighter.english_defense
        
        elif target.fighter.name == 'Guardian':
            if self.subject == 'art':
                damage = self.power - target.fighter.defense - target.fighter.art_defense
            if self.subject == 'math':
                damage = self.power - target.fighter.defense - target.fighter.math_defense
            if self.subject == 'science':
                damage = self.power - target.fighter.defense - target.fighter.science_defense
            if self.subject == 'english':
                damage = self.power - target.fighter.defense - target.fighter.english_defense
        
        else:
            damage = 0
            
        if damage > 0:
            if self.name == 'Guardian':
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