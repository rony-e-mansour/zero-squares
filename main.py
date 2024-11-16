import pygame
import sys
from game_logic import *
from state import *
from levels import *
from algo import *

states = []
grid = np.array(level16)
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
    temp_state = State(state.grid)
    for player in sorted_players:
        while True:
            draw_grid(state.grid)
            pygame.time.delay(7)
            temp_state.grid, bool = move_one_step(
                temp_state.grid, direction, player.color
            )
            if not bool:
                break
        screen.fill(WHITE)
        pygame.time.delay(7)
    return temp_state
    # print_grid(state.grid)


def main(state, algo="manual"):
    current_state = state
    running = True
    states = []
    states.append(current_state)
    if algo == "manual":
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        new_state = handle_movement(current_state, "left")
                        if not np.array_equal(new_state.grid, current_state.grid):
                            current_state = new_state
                            states.append(new_state)

                    elif event.key == pygame.K_RIGHT:
                        new_state = handle_movement(current_state, "right")
                        if not np.array_equal(new_state.grid, current_state.grid):
                            current_state = new_state
                            states.append(new_state)

                    elif event.key == pygame.K_UP:
                        new_state = handle_movement(current_state, "up")
                        if not np.array_equal(new_state.grid, current_state.grid):
                            current_state = new_state
                            states.append(new_state)

                    elif event.key == pygame.K_DOWN:
                        new_state = handle_movement(current_state, "down")
                        if not np.array_equal(new_state.grid, current_state.grid):
                            current_state = new_state
                            states.append(new_state)

            draw_grid(current_state.grid)
            clock.tick(60)

    elif algo == "BFS":
        path, len = BFS(init_state)
        print(f" ==> [len] = {len}")
        render_path(path)

    elif algo == "DFS":
        path, len = DFS(init_state)
        print(f" ==> [len] = {len}")
        render_path(path)
    print(f" ==> [len] = {len}")
    # render_path(path)
    pygame.quit()
    sys.exit()


def render_path(path):
    screen.fill(WHITE)
    for state in path:
        screen.fill(WHITE)
        pygame.time.delay(400)
        draw_grid(state.grid)
    pygame.time.delay(400)
    print(f" ==> [len(path)] = {len(path)}")


init_state = State(grid=grid)

if __name__ == "__main__":
    main(init_state, "BFS")
