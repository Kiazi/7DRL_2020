import tcod as libtcod

from enum import Enum, auto

from game_states import GameStates

from menus import character_screen, inventory_menu, level_up_menu

class RenderOrder(Enum):
    STAIRS = auto()
    CORPSE = auto()
    ITEM = auto()
    ACTOR = auto()

def get_names_under_mouse(mouse, entities, fov_map):
    (x, y) = (mouse.cx, mouse.cy)

    names = [entity.name for entity in entities
             if entity.x == x and entity.y == y and libtcod.map_is_in_fov(fov_map, entity.x, entity.y)]
    names = ', '.join(names)

    return names.capitalize()
    
def render_bar(panel, x, y, total_width, name, value, maximum, bar_color, back_color, text_color):
    bar_width = int(float(value) / maximum * total_width)
    
    libtcod.console_set_default_background(panel, back_color)
    libtcod.console_rect(panel, x, y, total_width, 1, False, libtcod.BKGND_SCREEN)
    
    libtcod.console_set_default_background(panel, bar_color)
    if bar_width > 0:
        libtcod.console_rect(panel, x, y, bar_width, 1, False, libtcod.BKGND_SCREEN)
        
    libtcod.console_set_default_foreground(panel, text_color)
    libtcod.console_print_ex(panel, x, y, libtcod.BKGND_NONE, libtcod.LEFT,
                '{0}:{1}/{2}'.format(name, value, maximum))
    
def render_all(con, panel, entities, player, game_map, fov_map, fov_recompute, message_log, screen_width, screen_height,
                bar_width, panel_height, panel_y, mouse, colors, game_state):
    if fov_recompute:
        # Draw all the visible tiles in the game map
        for y in range(game_map.height):
            for x in range(game_map.width):
                visible = libtcod.map_is_in_fov(fov_map, x, y)
                wall = game_map.tiles[x][y].block_sight
                wall_tile = 257
                floor_tile = 256
                if visible:
                    if wall:
                        libtcod.console_put_char_ex(con, x, y, wall_tile, libtcod.white, libtcod.black)
                    else:
                        libtcod.console_put_char_ex(con, x, y, floor_tile, libtcod.white, libtcod.black)
                    game_map.tiles[x][y].explored = True
                elif game_map.tiles[x][y].explored:
                    if wall:
                        libtcod.console_put_char_ex(con, x, y, wall_tile, libtcod.grey, libtcod.black)
                    else:
                        libtcod.console_put_char_ex(con, x, y, floor_tile, libtcod.grey, libtcod.black)

    entities_in_render_order = sorted(entities, key=lambda x: x.render_order.value)
    
                        
    # Draw all entities in the list
    for entity in entities_in_render_order:
        visible = libtcod.map_is_in_fov(fov_map, entity.x, entity.y)
        x = entity.x
        y = entity.y
        if visible:
            draw_entity(con, entity, fov_map, game_map)
        else:
            floor_tile = 256
            if game_map.tiles[x][y].explored == True:
                if entity.stairs:
                    stairsdown_tile = 265
                    libtcod.console_put_char_ex(con, x, y, stairsdown_tile, libtcod.white, libtcod.black)
                else:
                    libtcod.console_put_char_ex(con, x, y, floor_tile, libtcod.grey, libtcod.black)
            else:
                libtcod.console_put_char_ex(con, x, y, floor_tile, libtcod.black, libtcod.black)

    libtcod.console_blit(con, 0, 0, screen_width, screen_height, 0, 0, 0)
    
    if game_state in (GameStates.SHOW_INVENTORY, GameStates.DROP_INVENTORY):
        if game_state == GameStates.SHOW_INVENTORY:
            inventory_title = 'Press the key next to an item to use it, or Esc to cancel.\n'
        else:
            inventory_title = 'Press the key next to an item to drop it, or Esc to cancel.\n'
        
        inventory_menu(con, inventory_title, player, 50, screen_width, screen_height)
    
    libtcod.console_set_default_background(panel, libtcod.black)
    libtcod.console_clear(panel)
    
    if game_state == GameStates.LEVEL_UP:
        level_up_menu(con, 'You gain knowledge of how to best use the elements...select a stat to raise:', player, screen_width-2, screen_width, screen_height)
    
    elif game_state == GameStates.CHARACTER_SCREEN:
        character_screen(player, 35, 10, screen_width, screen_height)
    
    # Print the game messages, one line at a time
    y = 1
    for message in message_log.messages:
        libtcod.console_set_default_foreground(panel, message.color)
        libtcod.console_print_ex(panel, message_log.x, y, libtcod.BKGND_NONE, libtcod.LEFT, message.text)
        y += 1
    
    render_bar(panel, 1, 1, bar_width, 'Health', player.fighter.hp, player.fighter.max_hp,
                libtcod.orange, libtcod.darker_orange, libtcod.black)
    # elemental render bars to display element levels
    render_bar(panel, 1, 2, bar_width, 'Blank', player.fighter.blank_element, player.fighter.max_blank_element,
                libtcod.orange, libtcod.darker_orange, libtcod.black)
    render_bar(panel, 1, 7, bar_width, ' Fire', player.fighter.fire_element, player.fighter.max_fire_element,
                libtcod.orange, libtcod.darker_orange, libtcod.black)
    render_bar(panel, 1, 8, bar_width, '  Air', player.fighter.air_element, player.fighter.max_air_element,
                libtcod.orange, libtcod.darker_orange, libtcod.black)
    render_bar(panel, 1, 9, bar_width, '  Ice', player.fighter.ice_element, player.fighter.max_ice_element,
                libtcod.orange, libtcod.darker_orange, libtcod.black)
    render_bar(panel, 1, 3, bar_width, 'Light', player.fighter.lightning_element, player.fighter.max_lightning_element,
                libtcod.orange, libtcod.darker_orange, libtcod.black)
    render_bar(panel, 1, 4, bar_width, 'Earth', player.fighter.earth_element, player.fighter.max_earth_element,
                libtcod.orange, libtcod.darker_orange, libtcod.black)
    render_bar(panel, 1, 5, bar_width, 'Psych', player.fighter.psychic_element, player.fighter.max_psychic_element,
                libtcod.orange, libtcod.darker_orange, libtcod.black)
    render_bar(panel, 1, 6, bar_width, 'Water', player.fighter.water_element, player.fighter.max_water_element,
                libtcod.orange, libtcod.darker_orange, libtcod.black)
                
                
    libtcod.console_set_default_foreground(panel, libtcod.light_gray)
    libtcod.console_print_ex(panel, 1, 0, libtcod.BKGND_NONE, libtcod.LEFT,
                             'Depth: {0}'.format(game_map.dungeon_level))
                
    libtcod.console_print_ex(panel, 1, 0, libtcod.BKGND_NONE, libtcod.LEFT,
                                get_names_under_mouse(mouse, entities, fov_map))
                
    libtcod.console_blit(panel, 0, 0, screen_width, panel_height, 0, 0, panel_y)


def clear_all(con, entities):
    for entity in entities:
        clear_entity(con, entity)


def draw_entity(con, entity, fov_map, game_map):
    if libtcod.map_is_in_fov(fov_map, entity.x, entity.y) or (entity.stairs and game_map.tiles[entity.x][entity.y].explored):
        libtcod.console_set_default_foreground(con, entity.color)
        libtcod.console_put_char(con, entity.x, entity.y, entity.char, libtcod.BKGND_NONE)


def clear_entity(con, entity):
    # erase the character that represents this object
    libtcod.console_put_char(con, entity.x, entity.y, ' ', libtcod.BKGND_NONE)