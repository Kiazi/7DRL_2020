import tcod as libtcod

from game_messages import Message
from game_states import GameStates
from render_functions import RenderOrder


def kill_player(player):
    player.char = 287
    player.color = libtcod.dark_red

    return Message('Too big of a courseload...you died of stress fatigue!', libtcod.red), GameStates.PLAYER_DEAD


def kill_monster(monster):
    death_message = Message('The {0} is finished!'.format(monster.name.capitalize()), libtcod.orange)

    monster.char = 287
    monster.color = libtcod.white
    monster.blocks = False
    monster.fighter = None
    monster.ai = None
    monster.name = 'remains of ' + monster.name
    monster.render_order = RenderOrder.CORPSE

    return death_message