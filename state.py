class State:
    def __init__(self, grid, status=False, previous=None, next_states=None):
        self.grid = grid
        self.status = status
        self.previous = previous
        self.next_states = next_states

    def __hash__(self):
        return hash(tuple(tuple(cell.type for cell in row) for row in self.grid))

    def __eq__(self, other):
        return all(
            self.grid[row][col].type == other.grid[row][col].type
            and self.grid[row][col].color == other.grid[row][col].color
            for row in range(len(self.grid))
            for col in range(len(self.grid[row]))
        )
