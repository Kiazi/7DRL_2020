import tcod as libtcod

from game_messages import Message

class Fighter:
    def __init__(self, hp, defense, power, name, xp=0, element=None,
                    blank_power=1, blank_defense=0, blank_element=0,
                    fire_power=0, fire_defense=0, fire_element=0,
                    air_power=0, air_defense=0, air_element=0,
                    ice_power=0, ice_defense=0, ice_element=0,
                    lightning_power=0, lightning_defense=0, lightning_element=0,
                    earth_power=0, earth_defense=0, earth_element=0,
                    psychic_power=0, psychic_defense=0, psychic_element=0,
                    water_power=0, water_defense=0, water_element=0):
        self.base_max_hp = hp
        self.hp = hp
        self.base_defense = defense
        self.base_power = power
        self.name = name
        self.xp = xp
        self.element = element
        self.base_max_blank_element = 5
        self.base_max_fire_element = 15
        self.base_max_air_element = 15
        self.base_max_ice_element = 15
        self.base_max_lightning_element = 15
        self.base_max_earth_element = 15
        self.base_max_psychic_element = 15
        self.base_max_water_element = 15
        # self.blank_power = blank_power
        # self.blank_defense = blank_defense
        self.blank_element = blank_element
        # self.fire_power = fire_power
        # self.fire_defense = fire_defense
        self.fire_element = fire_element
        # self.air_power = air_power
        # self.air_defense = air_defense
        self.air_element = air_element
        # self.ice_power = ice_power
        # self.ice_defense = ice_defense
        self.ice_element = ice_element
        # self.lightning_power = lightning_power
        # self.lightning_defense = lightning_defense
        self.lightning_element = lightning_element
        # self.earth_power = earth_power
        # self.earth_defense = earth_defense
        self.earth_element = earth_element
        # self.psychic_power = psychic_power
        # self.psychic_defense = psychic_defense
        self.psychic_element = psychic_element
        # self.water_power = water_power
        # self.water_defense = water_defense
        self.water_element = water_element
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
    def max_blank_element(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.max_blank_element_bonus
        else:
            bonus = 0

        return self.base_max_blank_element + bonus
        
    @property
    def max_fire_element(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.max_fire_element_bonus
        else:
            bonus = 0

        return self.base_max_fire_element + bonus
        
    @property
    def max_air_element(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.max_air_element_bonus
        else:
            bonus = 0

        return self.base_max_air_element + bonus
        
    @property
    def max_ice_element(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.max_ice_element_bonus
        else:
            bonus = 0

        return self.base_max_ice_element + bonus
        
    @property
    def max_lightning_element(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.max_lightning_element_bonus
        else:
            bonus = 0

        return self.base_max_lightning_element + bonus
        
    @property
    def max_earth_element(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.max_earth_element_bonus
        else:
            bonus = 0

        return self.base_max_earth_element + bonus
        
    @property
    def max_psychic_element(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.max_psychic_element_bonus
        else:
            bonus = 0

        return self.base_max_psychic_element + bonus
        
    @property
    def max_water_element(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.max_water_element_bonus
        else:
            bonus = 0

        return self.base_max_water_element + bonus

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

        return self.blank_element + bonus
        
    @property
    def fire_power(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.fire_power_bonus
        else:
            bonus = 0

        return self.fire_element + bonus
        
    @property
    def air_power(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.air_power_bonus
        else:
            bonus = 0

        return self.air_element + bonus
        
    @property
    def ice_power(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.ice_power_bonus
        else:
            bonus = 0

        return self.ice_element + bonus
        
    @property
    def lightning_power(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.lightning_power_bonus
        else:
            bonus = 0

        return self.lightning_element + bonus
        
    @property
    def earth_power(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.earth_power_bonus
        else:
            bonus = 0

        return self.earth_element + bonus
        
    @property
    def psychic_power(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.psychic_power_bonus
        else:
            bonus = 0

        return self.psychic_element + bonus
        
    @property
    def water_power(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.water_power_bonus
        else:
            bonus = 0

        return self.water_element + bonus

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

        return self.blank_element + bonus
    
    @property
    def fire_defense(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.fire_defense_bonus
        else:
            bonus = 0

        return self.fire_element + bonus
        
    @property
    def air_defense(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.air_defense_bonus
        else:
            bonus = 0

        return self.air_element + bonus
        
    @property
    def ice_defense(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.ice_defense_bonus
        else:
            bonus = 0

        return self.ice_element + bonus
        
    @property
    def lightning_defense(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.lightning_defense_bonus
        else:
            bonus = 0

        return self.lightning_element + bonus
        
    @property
    def earth_defense(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.earth_defense_bonus
        else:
            bonus = 0

        return self.earth_element + bonus
        
    @property
    def psychic_defense(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.psychic_defense_bonus
        else:
            bonus = 0

        return self.psychic_element + bonus
        
    @property
    def water_defense(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.water_defense_bonus
        else:
            bonus = 0

        return self.water_element + bonus
        
    def take_damage(self, amount):
        results = []
    
        self.hp -= amount
        
        if self.hp > self.max_hp:
            self.hp = self.max_hp
        
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
            if target.fighter.ice_defense == 0 and target.fighter.fire_defense == 0:
                fire_damage = self.fire_power*1/3
            else:
                fire_damage = self.fire_power*((target.fighter.ice_defense)/(target.fighter.ice_defense+target.fighter.fire_defense)-0.25)*4/3
            
            if target.fighter.psychic_defense == 0 and target.fighter.air_defense == 0:
                air_damage = self.air_power*1/3
            else:
                air_damage = self.air_power*((target.fighter.psychic_defense)/(target.fighter.psychic_defense+target.fighter.air_defense)-0.25)*4/3
            
            if target.fighter.earth_defense == 0 and target.fighter.ice_defense == 0:
                ice_damage = self.ice_power*1/3
            else:
                ice_damage = self.ice_power*((target.fighter.earth_defense)/(target.fighter.earth_defense+target.fighter.ice_defense)-0.25)*4/3
            
            if target.fighter.water_defense == 0 and target.fighter.lightning_defense == 0:
                lightning_damage = self.lightning_power*1/3
            else:
                lightning_damage = self.lightning_power*((target.fighter.water_defense)/(target.fighter.water_defense+target.fighter.lightning_defense)-0.25)*4/3
            
            if target.fighter.air_defense == 0 and target.fighter.earth_defense == 0:
                earth_damage = self.earth_power*1/3
            else:
                earth_damage = self.earth_power*((target.fighter.air_defense)/(target.fighter.air_defense+target.fighter.earth_defense)-0.25)*4/3
            
            if target.fighter.lightning_defense == 0 and target.fighter.psychic_defense == 0:
                psychic_damage = self.psychic_power*1/3
            else:
                psychic_damage = self.psychic_power*((target.fighter.lightning_defense)/(target.fighter.lightning_defense+target.fighter.psychic_defense)-0.25)*4/3
            
            if target.fighter.fire_defense == 0 and target.fighter.water_defense == 0:
                water_damage = self.water_power*1/3
            else:
                water_damage = self.water_power*((target.fighter.fire_defense)/(target.fighter.fire_defense+target.fighter.water_defense)-0.25)*4/3
            
            #sum all damage to get total damage dealt, then round to nearest integer
            damage = int(round(base_damage+
            blank_damage+
            fire_damage+
            air_damage+
            ice_damage+
            lightning_damage+
            earth_damage+
            psychic_damage+
            water_damage
            ,0))
            
            #determine the damage type. This can then be printed with str(damage_type)
            if base_damage > max(blank_damage,fire_damage,air_damage,ice_damage,lightning_damage,earth_damage,psychic_damage,water_damage):
                damage_type = 'physical'
                
            elif blank_damage > max(base_damage,fire_damage,air_damage,ice_damage,lightning_damage,earth_damage,psychic_damage,water_damage):
                damage_type = 'true'
                
            elif fire_damage > max(base_damage,blank_damage,air_damage,ice_damage,lightning_damage,earth_damage,psychic_damage,water_damage):
                damage_type = 'fire'
                
            elif air_damage > max(base_damage,blank_damage,fire_damage,ice_damage,lightning_damage,earth_damage,psychic_damage,water_damage):
                damage_type = 'air'
                
            elif ice_damage > max(base_damage,blank_damage,fire_damage,air_damage,lightning_damage,earth_damage,psychic_damage,water_damage):
                damage_type = 'ice'
                
            elif lightning_damage > max(base_damage,blank_damage,fire_damage,air_damage,ice_damage,earth_damage,psychic_damage,water_damage):
                damage_type = 'lightning'
                
            elif earth_damage > max(base_damage,blank_damage,fire_damage,air_damage,ice_damage,lightning_damage,psychic_damage,water_damage):
                damage_type = 'earth'
                
            elif psychic_damage > max(base_damage,blank_damage,fire_damage,air_damage,ice_damage,lightning_damage,earth_damage,water_damage):
                damage_type = 'psychic'
            
            elif water_damage > max(base_damage,blank_damage,fire_damage,air_damage,ice_damage,lightning_damage,earth_damage,psychic_damage):
                damage_type = 'water'
                
            else:
                damage_type = 'physical'
        
        # Attacking Guardian/player
        elif target.fighter.name == 'Guardian':
            #calculate all of the damages dealt by element
            base_damage = self.power
            blank_damage = self.blank_power
            if target.fighter.ice_defense == 0 and target.fighter.fire_defense == 0:
                fire_damage = self.fire_power*1/3
            else:
                fire_damage = self.fire_power*((target.fighter.ice_defense)/(target.fighter.ice_defense+target.fighter.fire_defense)-0.25)*4/3
            
            if target.fighter.psychic_defense == 0 and target.fighter.air_defense == 0:
                air_damage = self.air_power*1/3
            else:
                air_damage = self.air_power*((target.fighter.psychic_defense)/(target.fighter.psychic_defense+target.fighter.air_defense)-0.25)*4/3
            
            if target.fighter.earth_defense == 0 and target.fighter.ice_defense == 0:
                ice_damage = self.ice_power*1/3
            else:
                ice_damage = self.ice_power*((target.fighter.earth_defense)/(target.fighter.earth_defense+target.fighter.ice_defense)-0.25)*4/3
            
            if target.fighter.water_defense == 0 and target.fighter.lightning_defense == 0:
                lightning_damage = self.lightning_power*1/3
            else:
                lightning_damage = self.lightning_power*((target.fighter.water_defense)/(target.fighter.water_defense+target.fighter.lightning_defense)-0.25)*4/3
            
            if target.fighter.air_defense == 0 and target.fighter.earth_defense == 0:
                earth_damage = self.earth_power*1/3
            else:
                earth_damage = self.earth_power*((target.fighter.air_defense)/(target.fighter.air_defense+target.fighter.earth_defense)-0.25)*4/3
            
            if target.fighter.lightning_defense == 0 and target.fighter.psychic_defense == 0:
                psychic_damage = self.psychic_power*1/3
            else:
                psychic_damage = self.psychic_power*((target.fighter.lightning_defense)/(target.fighter.lightning_defense+target.fighter.psychic_defense)-0.25)*4/3
            
            if target.fighter.fire_defense == 0 and target.fighter.water_defense == 0:
                water_damage = self.water_power*1/3
            else:
                water_damage = self.water_power*((target.fighter.fire_defense)/(target.fighter.fire_defense+target.fighter.water_defense)-0.25)*4/3
            
            #sum all damage to get total damage dealt, then round to nearest integer
            damage = int(round(base_damage+
            blank_damage+
            fire_damage+
            air_damage+
            ice_damage+
            lightning_damage+
            earth_damage+
            psychic_damage+
            water_damage-
            target.fighter.defense,0))
            
            #determine the damage type. This can then be printed with str(damage_type)
            if base_damage > max(blank_damage,fire_damage,air_damage,ice_damage,lightning_damage,earth_damage,psychic_damage,water_damage):
                damage_type = 'physical'
                
            elif blank_damage > max(base_damage,fire_damage,air_damage,ice_damage,lightning_damage,earth_damage,psychic_damage,water_damage):
                damage_type = 'true'
                
            elif fire_damage > max(base_damage,blank_damage,air_damage,ice_damage,lightning_damage,earth_damage,psychic_damage,water_damage):
                damage_type = 'fire'
                
            elif air_damage > max(base_damage,blank_damage,fire_damage,ice_damage,lightning_damage,earth_damage,psychic_damage,water_damage):
                damage_type = 'air'
                
            elif ice_damage > max(base_damage,blank_damage,fire_damage,air_damage,lightning_damage,earth_damage,psychic_damage,water_damage):
                damage_type = 'ice'
                
            elif lightning_damage > max(base_damage,blank_damage,fire_damage,air_damage,ice_damage,earth_damage,psychic_damage,water_damage):
                damage_type = 'lightning'
                
            elif earth_damage > max(base_damage,blank_damage,fire_damage,air_damage,ice_damage,lightning_damage,psychic_damage,water_damage):
                damage_type = 'earth'
                
            elif psychic_damage > max(base_damage,blank_damage,fire_damage,air_damage,ice_damage,lightning_damage,earth_damage,water_damage):
                damage_type = 'psychic'
            
            elif water_damage > max(base_damage,blank_damage,fire_damage,air_damage,ice_damage,lightning_damage,earth_damage,psychic_damage):
                damage_type = 'water'
                
            else:
                damage_type = 'physical'
        
        else:
            damage = 0
        
        damage_color =  libtcod.white
        if damage_type == 'physical':
            damage_color = libtcod.light_gray
        elif damage_type == 'true':
            damage_color = libtcod.white
        elif damage_type == 'fire':
            damage_color = libtcod.orange
        elif damage_type == 'air':
            damage_color = libtcod.Color(210,233,175)
        elif damage_type == 'ice':
            damage_color = libtcod.Color(173,216,230)
        elif damage_type == 'lightning':
            damage_color = libtcod.light_yellow
        elif damage_type == 'earth':
            damage_color = libtcod.light_orange
        elif damage_type == 'psychic':
            damage_color = libtcod.light_purple
        elif damage_type == 'water':
            damage_color = libtcod.light_blue
        
        if damage > 0:
            if self.name == 'Guardian':
                #Add in str(damage_type) as a fourth variable {3} to use. i.e. The Guardian deals 4 fire damage to the ice elemental.
                results.append({'message': Message('The {0} deals {2} {3} damage to the {1}.'.format(
                    self.owner.name, target.name, str(damage), damage_type), damage_color)})
                results.extend(target.fighter.take_damage(damage))
            else:
                results.append({'message': Message('The {0} deals {2} {3} damage to the {1}.'.format(
                    self.owner.name, target.name, str(damage), damage_type), damage_color)})
                results.extend(target.fighter.take_damage(damage))
        elif damage < 0:
            if self.name == 'Guardian':
                results.append({'message': Message('The {0} heals the {1} for {2} health!'.format(
                    self.owner.name, target.name, str(-damage), damage_type), libtcod.light_red)})
                results.extend(target.fighter.take_damage(damage))
            else:
                results.append({'message': Message('The {0} heals the {1} for {2} health!'.format(
                    self.owner.name, target.name, str(-damage), damage_type), libtcod.dark_green)})
                results.extend(target.fighter.take_damage(damage))
        else:
            if self.name == 'Guardian':
                results.append({'message': Message('The {0} can\'t damage the {1}!'.format(
                    self.owner.name, target.name, str(damage), damage_type), libtcod.yellow)})
            else:
                results.append({'message': Message('The {0} can\'t damage the {1}!'.format(
                    self.owner.name.capitalize(), target.name, str(damage), damage_type), libtcod.yellow)})
                
        return results