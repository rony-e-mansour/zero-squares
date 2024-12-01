import pygame
import sys
from game_logic import *
from state import *
from levels import *
from algo import *
import time
import os
import matplotlib.pyplot as plt

# Increase this value to increase the time between movements (in millisecond)
time_between_moves = 100

i = 0
WIDTH, HEIGHT = 800, 750
CELL_SIZE = 50
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (150, 150, 150)
RED = (255, 50, 50)
BLUE = (100, 100, 255)
ORANGE = (255, 191, 0)
GREEN = (59, 180, 170)
PINK = (243, 120, 150)

# grid = np.array(chosen_level)

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
surface = pygame.image.load("logo.jpg")
pygame.display.set_icon(surface)
screen.fill(WHITE)
pygame.display.set_caption("Zero Squares")

cell_size = 120  # Adjust this value if needed


def draw_level_selection_screen():
    screen.fill(WHITE)
    font = pygame.font.Font(None, 25)
    titlefont = pygame.font.Font(None, 36)
    title = titlefont.render("Select Level", True, BLACK)
    screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 20))

    levels = list(range(1, 21))  # List of levels from 1 to 20

    image_folder = "levels_image"  # Replace with your actual folder path
    for i, level in enumerate(levels):
        row = i // 5  # Calculate the row number
        col = i % 5  # Calculate the column number
        x = WIDTH // 2 - (5 * cell_size) // 2 + col * (cell_size + 10)
        y = 70 + row * (cell_size + 10)

        level_rect = pygame.Rect(x, y, cell_size, cell_size)
        level_rect_shadow = pygame.Rect(x + 2, y + 2, cell_size + 2, cell_size + 2)
        pygame.draw.rect(screen, GREY, level_rect_shadow, 0, 7)
        pygame.draw.rect(screen, WHITE, level_rect, 0, 7)
        pygame.draw.rect(screen, BLACK, level_rect, 1, 7)

        # Load the image for this level
        img_path = os.path.join(image_folder, f"level_{level}.png")
        try:
            level_image = pygame.image.load(img_path).convert_alpha()
        except pygame.error:
            print(f"Warning: Image file 'level_{level}.png' not found.")
            level_image = pygame.Surface((cell_size, cell_size)).convert_alpha()

        # Calculate aspect ratio and center image
        aspect_ratio = level_image.get_width() / level_image.get_height()
        if aspect_ratio > 1:
            new_width = cell_size - 0
            new_height = int((cell_size - 0) / aspect_ratio)
        else:
            new_height = cell_size - 6
            new_width = int((cell_size - 6) * aspect_ratio)

        level_image = pygame.transform.scale(level_image, (new_width, new_height))
        x_offset = (cell_size - 10 - new_width) // 2
        y_offset = (cell_size - 10 - new_height) // 2

        screen.blit(level_image, (x + 5 + x_offset, y + 5 + y_offset))

    pygame.display.flip()


