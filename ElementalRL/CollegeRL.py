import tcod as libtcod

from components.equipment import Equipment
from components.equippable import Equippable
from components.fighter import Fighter
from components.inventory import Inventory
from components.level import Level
from death_functions import kill_monster, kill_player
from entity import Entity, get_blocking_entities_at_location
from equipment_slots import EquipmentSlots
from fov_functions import initialize_fov, recompute_fov
from game_messages import Message, MessageLog
from game_states import GameStates
from input_handlers import handle_keys
from loader_functions.initialize_new_game import get_constants
from map_objects.game_map import GameMap
from render_functions import clear_all, render_all, RenderOrder

def load_customfont():
    # the index of the first custom tile in the file
    a = 256
    
    # the 'y' is the row index, here we load the sixth row in the font file. increase the '6' to load any new rows from the file
    for y in range(5, 6):
        libtcod.console_map_ascii_codes_to_font(a, 32, 0, y)
        a += 32
    #libtcod.console_map_ascii_code_to_font(34,0,3)



def main():
    constants = get_constants()
    
    libtcod.console_set_custom_font('tiledfont.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD, 32, 10)
    
    libtcod.console_init_root(constants['screen_width'], constants['screen_height'], constants['window_title'], False)

    # load the custom font rows
    load_customfont()
    
    # assign the custom font rows numbers to text (for easier calling when defining entities with custom tiles)
    # defining tiles (rather than numbers)
    wall_tile = 256
    floor_tile = 257
    player_tile = 258
    quiz_tile = 259
    exam_tile = 260
    healingpotion_tile = 261
    sword_tile = 263
    shield_tile = 264
    stairsdown_tile = 265
    dagger_tile = 266
    
    fighter_component = Fighter(hp=100, defense=1, power=3, name='Student')
    inventory_component = Inventory(26)
    level_component = Level()
    equipment_component = Equipment()
    player = Entity(0,0, player_tile, libtcod.white, 'Student', blocks=True, render_order=RenderOrder.ACTOR,
                    fighter=fighter_component, inventory=inventory_component, level=level_component,
                    equipment=equipment_component)
    entities = [player]
    
    equippable_component = Equippable(EquipmentSlots.MAIN_HAND, power_bonus=1)
    dagger = Entity(0,0, dagger_tile, libtcod.white, 'Pencil', equippable=equippable_component)
    player.inventory.add_item(dagger)
    player.equipment.toggle_equip(dagger)
    
    con = libtcod.console.Console(constants['screen_width'], constants['screen_height'])
    panel = libtcod.console.Console(constants['screen_width'], constants['panel_height'])

    game_map = GameMap(constants['map_width'], constants['map_height'])
    game_map.make_map(constants['max_rooms'], constants['room_min_size'], constants['room_max_size'],
                      constants['map_width'], constants['map_height'], player, entities)
    
    fov_recompute = True
    
    fov_map = initialize_fov(game_map)
    
    message_log = MessageLog(constants['message_x'], constants['message_width'], constants['message_height'])
    
    key = libtcod.Key()
    mouse = libtcod.Mouse()
    
    game_state = GameStates.PLAYERS_TURN
    previous_game_state = game_state

    # Welcome the player
    message_log.add_message(Message('Welcome, Student, to the College of Doom! Aquire 180 credits to graduate...or die trying!', libtcod.white))
    
    while not libtcod.console_is_window_closed():
        libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS | libtcod.EVENT_MOUSE, key, mouse)
        
        if fov_recompute:
            recompute_fov(fov_map, player.x, player.y, constants['fov_radius'], constants['fov_light_walls'],
                          constants['fov_algorithm'])

        render_all(con, panel, entities, player, game_map, fov_map, fov_recompute, message_log,
                   constants['screen_width'], constants['screen_height'], constants['bar_width'],
                   constants['panel_height'], constants['panel_y'], mouse, constants['colors'], game_state)

        fov_recompute = False
        
        libtcod.console_flush()

        clear_all(con, entities)

        action = handle_keys(key, game_state)

        move = action.get('move')
        pickup = action.get('pickup')
        show_inventory = action.get('show_inventory')
        drop_inventory = action.get('drop_inventory')
        inventory_index = action.get('inventory_index')
        take_stairs = action.get('take_stairs')
        level_up = action.get('level_up')
        show_character_screen = action.get('show_character_screen')
        wait = action.get('wait')
        exit = action.get('exit')
        fullscreen = action.get('fullscreen')
        
        player_turn_results = []

        if move and game_state == GameStates.PLAYERS_TURN:
            dx, dy = move
            destination_x = player.x + dx
            destination_y = player.y + dy
            
            if not game_map.is_blocked(destination_x, destination_y):
                target = get_blocking_entities_at_location(entities, destination_x, destination_y)
                
                if target:
                    attack_results = player.fighter.attack(target)
                    player_turn_results.extend(attack_results)
                    fov_recompute = True
                else:
                    player.move(dx, dy)
                    
                    fov_recompute = True
                    
                game_state = GameStates.ENEMY_TURN

        elif pickup and game_state == GameStates.PLAYERS_TURN:
            for entity in entities:
                if entity.item and entity.x == player.x and entity.y == player.y:
                    pickup_results = player.inventory.add_item(entity)
                    player_turn_results.extend(pickup_results)
                    
                    break
            
            else:
                message_log.add_message(Message('There is nothing here to pick up.', libtcod.yellow))

        if show_inventory:
            previous_game_state = game_state
            game_state = GameStates.SHOW_INVENTORY
        
        if drop_inventory:
            previous_game_state = game_state
            game_state = GameStates.DROP_INVENTORY
            
        if inventory_index is not None and previous_game_state != GameStates.PLAYER_DEAD and inventory_index < len(
                player.inventory.items):
            item = player.inventory.items[inventory_index]
            
            if game_state == GameStates.SHOW_INVENTORY:
                player_turn_results.extend(player.inventory.use(item))
            elif game_state == GameStates.DROP_INVENTORY:
                player_turn_results.extend(player.inventory.drop_item(item))
        
        if take_stairs and game_state == GameStates.PLAYERS_TURN:
            for entity in entities:
                if entity.stairs and entity.x == player.x and entity.y == player.y:
                    entities = game_map.next_floor(player, message_log, constants)
                    fov_map = initialize_fov(game_map)
                    fov_recompute = True
                    con.clear()

                    break
            else:
                message_log.add_message(Message('You search around, but Summer break is nowhere to be seen.', libtcod.yellow))
        
        if level_up:
            if level_up == 'hp':
                player.fighter.base_max_hp += 20
                player.fighter.hp += 20
            elif level_up == 'str':
                player.fighter.base_power += 1
            elif level_up == 'def':
                player.fighter.base_defense += 1

            game_state = previous_game_state
        
        if show_character_screen:
            previous_game_state = game_state
            game_state = GameStates.CHARACTER_SCREEN
        
        if wait == True:
            game_state = GameStates.ENEMY_TURN
            fov_recompute = True
                
        if exit:
            if game_state in (GameStates.SHOW_INVENTORY, GameStates.DROP_INVENTORY, GameStates.CHARACTER_SCREEN):
                game_state = previous_game_state
            else:
                return True

        if fullscreen:
            libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())
        
        for player_turn_result in player_turn_results:
            message = player_turn_result.get('message')
            dead_entity = player_turn_result.get('dead')
            item_added = player_turn_result.get('item_added')
            item_consumed = player_turn_result.get('consumed')
            item_dropped = player_turn_result.get('item_dropped')
            equip = player_turn_result.get('equip')
            
            if message:
                message_log.add_message(message)
            
            if dead_entity:
                if dead_entity == player:
                    message, game_state = kill_player(dead_entity)
                else:
                    message = kill_monster(dead_entity)
                
                message_log.add_message(message)
            
            if item_added:
                entities.remove(item_added)
                
                game_state = GameStates.ENEMY_TURN
            
            if item_consumed:
                game_state = GameStates.ENEMY_TURN
                
            if item_dropped:
                entities.append(item_dropped)
                
                game_state = GameStates.ENEMY_TURN
            
            if equip:
                equip_results = player.equipment.toggle_equip(equip)
                
                for equip_result in equip_results:
                    equipped = equip_result.get('equipped')
                    dequipped = equip_result.get('dequipped')
                    
                    if equipped:
                        message_log.add_message(Message('You equipped the {0}.'.format(equipped.name)))
                        
                    if dequipped:
                        message_log.add_message(Message('You dequipped the {0}.'.format(dequipped.name)))
                        
                game_state = GameStates.ENEMY_TURN
            
            xp = player_turn_result.get('xp')
            
            if xp:
                leveled_up = player.level.add_xp(xp)
                message_log.add_message(Message('You passed the Final Exam and gained {0} credits!'.format(xp)))
                
                if leveled_up:
                    if player.level.current_level == 5:
                        previous_game_state = game_state
                        game_state = GameStates.WIN
                        message_log.add_message(Message('You have completed 180 credits at the College of Doom! You graduated!', libtcod.yellow))
                    else:
                        message_log.add_message(Message(
                            'You made it through another year of school! You move on to school year {0}'.format(
                                player.level.current_level) + '!', libtcod.yellow))
                        previous_game_state = game_state
                        game_state = GameStates.LEVEL_UP

        if game_state == GameStates.ENEMY_TURN:
            for entity in entities:
                if entity.ai:
                    enemy_turn_results = entity.ai.take_turn(player, fov_map, game_map, entities)
                    
                    for enemy_turn_result in enemy_turn_results:
                        message = enemy_turn_result.get('message')
                        dead_entity = enemy_turn_result.get('dead')
                        
                        if message:
                            message_log.add_message(message)
                            
                        if dead_entity:
                            if dead_entity == player:
                                message, game_state = kill_player(dead_entity)
                            else:
                                message = kill_monster(dead_entity)
                            
                            message_log.add_message(message)
                            
                            if game_state == GameStates.PLAYER_DEAD:
                                break
                            
                    if game_state == GameStates.PLAYER_DEAD:
                        break
                        
            else:
                game_state = GameStates.PLAYERS_TURN
            
            fov_recompute = True

if __name__ == '__main__':
     main()