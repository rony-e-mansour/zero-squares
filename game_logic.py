from cell import Cell

w = Cell(type="wall", color=None)
n = Cell()
e = Cell(type="empty", color=None)
r = Cell(type="player", color="red")
b = Cell(type="player", color="blue")
g = Cell(type="player", color="green")
R = Cell(type="goal", color="red")
B = Cell(type="goal", color="blue")
G = Cell(type="goal", color="green")


def find_next_states(grid, available_moves):
    next_states = []
    for move in available_moves:
        new_grid = grid
        print(f" ==> [move] = {move}")
        print_grid(move_all_players_in_direction(grid=new_grid, direction=move))


def print_grid(grid):
    print("Grid: ")
    for row in grid:
        print("".join(str(cell) for cell in row))
    print()


def get_adjacent_cell_in_direction(grid, player, direction):
    x, y = find_one_player_position(grid, player.color)
    adjacent_cell = None

    if direction == "up":
        if y > 0:
            adjacent_cell = Cell(grid[y - 1][x].type, grid[y - 1][x].color)
    elif direction == "down":
        if y < len(grid) - 1:
            adjacent_cell = Cell(grid[y + 1][x].type, grid[y + 1][x].color)
    elif direction == "left":
        if x > 0:
            adjacent_cell = Cell(grid[y][x - 1].type, grid[y][x - 1].color)
    elif direction == "right":
        if x < len(grid[0]) - 1:
            adjacent_cell = Cell(grid[y][x + 1].type, grid[y][x + 1].color)

    # print(f" ==> [adjacent_cell] = {adjacent_cell.type, player}")
    return adjacent_cell


def get_adjacent_cells(grid, player_position):
    x, y = player_position
    adjacent_cells = []

    if y > 0:
        adjacent_cells.append(grid[y - 1][x])

    if y < len(grid) - 1:
        adjacent_cells.append(grid[y + 1][x])

    if x > 0:
        adjacent_cells.append(grid[y][x - 1])

    if x < len(grid[0]) - 1:
        adjacent_cells.append(grid[y][x + 1])

    return adjacent_cells


def all_available_moves(grid):
    players_pos = find_all_players_position(grid)
    players_moves = []

    for player in players_pos:
        players_moves.append(player_available_move(grid, player))

    all_moves = set()

    for moves in players_moves:
        all_moves.update(moves)

    return all_moves


def player_available_move(grid, player_position):
    x, y = player_position
    directions = []

    if y > 0 and grid[y - 1][x].type not in ["wall", "player", "mixed"]:
        directions.append("up")

    if y < len(grid) - 1 and grid[y + 1][x].type not in ["wall", "player", "mixed"]:
        directions.append("down")

    if x > 0 and grid[y][x - 1].type not in ["wall", "player", "mixed"]:
        directions.append("left")

    if x < len(grid[0]) - 1 and grid[y][x + 1].type not in ["wall", "player", "mixed"]:
        directions.append("right")

    return directions


def get_players(grid):
    players = []
    for _, row in enumerate(grid):
        for _, cell in enumerate(row):
            if cell.type == "player":
                players.append(cell)
            if cell.type == "mixed":
                players.append(cell.top_cell)
    # print(f" ==> [players] = {players}")
    return players


def get_players_num(grid):
    players_num = 0
    for _, row in enumerate(grid):
        for _, cell in enumerate(row):
            if cell.type in ["player", "mixed"]:
                players_num += 1

    return players_num or Exception("No Players Found")


def find_all_players_position(grid):
    players_positions = []
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell.type in ["player", "mixed"]:
                players_positions.append((x, y))
    return players_positions  # Return None if player not found


def find_one_player_position(grid, player_color):
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if (cell.type == "player" and cell.color == player_color) or (
                cell.type == "mixed" and cell.top_cell.color == player_color
            ):
                return x, y


def did_reach_the_goal(player, goal):
    return player.color == goal.color


