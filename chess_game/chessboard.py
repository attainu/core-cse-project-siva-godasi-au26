class board:
    def __init__(self):
       self.grid = [['*']*8 for i in range (8)]
    def create_board(self):
        self.grid = [['*']*8 for i in range (8)]
    # W - white coins, B - black coins
    #R-rook,H-knight,B-bishop,K-king,Q-queen,P-pawn

        arr = ['R','H','B','K','Q','B','H','R']
        for i in range (len(arr)):
            self.grid[0][i] = 'B'+arr[i]
            self.grid[1][i] = 'BP'
            self.grid[7][i] = 'W'+arr[i]
            self.grid[6][i] = 'WP'
    def print_grid(self):
        for i in self.grid:
            print(i)


