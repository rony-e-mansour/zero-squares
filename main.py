import pygame
import sys
from game_logic import *
from state import *
from levels import *

# import numby

states = []
grid = level6
pygame.init()

WIDTH, HEIGHT = 800, 600
CELL_SIZE = 50
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 50, 50)
BLUE = (100, 100, 255)
ORANGE = (255, 191, 0)
GREEN = (59, 215, 145)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(WHITE)
pygame.display.set_caption("Zero Squares")

clock = pygame.time.Clock()


def draw_grid(grid):

    offset_x = (WIDTH - len(grid[0]) * CELL_SIZE) // 2
    offset_y = (HEIGHT - len(grid) * CELL_SIZE) // 2

    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            rect = pygame.Rect(
                offset_x + x * CELL_SIZE, offset_y + y * CELL_SIZE, CELL_SIZE, CELL_SIZE
            )
            if cell.type == "wall":
                pygame.draw.rect(screen, BLACK, rect)
            elif cell.type == "player":
                pygame.draw.rect(
                    screen,
                    (
                        RED
                        if cell.color == "red"
                        else (
                            BLUE
                            if cell.color == "blue"
                            else (ORANGE if cell.color == "orange" else GREEN)
                        )
                    ),
                    rect,
                    0,
                    10,
                )
            elif cell.type == "goal":
                pygame.draw.rect(screen, WHITE, rect)
                pygame.draw.rect(
                    screen,
                    (
                        RED
                        if cell.color == "red"
                        else (
                            BLUE
                            if cell.color == "blue"
                            else (ORANGE if cell.color == "orange" else GREEN)
                        )
                    ),
                    rect,
                    5,
                    10,
                )
            elif cell.type == "mixed":
                pygame.draw.rect(
                    screen,
                    (
                        RED
                        if cell.top_cell.color == "red"
                        else (
                            BLUE
                            if cell.top_cell.color == "blue"
                            else (ORANGE if cell.top_cell.color == "orange" else GREEN)
                        )
                    ),
                    rect,
                    0,
                    15,
                )
                pygame.draw.rect(
                    screen,
                    (
                        RED
                        if cell.color == "red"
                        else (
                            BLUE
                            if cell.color == "blue"
                            else (ORANGE if cell.color == "orange" else GREEN)
                        )
                    ),
                    rect,
                    5,
                    10,
                )

    pygame.display.flip()


def handle_movement(state, direction):

    players = get_players(state.grid)
    sorted_players = sort_players_by_distance_from_edge(state.grid, players, direction)
    sorted_players = remove_blocked_players(state.grid, sorted_players, direction)
    temp_state = State(state.grid.copy())
    for player in sorted_players:
        print(f" ==> [player] = {player}")
        while True:
            print("in while true")
            draw_grid(grid)
            pygame.time.delay(7)
            can_move_more = move_one_step(temp_state.grid, direction, player.color)

            if not can_move_more:
                break

        screen.fill(WHITE)
        pygame.time.delay(7)

    return temp_state
    # print_grid(state.grid)


def main(state):
    current_state = state
    running = True
    states = []
    states.append(current_state)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                print(f" ==> [event] = {event}")
                if event.key == pygame.K_LEFT:
                    new_state = handle_movement(current_state, "left")
                    if new_state != current_state:
                        states.append(new_state)
                elif event.key == pygame.K_RIGHT:
                    new_state = handle_movement(current_state, "right")
                    if new_state != current_state:
                        states.append(new_state)
                elif event.key == pygame.K_UP:
                    new_state = handle_movement(current_state, "up")
                    if new_state != current_state:
                        states.append(new_state)
                elif event.key == pygame.K_DOWN:
                    new_state = handle_movement(current_state, "down")
                    if new_state != current_state:
                        states.append(new_state)

        draw_grid(current_state.grid)
        clock.tick(60)

    pygame.quit()
    print(len(states))
    sys.exit()


init_state = State(grid=grid)

if __name__ == "__main__":
    main(init_state)


states.extend([init_state])
print(len(states))
print(states[0])

print("Original Grid:")
print_grid(init_state.grid)
new_grid = move_all_players_in_direction(grid=grid, direction="left")
new_state = State(grid=new_grid)
print("\nNew Grid:")
print_grid(new_state.grid)
print(
    "\nDifference:",
    set(tuple(row) for row in init_state.grid)
    ^ set(tuple(row) for row in new_state.grid),
)

if grid != new_grid:
    new_state = State(grid=new_grid)
    states.extend([new_state])
    print()
    print(states[1])
print(len(states))
