import tcod as libtcod
from random import randint

from components.ai import BasicMonster
from components.equipment import EquipmentSlots
from components.equippable import Equippable
from components.fighter import Fighter
from components.item import Item
from components.stairs import Stairs

from entity import Entity
from item_functions import heal
from map_objects.rectangle import Rect
from map_objects.tile import Tile
from random_utils import from_dungeon_level, random_choice_from_dict
from render_functions import RenderOrder
from game_messages import Message

class GameMap:
    def __init__(self, width, height, dungeon_level=1):
        self.width = width
        self.height = height
        self.tiles = self.initialize_tiles()
        self.dungeon_level = dungeon_level

    def initialize_tiles(self):
        tiles = [[Tile(True) for y in range(self.height)] for x in range(self.width)]

        return tiles

    def make_map(self, max_rooms, room_min_size, room_max_size, map_width, map_height, player, entities):
        rooms = []
        num_rooms = 0
        
        center_of_last_room_x = None
        center_of_last_room_y = None
        
        for r in range(max_rooms):
            # random width and height
            w = randint(room_min_size, room_max_size)
            h = randint(room_min_size, room_max_size)
            # random position without going out of the boundaries of the map
            x = randint(0, map_width - w -1 )
            y = randint(0, map_height - h - 1)
            
            # "Rect" class makes rectangles easier to work with
            new_room = Rect(x, y, w, h)
            
            # run though the other rooms and see if they intersect with this one
            for other_room in rooms:
                if new_room.intersect(other_room):
                    break
                    
            else:
                # this means there are no intersections, so this room is valid
                
                # "paint" it to the map's tiles
                self.create_room(new_room)
                
                # center coordinates of new room, will be useful later
                (new_x, new_y) = new_room.center()
                
                center_of_last_room_x = new_x
                center_of_last_room_y = new_y
                
                if num_rooms == 0:
                    # this is the first room, where the player starts at
                    player.x = new_x
                    player.y = new_y
                else:
                    # all rooms after the first:
                    # connect it to the previous room with a tunnel
                    
                    # center coordinates of previous room
                    (prev_x, prev_y) = rooms[num_rooms - 1].center()
                
                    # flip a coin (random number that is either 0 or 1)
                    if randint(0, 1) == 1:
                        # first move horizontally, then vertically
                        self.create_h_tunnel(prev_x, new_x, prev_y)
                        self.create_v_tunnel(prev_y, new_y, new_x)
                    else:
                        # first move vertically, then horizontally
                        self.create_v_tunnel(prev_y, new_y, prev_x)
                        self.create_h_tunnel(prev_x, new_x, new_y)
                        
                self.place_entities(new_room, entities)
                    
                # finally, append the new room to the list
                rooms.append(new_room)
                num_rooms += 1
        
        stairs_component = Stairs(self.dungeon_level +1)
        down_stairs = Entity(center_of_last_room_x, center_of_last_room_y, 265, libtcod.white, 'Stairs',
                            render_order = RenderOrder.STAIRS, stairs=stairs_component)
        entities.append(down_stairs)
            
    def create_room(self,room):
        # go through the tiles in the rectangle and make them passable
        for x in range(room.x1 + 1, room.x2):
            for y in range(room.y1 + 1, room.y2):
                self.tiles[x][y].blocked = False
                self.tiles[x][y].block_sight = False
                
    def create_h_tunnel(self, x1, x2, y):
        for x in range(min(x1, x2), max(x1, x2) +1):
            self.tiles[x][y].blocked = False
            self.tiles[x][y].block_sight = False

    def create_v_tunnel(self, y1, y2, x):
        for y in range(min(y1, y2), max(y1, y2) + 1):
            self.tiles[x][y].blocked = False
            self.tiles[x][y].block_sight = False
    
    def place_entities(self, room, entities):
        # first number indicates how many, second indicates after which dungeon level: ie [2,1] indicates starting with the first level, 2 things can spawn
        max_monsters_per_room = from_dungeon_level([[2, 1], [3, 4], [5, 6]], self.dungeon_level)
        max_items_per_room = from_dungeon_level([[1, 1], [2, 4]], self.dungeon_level)
        
        # Get a random number of monsters
        number_of_monsters = randint(0, max_monsters_per_room)
        number_of_items = randint(0, max_items_per_room)
        
        monster_chances = {
            'small': 80,
            'medium': from_dungeon_level([[15, 3], [30, 5], [60, 7]], self.dungeon_level),
            'large': from_dungeon_level([[10, 6], [20, 8], [30, 10]], self.dungeon_level)
            # add in 'boss' which changes its element randomly each turn
        }
        
        # Define chance for each type
        monster_type_chances = {
            'blank': 25,
            'fire': 25,
            'air': 25,
            'ice': 25,
            'lightning': 25,
            'earth': 25,
            'psychic': 25,
            'water': 25
        }
        
        item_chances = {
            'healing_potion': 50,
            'dagger': 2,
            'shield': 2
            #'art_sword': from_dungeon_level([[5, 1]], self.dungeon_level),
            #'art_shield': from_dungeon_level([[5, 1]], self.dungeon_level),
            #'math_sword': from_dungeon_level([[5, 1]], self.dungeon_level),
            #'math_shield': from_dungeon_level([[5, 1]], self.dungeon_level),
            #'science_sword': from_dungeon_level([[5, 1]], self.dungeon_level),
            #'science_shield': from_dungeon_level([[5, 1]], self.dungeon_level),
            #'english_sword': from_dungeon_level([[5, 1]], self.dungeon_level),
            #'english_shield': from_dungeon_level([[5, 1]], self.dungeon_level),
            #'lightning_scroll': from_dungeon_level([[25, 4]], self.dungeon_level),
            #'fireball_scroll': from_dungeon_level([[25, 6]], self.dungeon_level),
            #'confusion_scroll': from_dungeon_level([[10, 2]], self.dungeon_level)
        }
        
        for i in range(number_of_monsters):
            # Choose a random location in the room
            x = randint(room.x1+1, room.x2-1)
            y = randint(room.y1+1, room.y2-1)
            
            if not any([entity for entity in entities if entity.x == x and entity.y == y]):
                monster_choice = random_choice_from_dict(monster_chances)
                monster_type_choice = random_choice_from_dict(monster_type_chances) # Get random type of monsters
                
                if monster_choice == 'small':
                    if monster_type_choice == 'blank':
                    
                        fighter_component = Fighter(hp=20, defense=0, power=0, blank_element=5, name='exto sprite', xp=1, element='blank')
                        ai_component = BasicMonster()
                        monster = Entity(x, y, 275, libtcod.white, 'exto sprite', blocks = True,
                            render_order=RenderOrder.ACTOR, fighter=fighter_component, ai=ai_component)
                    
                    elif monster_type_choice == 'fire':
                    
                        fighter_component = Fighter(hp=20, defense=0, power=0, fire_element=10, name='infernus sprite', xp=1, element='fire')
                        ai_component = BasicMonster()
                        monster = Entity(x, y, 268, libtcod.white, 'infernus sprite', blocks = True,
                            render_order=RenderOrder.ACTOR, fighter=fighter_component, ai=ai_component)
                    
                    elif monster_type_choice == 'air':
                    
                        fighter_component = Fighter(hp=20, defense=0, power=0, air_element=10, name='sonus sprite', xp=1, element='air')
                        ai_component = BasicMonster()
                        monster = Entity(x, y, 270, libtcod.white, 'sonus sprite', blocks = True,
                            render_order=RenderOrder.ACTOR, fighter=fighter_component, ai=ai_component)
                    
                    elif monster_type_choice == 'ice':
                    
                        fighter_component = Fighter(hp=20, defense=0, power=0, ice_element=10, name='glacius sprite', xp=1, element='ice')
                        ai_component = BasicMonster()
                        monster = Entity(x, y, 271, libtcod.white, 'glacius sprite', blocks = True,
                            render_order=RenderOrder.ACTOR, fighter=fighter_component, ai=ai_component)
                            
                    elif monster_type_choice == 'lightning':
                    
                        fighter_component = Fighter(hp=20, defense=0, power=0, lightning_element=randint(5,15), name='fara sprite', xp=1, element='lightning')
                        ai_component = BasicMonster()
                        monster = Entity(x, y, 273, libtcod.white, 'fara sprite', blocks = True,
                            render_order=RenderOrder.ACTOR, fighter=fighter_component, ai=ai_component)
                            
                    elif monster_type_choice == 'earth':
                    
                        fighter_component = Fighter(hp=20, defense=0, power=0, earth_element=10, name='stowne sprite', xp=1, element='earth')
                        ai_component = BasicMonster()
                        monster = Entity(x, y, 273, libtcod.white, 'stowne sprite', blocks = True,
                            render_order=RenderOrder.ACTOR, fighter=fighter_component, ai=ai_component)
                            
                    elif monster_type_choice == 'psychic':
                    
                        fighter_component = Fighter(hp=20, defense=0, power=0, psychic_element=10, name='hex sprite', xp=1, element='psychic')
                        ai_component = BasicMonster()
                        monster = Entity(x, y, 274, libtcod.white, 'hex sprite', blocks = True,
                            render_order=RenderOrder.ACTOR, fighter=fighter_component, ai=ai_component)
                            
                    elif monster_type_choice == 'water':
                    
                        fighter_component = Fighter(hp=20, defense=0, power=0, water_element=10, name='vapore sprite', xp=1, element='water')
                        ai_component = BasicMonster()
                        monster = Entity(x, y, 269, libtcod.white, 'vapore sprite', blocks = True,
                            render_order=RenderOrder.ACTOR, fighter=fighter_component, ai=ai_component)
                        
                elif monster_choice == 'medium':
                    if monster_type_choice == 'blank':
                    
                        fighter_component = Fighter(hp=35, defense=5, power=0, blank_element=10, name='noxis pool', xp=2, element='blank')
                        ai_component = BasicMonster()
                        monster = Entity(x, y, 283, libtcod.white, 'noxis pool', blocks = True,
                            render_order=RenderOrder.ACTOR, fighter=fighter_component, ai=ai_component)
                    
                    elif monster_type_choice == 'fire':
                    
                        fighter_component = Fighter(hp=35, defense=5, power=0, fire_element=15, name='magmis pool', xp=2, element='fire')
                        ai_component = BasicMonster()
                        monster = Entity(x, y, 276, libtcod.white, 'magmis pool', blocks = True,
                            render_order=RenderOrder.ACTOR, fighter=fighter_component, ai=ai_component)
                    
                    elif monster_type_choice == 'air':
                    
                        fighter_component = Fighter(hp=35, defense=5, power=0, air_element=15, name='tumul pool', xp=2, element='air')
                        ai_component = BasicMonster()
                        monster = Entity(x, y, 278, libtcod.white, 'tumul pool', blocks = True,
                            render_order=RenderOrder.ACTOR, fighter=fighter_component, ai=ai_component)
                    
                    elif monster_type_choice == 'ice':
                    
                        fighter_component = Fighter(hp=35, defense=5, power=0, ice_element=15, name='iglis pool', xp=2, element='ice')
                        ai_component = BasicMonster()
                        monster = Entity(x, y, 279, libtcod.white, 'iglis pool', blocks = True,
                            render_order=RenderOrder.ACTOR, fighter=fighter_component, ai=ai_component)
                            
                    elif monster_type_choice == 'lightning':
                    
                        fighter_component = Fighter(hp=35, defense=5, power=0, lightning_element=randint(10,20), name='galva pool', xp=2, element='lightning')
                        ai_component = BasicMonster()
                        monster = Entity(x, y, 280, libtcod.white, 'galva pool', blocks = True,
                            render_order=RenderOrder.ACTOR, fighter=fighter_component, ai=ai_component)
                            
                    elif monster_type_choice == 'earth':
                    
                        fighter_component = Fighter(hp=35, defense=5, power=0, earth_element=15, name='vivus pool', xp=2, element='earth')
                        ai_component = BasicMonster()
                        monster = Entity(x, y, 281, libtcod.white, 'vivus pool', blocks = True,
                            render_order=RenderOrder.ACTOR, fighter=fighter_component, ai=ai_component)
                            
                    elif monster_type_choice == 'psychic':
                    
                        fighter_component = Fighter(hp=35, defense=5, power=0, psychic_element=15, name='manos pool', xp=2, element='psychic')
                        ai_component = BasicMonster()
                        monster = Entity(x, y, 282, libtcod.white, 'manos pool', blocks = True,
                            render_order=RenderOrder.ACTOR, fighter=fighter_component, ai=ai_component)
                            
                    elif monster_type_choice == 'water':
                    
                        fighter_component = Fighter(hp=35, defense=5, power=0, water_element=15, name='azure pool', xp=2, element='water')
                        ai_component = BasicMonster()
                        monster = Entity(x, y, 277, libtcod.white, 'azure pool', blocks = True,
                            render_order=RenderOrder.ACTOR, fighter=fighter_component, ai=ai_component)
                
                elif monster_choice == 'large':
                    if monster_type_choice == 'blank':
                    
                        fighter_component = Fighter(hp=50, defense=10, power=0, blank_power=15, name='Aeon', xp=4, element='blank')
                        ai_component = BasicMonster()
                        monster = Entity(x, y, 292, libtcod.white, 'Aeon', blocks = True,
                            render_order=RenderOrder.ACTOR, fighter=fighter_component, ai=ai_component)
                    
                    elif monster_type_choice == 'fire':
                    
                        fighter_component = Fighter(hp=50, defense=10, power=3, fire_element=20, name='Kindra', xp=4, element='fire')
                        ai_component = BasicMonster()
                        monster = Entity(x, y, 284, libtcod.white, 'Kindra', blocks = True,
                            render_order=RenderOrder.ACTOR, fighter=fighter_component, ai=ai_component)
                    
                    elif monster_type_choice == 'air':
                    
                        fighter_component = Fighter(hp=50, defense=10, power=3, air_element=20, name='Huricus', xp=4, element='air')
                        ai_component = BasicMonster()
                        monster = Entity(x, y, 286, libtcod.white, 'Huricus', blocks = True,
                            render_order=RenderOrder.ACTOR, fighter=fighter_component, ai=ai_component)
                    
                    elif monster_type_choice == 'ice':
                    
                        fighter_component = Fighter(hp=50, defense=10, power=3, ice_element=20, name='Flaik', xp=4, element='ice')
                        ai_component = BasicMonster()
                        monster = Entity(x, y, 288, libtcod.white, 'Flaik', blocks = True,
                            render_order=RenderOrder.ACTOR, fighter=fighter_component, ai=ai_component)
                            
                    elif monster_type_choice == 'lightning':
                    
                        fighter_component = Fighter(hp=50, defense=10, power=3, lightning_element=randint(20,30), name='Astra', xp=4, element='lightning')
                        ai_component = BasicMonster()
                        monster = Entity(x, y, 289, libtcod.white, 'Astra', blocks = True,
                            render_order=RenderOrder.ACTOR, fighter=fighter_component, ai=ai_component)
                            
                    elif monster_type_choice == 'earth':
                    
                        fighter_component = Fighter(hp=50, defense=10, power=3, earth_element=20, name='Oria', xp=4, element='earth')
                        ai_component = BasicMonster()
                        monster = Entity(x, y, 290, libtcod.white, 'Oria', blocks = True,
                            render_order=RenderOrder.ACTOR, fighter=fighter_component, ai=ai_component)
                            
                    elif monster_type_choice == 'psychic':
                    
                        fighter_component = Fighter(hp=50, defense=10, power=3, psychic_element=20, name='Genis', xp=4, element='psychic')
                        ai_component = BasicMonster()
                        monster = Entity(x, y, 291, libtcod.white, 'Genis', blocks = True,
                            render_order=RenderOrder.ACTOR, fighter=fighter_component, ai=ai_component)
                            
                    elif monster_type_choice == 'water':
                    
                        fighter_component = Fighter(hp=50, defense=10, power=3, water_element=20, name='Aquifis', xp=4, element='water')
                        ai_component = BasicMonster()
                        monster = Entity(x, y, 285, libtcod.white, 'Aquifis', blocks = True,
                            render_order=RenderOrder.ACTOR, fighter=fighter_component, ai=ai_component)
                entities.append(monster)
                
        for i in range(number_of_items):
            x = randint(room.x1+1, room.x2-1)
            y = randint(room.y1+1, room.y2-1)
            
            if not any([entity for entity in entities if entity.x == x and entity.y == y]):
                item_choice = random_choice_from_dict(item_chances)
                
                if item_choice == 'healing_potion':
                    item_component=Item(use_function=heal, amount = 40)
                    item = Entity(x, y, 262, libtcod.white, 'Relaxing Tea', render_order=RenderOrder.ITEM,
                                    item=item_component)
                if item_choice == 'dagger':
                    equippable_component = Equippable(EquipmentSlots.MAIN_HAND, power_bonus= int(self.dungeon_level))
                    item = Entity(x, y, 266, libtcod.white, 'Elemental Absorber + ' + str(self.dungeon_level), equippable=equippable_component)
                if item_choice == 'shield':
                    equippable_component = Equippable(EquipmentSlots.OFF_HAND, defense_bonus= int(self.dungeon_level), max_hp_bonus=self.dungeon_level*5)
                    item = Entity(x, y, 264, libtcod.white, 'Elemental Deflector + ' + str(self.dungeon_level), equippable=equippable_component)
                # elif item_choice == 'art_sword':
                    # equippable_component = Equippable(EquipmentSlots.MAIN_HAND, art_power_bonus=5)
                    # item = Entity(x, y, 267, libtcod.white, 'Paintbrush', equippable=equippable_component)
                # elif item_choice == 'art_shield':
                    # equippable_component = Equippable(EquipmentSlots.OFF_HAND, art_defense_bonus=4)
                    # item = Entity(x, y, 268, libtcod.white, 'Pallete Clipboard', equippable=equippable_component)
                # elif item_choice == 'math_sword':
                    # equippable_component = Equippable(EquipmentSlots.MAIN_HAND, math_power_bonus=5)
                    # item = Entity(x, y, 269, libtcod.white, 'Ruler', equippable=equippable_component)
                # elif item_choice == 'math_shield':
                    # equippable_component = Equippable(EquipmentSlots.OFF_HAND, math_defense_bonus=4)
                    # item = Entity(x, y, 270, libtcod.white, 'Measuring Clipboard', equippable=equippable_component)
                # elif item_choice == 'science_sword':
                    # equippable_component = Equippable(EquipmentSlots.MAIN_HAND, science_power_bonus=5)
                    # item = Entity(x, y, 271, libtcod.white, 'Calculator', equippable=equippable_component)
                # elif item_choice == 'science_shield':
                    # equippable_component = Equippable(EquipmentSlots.OFF_HAND, science_defense_bonus=4)
                    # item = Entity(x, y, 272, libtcod.white, 'Vial Clipboard', equippable=equippable_component)
                # elif item_choice == 'english_sword':
                    # equippable_component = Equippable(EquipmentSlots.MAIN_HAND, english_power_bonus=5)
                    # item = Entity(x, y, 273, libtcod.white, 'Dictionary', equippable=equippable_component)
                # elif item_choice == 'english_shield':
                    # equippable_component = Equippable(EquipmentSlots.OFF_HAND, english_defense_bonus=4)
                    # item = Entity(x, y, 274, libtcod.white, 'Report Clipboard', equippable=equippable_component)
                
                entities.append(item)
    
    def is_blocked(self, x, y):
        if self.tiles[x][y].blocked:
            return True

        return False
        
    def next_floor(self, player, message_log, constants):
        self.dungeon_level += 1
        entities = [player]

        self.tiles = self.initialize_tiles()
        self.make_map(constants['max_rooms'], constants['room_min_size'], constants['room_max_size'],
                      constants['map_width'], constants['map_height'], player, entities)

        player.fighter.heal(player.fighter.max_hp // 2)

        message_log.add_message(Message('You take a moment to rest and relax before the next wave of elements.', libtcod.light_violet))

        return entities