def handle_algorithm_selection():
    running = True
    selected_algo = None
    algorithms = [
        (
            "Manual",
            pygame.Rect(WIDTH // 2 - 350, HEIGHT // 2 - 80, 120, 40),
            pygame.Rect(WIDTH // 2 - 346, HEIGHT // 2 - 76, 120, 40),
        ),
        (
            "BFS",
            pygame.Rect(WIDTH // 2 - 180, HEIGHT // 2 - 80, 120, 40),
            pygame.Rect(WIDTH // 2 - 176, HEIGHT // 2 - 76, 120, 40),
        ),
        (
            "DFS",
            pygame.Rect(WIDTH // 2 - 10, HEIGHT // 2 - 80, 120, 40),
            pygame.Rect(WIDTH // 2 - 6, HEIGHT // 2 - 76, 120, 40),
        ),
        (
            "DFS-Rec",
            pygame.Rect(WIDTH // 2 + 160, HEIGHT // 2 - 80, 120, 40),
            pygame.Rect(WIDTH // 2 + 164, HEIGHT // 2 - 76, 120, 40),
        ),
        (
            "UCS",
            pygame.Rect(WIDTH // 2 - 350, HEIGHT // 2 + 10, 120, 40),
            pygame.Rect(WIDTH // 2 - 346, HEIGHT // 2 + 14, 120, 40),
        ),
    ]

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                for name, rect, shadow in algorithms:
                    if rect.collidepoint(mouse_pos):
                        selected_algo = name
                        return selected_algo

        screen.fill(WHITE)
        titlefont = pygame.font.Font(None, 36)
        title = titlefont.render("Select Algorithm", True, BLACK)
        screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 20))

        # Draw algorithm options
        font = pygame.font.Font(None, 25)
        for name, rect, shadow in algorithms:
            pygame.draw.rect(screen, GREY, shadow, 0, 7)
            pygame.draw.rect(screen, WHITE, rect, 0, 7)
            pygame.draw.rect(screen, BLACK, rect, 1, 7)

            text_surface = font.render(name, True, BLACK)
            screen.blit(
                text_surface,
                (rect.x + 120 // 2 - text_surface.get_width() // 2, rect.y + 12),
            )

        pygame.display.flip()

    return selected_algo


def handle_level_selection():
    running = True
    selected_level = None
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                for i, level in enumerate(range(1, 21)):
                    row = i // 5
                    col = i % 5
                    x = WIDTH // 2 - (5 * cell_size) // 2 + col * (cell_size + 10)
                    y = 70 + row * (cell_size + 10)

                    level_rect = pygame.Rect(x, y, cell_size, cell_size)
                    if level_rect.collidepoint(mouse_pos):
                        selected_level = level
                        return selected_level

        draw_level_selection_screen()

    return selected_level


def render_path(path):
    print(f"\nIt took ({len(path)}) step to solve the level\n")

    screen.fill(WHITE)
    for state in path:
        screen.fill(WHITE)
        pygame.time.delay(time_between_moves)
        draw_grid(state.grid)

    pygame.time.delay(time_between_moves * 2)


def draw_grid(grid):
    global i
    i = i + 1
    titlefont = pygame.font.Font(None, 40)
    text = f"Level {selected_level}"
    leveltitle = titlefont.render(text, True, BLACK)
    screen.blit(leveltitle, (WIDTH // 2 - leveltitle.get_width() // 2, 20))
    player_num = get_players_num(grid)
    playerfont = pygame.font.Font(None, 30)
    plyerstext = f"Players Number: {player_num}"
    playertitle = playerfont.render(plyerstext, True, BLACK)
    screen.blit(playertitle, (WIDTH // 2 - playertitle.get_width() // 2, HEIGHT - 60))
    movestext = f"Moves number: {i}"
    movesfont = pygame.font.Font(None, 25)
    movestitle = movesfont.render(movestext, True, BLACK)
    if selected_algo != "Manual":
        screen.blit(movestitle, (WIDTH // 2 - movestitle.get_width() // 2, HEIGHT - 35))
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
                            else (
                                ORANGE
                                if cell.color == "orange"
                                else (PINK if cell.color == "pink" else GREEN)
                            )
                        )
                    ),
                    rect,
                    0,
                    5,
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
                            else (
                                ORANGE
                                if cell.color == "orange"
                                else (PINK if cell.color == "pink" else GREEN)
                            )
                        )
                    ),
                    rect,
                    5,
                    5,
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
                            else (
                                ORANGE
                                if cell.top_cell.color == "orange"
                                else (PINK if cell.top_cell.color == "pink" else GREEN)
                            )
                        )
                    ),
                    rect,
                    0,
                    10,
                )
                pygame.draw.rect(
                    screen,
                    (
                        RED
                        if cell.color == "red"
                        else (
                            BLUE
                            if cell.color == "blue"
                            else (
                                ORANGE
                                if cell.color == "orange"
                                else (PINK if cell.color == "pink" else GREEN)
                            )
                        )
                    ),
                    rect,
                    5,
                    5,
                )

    pygame.display.flip()


def handle_movement(state, direction):

    players = get_players(state.grid)
    sorted_players = sort_players_by_distance_from_edge(state.grid, players, direction)
    sorted_players = remove_blocked_players(state.grid, sorted_players, direction)
    new_state = State(state.grid)
    for player in sorted_players:
        while True:
            draw_grid(state.grid)
            pygame.time.delay(7)
            new_state.grid, bool = move_one_step(
                new_state.grid, direction, player.color
            )
            if not bool:
                break
        screen.fill(WHITE)
        pygame.time.delay(7)
    return new_state


def main(state, algo):
    current_state = state
    running = True
    states = []
    results = []
    states.append(current_state)

    if algo == "Manual":
        screen.fill(WHITE)
        while running:
            if get_players_num(current_state.grid) == 0:
                pygame.time.delay(700)
                return
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

    else:
        start_time = time.time()

        if algo == "BFS":
            path, visited_states = BFS(init_state)
            moves = len(path) - 1
        elif algo == "DFS":
            path, visited_states = DFS(init_state)
            moves = len(path) - 1
        elif algo == "UCS":
            path, visited_states = UCS(init_state)
            moves = len(path) - 1
        elif algo == "DFS-Rec":
            path, visited_states = DFS_Rec(init_state)
            moves = len(path) - 1

        end_time = time.time()
        elapsed_time = end_time - start_time

        results.append(
            {
                "algo": algo,
                "level": selected_level,
                "time": elapsed_time,
                "visited_states": visited_states,
                "path": len(path),
            }
        )

        render_path(path)

    return results


def write_results_to_file(results):
    with open("results.md", "a") as f:
        for result in results:
            f.write(
                f"|  **{result['algo']}** | {result['time']:.8f} | {result['visited_states']} | {result['path']} |\n"
            )
    print("Results have been written to results.txt")


if __name__ == "__main__":
    selected_level = handle_level_selection()
    selected_algo = handle_algorithm_selection()
    # print(f" ==> [selected_algo] = {selected_algo}")
    # print(f" ==> [selected_level] = {selected_level}")
    grid = levels[selected_level - 1]
    grid = np.array(grid)
    init_state = State(grid=grid)
    # screen.fill(WHITE)
    pygame.display.flip()

    results= main(init_state, selected_algo)

    write_results_to_file(results)
