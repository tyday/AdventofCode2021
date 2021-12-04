# Advent of Code Day 04
#
# Creator: Ty Day
class color:
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

class Game:
    def __init__(self):
        self.turns = []
        self.bingo_cards = {} # collection of bingo cards organized by board id
        self.positions = {} # collection of Position(s) organized by Position val
                            # ie. 45:[Position.val=45,Position.val=45,Position.val=45]
    def simulate_game(self):
        games = [id for id in self.bingo_cards]
        turns = self.turns[:]
        turn_count = 0
        while len(turns) > 0:
            turn = turns.pop(0)
            for position in self.positions[turn]:
                card_id, row, col = position.mark()
                card = self.bingo_cards[card_id]
                card_won = card.check_for_win(row, col, turn_count)
                if card_won:
                    print(f'Win on turn {turn_count}')
                    print(f'Last number called = {turn}')
                    print(f'Card {card.id} won with {card.value_at_win} points')
                    print(f'Total: {turn * card.value_at_win}')
                    if card_id in games:
                        idx = games.index(card_id)
                        games.pop(idx)
                        if len(games) == 1:
                            print("Last Card")
            
            turn_count += 1
        print("No cards won")
class Position:
    # A position on the bingo card.
    # 
    def __init__(self, val, col, row, card_number, marked=False):
        self.val = val
        self.row = row
        self.col = col
        self.card_number = card_number
        self.marked = marked
    def mark(self):
        self.marked = True
        return self.card_number, self.row, self.col
    def __repr__(self) -> str:
        value = f'{self.val:01d}'
        if self.marked:
            return color.PURPLE + value + color.END
        else:
            return value

class Bingo_Card:
    def __init__(self, matrix, id):
        self.id = id
        self.matrix = matrix # a 2d array 5x5 of Position(s) representing the Bingo card
        self.won = False
        self.turn_won = None
        self.value_at_win = 0
    def display(self) -> str:
        for row in self.matrix:
            print(row)

    def is_row_complete(self,row):
        positions = self.matrix[row]
        for pos in positions:
            if pos.marked == False:
                return False
        return True
    def is_column_complete(self,column):
        for row in range(5):
            if self.matrix[row][column].marked == False:
                return False
        return True
    def calculate_score(self):
        score = 0
        for row in self.matrix:
            for position in row:
                if position.marked == False:
                    score += position.val
        return score

    def check_for_win(self, row, col, turn_count):
        if self.won:
            # If the card has already won
            return False
        if self.is_row_complete(row):
            self.won = True
            self.turn_won = turn_count
            self.value_at_win = self.calculate_score()
            return True
        elif self.is_column_complete(col):
            self.won = True
            self.turn_won = turn_count
            self.value_at_win = self.calculate_score()
            return True
        else:
            return False

if __name__ == '__main__':
    data = ''
    with open('/home/pi/Programming/AdventOfCode/2021/Day04/day04.txt') as f:
        data = f.read()
        data = data.split('\n')

    game = Game()
    game.turns = [int(i) for i in data.pop(0).split(',')]
    data.pop(0)

    board_count = 0
    matrix = [[None]*5,[None]*5,[None]*5,[None]*5,[None]*5]
    row = 0
    # col = 0
    for line in data:
        if line == '':  
            # We've reached the end of a bingo card
            # Add it to the Game object
            card = Bingo_Card(matrix,board_count)
            game.bingo_cards[board_count] = card
            board_count += 1
            matrix = [[None]*5,[None]*5,[None]*5,[None]*5,[None]*5]
            row = 0
        else:
            row_data = [int(i) for i in line.split()]
            for col in range(5):
                val = row_data[col]
                position = Position(val,col,row,board_count)
                matrix[row][col] = position
                if val in game.positions:
                    game.positions[val].append(position)
                else:
                    game.positions[val] = [position]
            row += 1


    game.simulate_game()