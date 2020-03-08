import tcod as libtcod

from game_messages import Message
from game_states import GameStates
from render_functions import RenderOrder
from components.fighter import Fighter

def kill_player(player):
    player.char = 287
    player.color = libtcod.dark_red

    return Message('You could not defend the elements, and they scatter to the wind...', libtcod.dark_red), GameStates.PLAYER_DEAD


def kill_monster(monster):
    death_message = Message('The {0} is absorbed!'.format(monster.name.capitalize()), libtcod.orange)

    monster.char = 287
    monster.color = libtcod.white
    monster.blocks = False
    monster.fighter = None
    monster.ai = None
    monster.name = 'remains of ' + monster.name
    monster.render_order = RenderOrder.CORPSE
    
    return death_message
    return absorb(monster.fighter.element,monster.fighter.xp)