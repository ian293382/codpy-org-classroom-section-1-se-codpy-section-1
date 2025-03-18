from ..database.operation import save_game_state
from .judge import hit_obstacle, game_over, arrive_at_destination

def move_location(game_state, direction):
    if game_over(game_state["health"]):
        return game_state
    
    x, y = game_state["current_position"]
    
    # Update position based on direction
    if direction == "up" and y > 0:
        y -= 1
    elif direction == "left":
        x -= 1
    elif direction == "right":
        x += 1
    elif direction == "down" :
        y += 1


    x = max(0,min(x, game_state["map_size"][0] - 1) )
    y = max(0, min(y, game_state["map_size"][1] - 1 ))
    new_position = [x, y]

    if hit_obstacle(new_position, game_state["current_level_name"]):
        # Update health
        game_state["health"] -= 1
    else:
        # Update path
        if new_position not in game_state["path"]:
            game_state["path"].append(new_position)

        # Update position
        game_state["current_position"] = new_position

    if arrive_at_destination(game_state["current_level_name"], game_state["current_position"]):
        # Game won
        game_state["health"] = 666

    # Update database
    save_game_state(game_state['username'], game_state["current_level_name"], game_state["map_size"],
                    game_state["health"], game_state["path"], game_state["current_position"])

    return game_state
