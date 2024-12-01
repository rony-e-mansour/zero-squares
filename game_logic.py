from cell import Cell
from state import State
import numpy as np
import random


def is_finished(grid):
    for cell in grid.flat:
        if cell.type == "player" or cell.type == "mixed":
            return False
    return True


def print_state(state):
    print("\nCurrent State:")
    print("Grid:")
    print_grid(state.grid)
    print("\nStatus:", state.status)

    if state.previous:
        print("\nPrevious State:")
        print_grid(state.previous.grid, True)
    else:
        print("\nNo previous state available.")

    if state.next_states and len(state.next_states) > 0:
        print("\nNext States:")
        for i, next_state in enumerate(state.next_states):
            print(f"\tstate number {i+1}:")
            print_grid(next_state.grid, True)
    else:
        print("\nNo next states available.")


def find_next_states(state):
    available_moves = all_available_moves(state.grid)
    current_grid = state.grid

    next_states = []
    for move in available_moves:
        new_grid = move_all_players_in_direction(current_grid, move)

        finished = is_finished(new_grid)

        next_states.append(State(grid=new_grid, status=finished, previous=state))

    return next_states


def print_grid(grid, with_tab=False):
    if with_tab:
        for row in grid:
            print("\t" + "".join(str(cell) for cell in row))
    else:
        for row in grid:
            print("".join(str(cell) for cell in row))


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
    random.shuffle(players_pos)
    all_moves = {
        move for player in players_pos for move in player_available_move(grid, player)
    }
    return all_moves


def player_available_move(grid, player_position):
    x, y = player_position
    directions = []

    max_y, max_x = grid.shape

    if y > 0 and grid[y - 1, x].type not in {"wall", "player", "mixed"}:
        directions.append("up")

    if y < max_y - 1 and grid[y + 1, x].type not in {"wall", "player", "mixed"}:
        directions.append("down")

    if x > 0 and grid[y, x - 1].type not in {"wall", "player", "mixed"}:
        directions.append("left")

    if x < max_x - 1 and grid[y, x + 1].type not in {"wall", "player", "mixed"}:
        directions.append("right")

    return directions


def get_players(grid):
    players = []
    for row in grid.flat:
        if row.type == "player":
            players.append(row)
        elif row.type == "mixed":
            players.append(row.top_cell)
    return players


def get_players_num(grid):
    players_num = 0
    for _, row in enumerate(grid):
        for _, cell in enumerate(row):
            if cell.type in ["player", "mixed"]:
                players_num += 1

    return players_num


def find_all_players_position(grid):
    players_positions = []
    for y in range(grid.shape[0]):
        for x in range(grid.shape[1]):
            cell = grid[y, x]
            if cell.type in {"player", "mixed"}:
                players_positions.append((x, y))
    random.shuffle(players_positions)
    return players_positions


def find_one_player_position(grid, player_color):
    max_y, max_x = grid.shape
    for y in range(max_y):
        for x in range(max_x):
            cell = grid[y, x]
            if cell.type == "player" and cell.color == player_color:
                return x, y
            elif cell.type == "mixed" and cell.top_cell.color == player_color:
                return x, y
    return None


def find_one_goal_position(grid, goal_color):
    max_y, max_x = grid.shape
    for y in range(max_y):
        for x in range(max_x):
            cell = grid[y, x]
            if cell.type == "goal" and cell.color == goal_color:
                return x, y
            elif cell.type == "mixed" and cell.color == goal_color:
                return x, y
    return None


def did_reach_the_goal(player, goal):
    return player.color == goal.color


def move_one_step(grid, direction, player_color):
    grid = np.array(grid)
    player_pos = find_one_player_position(grid, player_color)

    if player_pos is None:
        return grid, False

    x, y = player_pos

    dx, dy = 0, 0
    if direction == "left" and x > 0:
        dx = -1
    elif direction == "right" and x < len(grid[0]) - 1:
        dx = 1
    elif direction == "up" and y > 0:
        dy = -1
    elif direction == "down" and y < len(grid) - 1:
        dy = 1

    new_x, new_y = x + dx, y + dy

    target_cell = grid[new_y][new_x]

    if target_cell.type in {"wall", "player", "mixed"}:
        return grid, False

    current_cell = grid[y][x]

    if current_cell.type == "mixed":
        grid[new_y][new_x] = Cell(type="player", color=player_color)
        grid[y][x] = Cell(type="goal", color=current_cell.color)

    elif target_cell.type == "goal":
        if did_reach_the_goal(current_cell, target_cell):
            grid[y][x] = Cell(type="empty", color=None)
            grid[new_y][new_x] = Cell(type="empty", color=None)
        else:
            grid[new_y][new_x] = Cell(
                type="mixed", color=target_cell.color, top_cell=current_cell
            )
            grid[y][x] = Cell(type="empty", color=None)

    else:
        grid[y][x] = Cell(type="empty", color=None)
        grid[new_y][new_x] = Cell(type="player", color=player_color)

    return grid, True


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
            grid, bool = move_one_step(grid, direction, player.color)
            if not bool:
                break
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


def calculate_heuristic(grid):
    grid = np.array(grid)
    players = get_players(grid)
    manhatin_dist = 0
    for player in players:
        player_pos = find_one_player_position(grid=grid, player_color=player.color)
        goal_pos = find_one_goal_position(grid=grid, goal_color=player.color)
        manhatin_dist += abs(player_pos[0] - goal_pos[0]) + abs(
            player_pos[1] - goal_pos[1]
        )
    manhatin_dist += len(players)
    return manhatin_dist
