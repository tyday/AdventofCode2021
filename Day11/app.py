# Advent of Code /home/tyrda/LocalProgramming/AdventofCode2021/Day11/input.txt
#
# Created: 12-11-2021 00:04:52
# Creator: Ty Day

class COLOR:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

class Octopus:
    def __init__(self, val, loc):
        self.val = val
        self.neighbors = []
        self.loc = loc
        self.flashed = False
    def get_text(self) -> str:
        text = COLOR.BLUE + str(self.val) + COLOR.END
        if self.val == 0:
            text = COLOR.YELLOW + str(self.val) + COLOR.END
        return text
    def __repr__(self) -> str:
        repr = f'[{self.loc}] - {self.val}'
        return repr

class Grid:
    def __init__(self, data):
        self.data = data
        self.grid = [[None for col in row]for row in data]
        self.flashes = 0

        self.initialize_grid()
    
    def __str__(self) -> str:
        grid = ''
        for row in self.grid:
            for squid in row:
                grid += f' {squid.get_text()} '
            grid += '\n'
        return grid

    def initialize_grid(self):
        for row in range(len(self.data)):
            for col in range(len(self.data[0])):
                self.grid[row][col] = Octopus(self.data[row][col], (row,col))
        for row in range(len(self.grid)):
            for col in range(len(self.grid[0])):
                neighbors = []
                min_row = row - 1 if row > 0 else row
                max_row = row + 2 if row < len(self.data) -1 else row + 1
                min_col = col - 1 if col > 0 else col
                max_col = col + 2 if col < len(self.data[0])-1 else col + 1

                for neighbor_row in range(min_row,max_row):
                    for neighbor_col in range(min_col, max_col):
                        if (neighbor_row,neighbor_col) != (row,col):
                            neighbors.append(self.grid[neighbor_row][neighbor_col])
                self.grid[row][col].neighbors = neighbors
    
    def energize_neighbors(self, neighbors):
        for neighbor in neighbors:
            neighbor.val += 1

    def run_turn(self):
        energized = []
        flashes = 0
        for row in self.grid:
            for squid in row:
                squid.val += 1
                squid.flashed = False
                if squid.val > 9:
                    flashes += 1
                    squid.flashed = True
                    squid.val = 0
                    [energized.append(n) for n in squid.neighbors]
        while len(energized) > 0:
            squid = energized.pop()
            if squid.flashed == False:
                squid.val += 1
            if squid.val > 9:
                flashes += 1
                squid.flashed = True
                squid.val = 0
                [energized.append(n) for n in squid.neighbors]
        self.flashes += flashes
        if flashes == len(self.grid ) * len(self.grid[0]):
            return True
        return False


def main():
    grid = Grid(data)
    turn = 0
    turn = 0
    flashes = 0
    all_octupi_flashed = False
    while all_octupi_flashed == False:
        all_octupi_flashed = grid.run_turn()
        turn += 1
        if turn == 100:
            print(f"Turn {turn} flashes: {grid.flashes}")
    print(grid)
    print(f"Turn {turn} flashes: {grid.flashes}")

if __name__ == '__main__':
    data = ''
    with open('/home/tyrda/LocalProgramming/AdventofCode2021/Day11/input.txt') as f:
        data = f.read().strip()
        data = data.split('\n')
    data = [[int(i) for i in d] for d in data]

    main()