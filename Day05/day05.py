# Advent of Code Day 05
#
# Creator: Ty Day

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Point_Pair:
    def __init__(self,x1,y1,x2,y2) -> None:
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.direction = None
        self.is_diagonal = self.check_diagonal()
    
    def __repr__(self) -> str:
        return f'{self.x1},{self.y1} -> {self.x2},{self.y2}'

    def check_diagonal(self):
        if (self.x1 == self.x2) and (self.y1 == self.y2):
            self.direction = "point"
            return False
        if (self.x1 == self.x2):
            self.direction = "vertical"
            return False
        elif (self.y1 == self.y2):
            self.direction = "horizontal"
            return False
        else:
            self.direction = 'diagonal'
            return True
    
    


class Grid:
    def __init__(self, point_pairs) -> None:
        self.point_pairs = point_pairs
        self.grid = []

        self.create_grid()
    
    def display(self):
        for row in self.grid:
            print(row)
    def create_grid(self):
        # find the largest x and y
        maxX, maxY = 0,0
        for pp in self.point_pairs:
            pp_maxX = max(pp.x1,pp.x2)
            pp_maxY = max(pp.y1, pp.y2)

            if pp_maxX > maxX:
                maxX = pp_maxX
            if pp_maxY > maxY:
                maxY = pp_maxY
        
        for row in range(maxY + 1):
            grid_row = []
            for col in range(maxX + 1):
                grid_row.append(0)
            self.grid.append(grid_row)
    def set_ascending(self, var1,var2):
        if var1 < var2:
            return var1,var2
        else:
            return var2,var1
    def get_rate_info(self, var1, var2):
        rate = 1
        length = var2 - var1
        if var1 > var2:
            rate = -1
            length = var1 - var2
        return var1, var2, rate, length + 1
    def populate_straight_vents(self):
        for pair in self.point_pairs:
            if pair.direction == 'horizontal':
                row = pair.y1
                var1, var2 = self.set_ascending(pair.x1,pair.x2)
                for col in range(var1, var2 + 1):
                    self.grid[row][col] += 1
            elif pair.direction == 'vertical':
                col = pair.x1
                var1, var2 = self.set_ascending(pair.y1,pair.y2)
                for row in range(var1, var2 + 1):
                    self.grid[row][col] += 1
            elif pair.direction == 'point':
                self.grid[pair.y1][pair.x1] += 1
            elif pair.direction == 'diagonal':
                # col,col_end = self.set_ascending(pair.x1,pair.x2)
                # row,row_end = self.set_ascending(pair.y1,pair.y2)
                x,x2,h_rate,length = self.get_rate_info(pair.x1,pair.x2)
                y,y2,v_rate,length = self.get_rate_info(pair.y1,pair.y2)
                for _ in range(length):
                    self.grid[y][x] += 1
                    x += h_rate
                    y += v_rate
            else:
                pass
    
    def calculate_part_one(self):
        score = 0
        for row in self.grid:
            for column in row:
                if column > 1:
                    score += 1
        return score
    

if __name__ == '__main__':
    data = ''
    with open('/home/pi/Programming/AdventOfCode/2021/Day05/day05.txt') as f:
    # with open('/home/pi/Programming/AdventOfCode/2021/Day05/test.txt') as f:
        data = f.read().strip()
        data = data.split('\n')
        data = [d.split(' -> ') for d in data]
        # print(data)
    
    list_of_point_pairs = []
    for line in data:
        x1,y1 = [int(pair) for pair in line[0].split(',')]
        x2,y2 = [int(pair) for pair in line[1].split(',')]
        pp = Point_Pair(x1,y1,x2,y2)
        list_of_point_pairs.append(pp)

    grid = Grid(list_of_point_pairs)
    grid.populate_straight_vents()
    # grid.display()
    print(grid.calculate_part_one())