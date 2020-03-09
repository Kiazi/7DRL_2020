import tcod as libtcod

from game_messages import Message


def heal(*args, **kwargs):
    entity = args[0]
    amount = kwargs.get('amount')

    results = []

    if entity.fighter.hp == entity.fighter.max_hp:
        results.append({'consumed': False, 'message': Message('You are already at maximum health.', libtcod.yellow)})
    else:
        entity.fighter.heal(amount)
        results.append({'consumed': True, 'message': Message('Your wounds begin to close!', libtcod.green)})

    return results
    
# def gold(*args, **kwargs):
    # entity = args[0]
    # amount = kwargs.get('amount')
    
    # entity.fighter.gold += amount
    
    # results = []
    
    # results.append({'consumed': True})
    
    # return results