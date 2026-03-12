def win_or_loss(player_storage, turn_count):
        if player_storage["key"] >= 3:
            print("Congratulations! You have collected all the keys and won the game!")
            return False
        elif turn_count <= 0:
            if player_storage["health"] <= 0:
                print("Game Over! You have no health left.")
                return False
#continue
        return True
