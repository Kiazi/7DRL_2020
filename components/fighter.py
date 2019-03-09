import tcod as libtcod

from game_messages import Message

class Fighter:
    def __init__(self, hp, defense, power, name):
        self.max_hp = hp
        self.hp = hp
        self.defense = defense
        self.power = power
        self.name = name
        
    def take_damage(self, amount):
        results = []
    
        self.hp -= amount
        
        if self.hp <= 0:
            results.append({'dead': self.owner})
        
        return results
        
    def attack(self, target):
        results = []
        
        damage = self.power - target.fighter.defense
        
        if damage > 0:
            if self.name == 'Student':
                results.append({'message': Message('The {0} finishes {2} problems on the {1}.'.format(
                    self.owner.name.capitalize(), target.name, str(damage)), libtcod.white)})
                results.extend(target.fighter.take_damage(damage))
            else:
                results.append({'message': Message('The {0} stresses out the {1} inflicting {2} stress!'.format(
                    self.owner.name.capitalize(), target.name, str(damage)), libtcod.white)})
                results.extend(target.fighter.take_damage(damage))
        else:
            if self.name == 'Student':
                results.append({'message': Message('The {0} can`t figure out any problems on the {1}!'.format(
                    self.owner.name.capitalize(), target.name), libtcod.white)})
            else:
                results.append({'message': Message('The {0} attempts to stress out the {1} but {1}`s got this {0} in the bag!'.format(
                    self.owner.name.capitalize(), target.name), libtcod.white)})
                
        return results