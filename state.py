from game_logic import *


class State:
    def __init__(self, grid, previous_state=None, next_states=None):
        self.grid = grid
        self.players = get_players(grid)
        self.previous_state = previous_state
        self.next_states = next_states

    def __repr__(self):
        print("Current State:")
        print_grid(self.grid)
        return f"players={self.players},\nnext_states={self.next_states},\nprevious_state={self.previous_state})"