def move_one_step(grid, direction, player_color):
    player_pos = find_one_player_position(grid, player_color)
    if not player_pos:
        return False

    x, y = player_pos
    new_x, new_y = x, y

    if direction == "left":
        new_x -= 1 if x > 0 else 0
    elif direction == "right":
        new_x += 1 if x < len(grid[0]) - 1 else 0
    elif direction == "up":
        new_y -= 1 if y > 0 else 0
    elif direction == "down":
        new_y += 1 if y < len(grid) - 1 else 0
    else:
        return False

    if (
        grid[new_y][new_x].type == "wall"
        or grid[new_y][new_x].type == "player"
        or grid[new_y][new_x].type == "mixed"
    ):
        return False

    elif grid[y][x].type == "mixed":
        grid[new_y][new_x] = Cell(type="player", color=player_color)
        grid[y][x] = Cell(type="goal", color=grid[y][x].color)

    elif grid[new_y][new_x].type == "goal":
        if did_reach_the_goal(grid[y][x], grid[new_y][new_x]):
            grid[y][x] = Cell(type="empty", color=None)
            grid[new_y][new_x] = Cell(type="empty", color=None)
        else:
            grid[new_y][new_x] = Cell(
                type="mixed",
                color=grid[new_y][new_x].color,
                top_cell=grid[y][x],
            )
            grid[y][x] = Cell(type="empty", color=None)

    else:
        grid[y][x] = Cell(type="empty", color=None)
        grid[new_y][new_x] = Cell(type="player", color=player_color)
    return True


def move_one_player(grid, direction, player_color):
    player_pos = find_one_player_position(grid, player_color)
    if not player_pos:
        return False

    x, y = player_pos
    new_x, new_y = x, y

    if direction == "left":
        while new_x > 0 and grid[y][new_x - 1].type not in ["wall", "player"]:
            new_x -= 1
    elif direction == "right":
        while new_x < len(grid[0]) - 1 and grid[y][new_x + 1].type not in [
            "wall",
            "player",
        ]:
            new_x += 1
    elif direction == "up":
        while new_y > 0 and grid[new_y - 1][x].type not in ["wall", "player"]:
            new_y -= 1
    elif direction == "down":
        while new_y < len(grid) - 1 and grid[new_y + 1][x].type not in [
            "wall",
            "player",
        ]:
            new_y += 1
    else:
        return False

    if (new_x, new_y) != (x, y):
        grid[y][x] = Cell(type="empty", color=None)
        grid[new_y][new_x] = Cell(type="player", color=player_color)
        return True
    else:
        return False


def sort_players_by_distance_from_edge(grid, players, direction):
    edge_distances = {}

    for player in players:
        x, y = find_one_player_position(grid, player.color)

        if direction == "left":
            distance = x
        elif direction == "right":
            distance = len(grid[0]) - 1 - x
        elif direction == "up":
            distance = y
        elif direction == "down":
            distance = len(grid) - 1 - y

        edge_distances[player] = distance

    sorted_players = sorted(players, key=lambda p: edge_distances[p])
    return sorted_players


def move_all_players_in_direction(grid, direction):
    players = get_players(grid)

    sorted_players = sort_players_by_distance_from_edge(grid, players, direction)

    sorted_players = remove_blocked_players(grid, sorted_players, direction)

    for player in sorted_players:
        while True:
            can_move_more = move_one_step(grid, direction, player.color)
            if not can_move_more:
                return grid


def remove_blocked_players(grid, players, direction):
    unblocked_players = []
    for player in players:
        x, y = find_one_player_position(grid, player.color)

        if direction == "up":
            adjacent_x, adjacent_y = x, y - 1
        elif direction == "down":
            adjacent_x, adjacent_y = x, y + 1
        elif direction == "left":
            adjacent_x, adjacent_y = x - 1, y
        elif direction == "right":
            adjacent_x, adjacent_y = x + 1, y

        if (0 <= adjacent_x < len(grid[0])) and (0 <= adjacent_y < len(grid)):
            adjacent_cell = grid[adjacent_y][adjacent_x]

            if adjacent_cell.type not in ["wall", "player", "mixed"]:
                unblocked_players.append(player)

    return unblocked_players
