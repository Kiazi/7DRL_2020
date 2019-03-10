import tcod as libtcod

from game_states import GameStates

def handle_keys(key, game_state):
    if game_state == GameStates.PLAYERS_TURN:
        return handle_player_turn_keys(key)
    elif game_state == GameStates.PLAYER_DEAD:
        return handle_player_dead_keys(key)
    elif game_state in (GameStates.SHOW_INVENTORY, GameStates.DROP_INVENTORY):
        return handle_inventory_keys(key)
    elif game_state == GameStates.LEVEL_UP:
        return handle_level_up_menu(key)
    elif game_state == GameStates.CHARACTER_SCREEN:
        return handle_character_screen(key)
    
    return {}

def handle_inventory_keys(key):
    index = key.c - ord('a')
    
    if index >= 0:
        return {'inventory_index': index}
    
    if key.vk == libtcod.KEY_ENTER and key.lalt:
        # Alt+Enter: toggle full screen
        return {'fullscreen': True}
    elif key.vk == libtcod.KEY_ESCAPE:
        # Exit the game
        return {'exit': True}
    
    return {}
    
def handle_player_turn_keys(key):
    key_char = chr(key.c)

    # Movement keys
    if key.vk == libtcod.KEY_UP or key_char == 'k' or key.vk == libtcod.KEY_KP8:
        return {'move': (0, -1)}
    elif key.vk == libtcod.KEY_DOWN or key_char == 'j' or key.vk == libtcod.KEY_KP2:
        return {'move': (0, 1)}
    elif key.vk == libtcod.KEY_LEFT or key_char == 'h' or key.vk == libtcod.KEY_KP4:
        return {'move': (-1, 0)}
    elif key.vk == libtcod.KEY_RIGHT or key_char == 'l' or key.vk == libtcod.KEY_KP6:
        return {'move': (1, 0)}
    elif key_char == 'y' or key.vk == libtcod.KEY_KP7:
        return {'move': (-1, -1)}
    elif key_char == 'u' or key.vk == libtcod.KEY_KP9:
        return {'move': (1, -1)}
    elif key_char == 'b' or key.vk == libtcod.KEY_KP1:
        return {'move': (-1, 1)}
    elif key_char == 'n' or key.vk == libtcod.KEY_KP3:
        return {'move': (1, 1)}
    elif key.vk == libtcod.KEY_KP5:
        return {'wait': True}
    elif key.vk == libtcod.KEY_ENTER:
        return {'take_stairs': True}
    elif key_char == 'c':
        return {'show_character_screen': True}
    
    # Pick up item
    if key_char == 'g':
        return {'pickup': True}
        
    # Drop item
    if key_char == 'd':
        return {'drop_inventory': True}
        
    # Open/close inventory
    if key_char == 'i':
        return {'show_inventory': True}

    if key.vk == libtcod.KEY_ENTER and key.lalt:
        # Alt+Enter: toggle full screen
        return {'fullscreen': True}
    elif key.vk == libtcod.KEY_ESCAPE:
        # Exit the game
        return {'exit': True}
        
    # No key was pressed
    return {}
    
def handle_level_up_menu(key):
    if key:
        key_char = chr(key.c)

        if key_char == 'a':
            return {'level_up': 'hp'}
        elif key_char == 'b':
            return {'level_up': 'str'}
        elif key_char == 'c':
            return {'level_up': 'def'}

    return {}
    
def handle_character_screen(key):
    key_char = chr(key.c)
    
    if key.vk == libtcod.KEY_ESCAPE:
        return {'exit': True}
    if key_char == 'c':
        return {'exit': True}
    
    return {}
    
def handle_player_dead_keys(key):
    key_char = chr(key.c)
    
    if key_char == 'i':
        return {'show_inventory': True}
    elif key_char == 'c':
        return {'show_character_screen': True}
        
    if key.vk == libtcod.KEY_ENTER and key.lalt:
        # Alt+Enter: toggle full screen
        return {'fullscreen': True}
    elif key.vk == libtcod.KEY_ESCAPE:
        # Exit the game
        return {'exit': True}

    return {}