import random

class Game2048State:
    def __init__(self, grid):
        self._grid = grid

    def add_new_tile(self):
        empty_cells = [(i, j) for i in range(4) for j in range(4) if self._grid[i][j] == 0]
        if empty_cells:
            i, j = random.choice(empty_cells)
            self._grid[i][j] = 2 if random.random() < 0.9 else 4

    def check_game_over(self):
        # todo
        pass

    # called after game over
    def check_if_won(self):
        for row in self.grid:
            if 2048 in row:
                return True
        return False
    
    def get_legal_moves(self):
        # todo
        pass



    # DNAWJNDIJAWNDJAWNDJIN
    def merge_left(self, row):
        new_row = [0] * 4
        i = 0
        for tile in row:
            if tile != 0:
                if new_row[i] == 0:
                    new_row[i] = tile
                elif new_row[i] == tile:
                    new_row[i] *= 2
                    i += 1
                else:
                    i += 1
                    new_row[i] = tile
        return new_row



    def transpose_grid(self, grid):
        return [list(row) for row in zip(*grid)]

    def move_left(self, grid):
        new_grid = []
        for row in grid:
            new_row = self.merge_left(row)
            new_grid.append(new_row)
        return new_grid

    def move_right(self, grid):
        reversed_grid = [row[::-1] for row in grid]
        new_grid = []
        for row in reversed_grid:
            new_row = self.merge_left(row)
            new_grid.append(new_row[::-1])
        return new_grid

    def move_up(self, grid):
        transposed_grid = self.transpose_grid(grid)
        new_board = self.move_left(transposed_grid)
        return self.transpose_grid(new_board)

    def move_down(self, grid):
        transposed_board = self.transpose_grid(grid)
        new_board = self.move_right(transposed_board)
        return self.transpose_grid(new_board)
    # DNAWJNDIJAWNDJAWNDJIN



    def compute_score(self):
        # todo
        pass


    def print_grid(self):
        for row in self._grid:
            print(" ".join(map(str, row)))
        print()

    # def payoff(self):

def initial_state():
    state = Game2048State([[0] * 4 for _ in range(4)])
    state.add_new_tile()
    state.add_new_tile()
    return state
