from dice import selector


def random_gift(player_storage):
    dice_roll = selector([0,1,2,3],[10,35,35,30])
    if dice_roll == 0:
        print("You found a key!")
        player_storage["key"] += 1
    elif dice_roll == 1:
        print("You found a health potion!")
        player_storage["health"] += 20
    elif dice_roll == 2:
        print("You found bullets!")
        player_storage["weapon"] += 1
    else:
        print("You found nothing!")
    return player_storage