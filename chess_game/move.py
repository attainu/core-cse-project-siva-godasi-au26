from chessboard import board

class Move(board):
    def __init__(self):
        self.turn = 1
        self.coin = None
        self.end_coin = None
        self.wx,self.wy,self.bx,self.by = -1,-1,-1,-1

        self.create_board()
    def valid_move(self,x,y,ex,ey):
        #if the move is valid change the position of the coins or print invalid move
        if (x>7 or ex >7 or x<0 or ex<0 or y>7 or ey>7 or y<0 or ey<0):
            print("invalid move")
            print("enter the x and y values 'less than 7 and graterthan 0 ")
        
        self.coin = self.grid[x][y]
        self.end_coin = self.grid[ex][ey]
        
        if (self.coin=='**' or self.turn==1 and (self.coin[0]=='B' or self.end_coin[0]=='W')) or (self.turn==0 and (self.coin[0]=='W' or self.end_coin[0]=='B')):
            print("invalid move")
        else:
            res = self.movabale(x,y,ex,ey)
            if res == True:
                self.grid[ex][ey] =self.coin
                self.grid[x][y] = '**'
            else:
                print("invalid move")

    def move(self):
        #moves takes from console and use required functions to change the postion of the coin
        if  self.turn == 1:
            print("white's move & x,y values should be >=0 and <=7")
            x,y = map(int,input("enter the starting point").split())
            ex,ey = map(int,input("enter the ending point").split())
            self.valid_move(x,y,ex,ey)
            self.print_grid()
            self.check()
            self.checkmate()
            if self.checkmate == True:
                self.turn !=0
            else:
                self.turn = 0
        if self.turn == 0:
            print("blacks move")
            x,y = map(int,input("enter the starting point").split())
            ex,ey = map(int,input("enter the ending point").split())
            self.valid_move(x,y,ex,ey)
            self.print_grid()
            self.check()
            self.checkmate()
            if self.checkmate == True:
                self.turn !=1
            else:
                self.turn = 1
            self.move()
    
    def straight(self,x,y,ex,ey):
        if (x == ex or y == ey) and self.obstructed(x,y,ex,ey) :
            return True
        return False

    def diagnal(self,x,y,ex,ey):
        if (abs(x-ex) == abs(y-ey)) and self.obstructed(x,y,ex,ey) :
            return True
        return False

    def lmove(self,x,y,ex,ey):
        if (abs(x-ex),abs(y-ey)) in [(2,1),(1,2)] :
            return True
        return False
    
    def movabale(self,x,y,ex,ey):
        if self.coin[1] == 'Q':
            if self.straight(x,y,ex,ey) or self.diagnal(x,y,ex,ey):
                return True
            return False
        if self.coin[1] == 'R':
            if self.straight(x,y,ex,ey):
                return True
            return False
        elif self.coin[1] == 'H':
            if self.lmove(x,y,ex,ey):
                return True
            return False
        elif self.coin[1] == 'B':
            if self.diagnal(x,y,ex,ey):
                return True
            return False
        elif self.coin[1] == 'P':
            if self.straight(x,y,ex,ey) or ((self.diagnal(x,y,ex,ey)and self.grid[ex][ey]!='**')):
             if (abs(x-ex)<=1 and abs(y-ey)<=1):
                    if self.coin[0] == 'B' and (ex > x):
                        return True
                    elif self.coin[0] == 'W' and (ex < x):
                        return True
        elif self.coin[1] == 'K':
            if self.straight(x,y,ex,ey) or self.diagnal(x,y,ex,ey):
                if(abs(x-ex)<=1 and abs(y-ey)<=1):
                    return True

    def obstructed(self,x,y,ex,ey):
        dirx,diry = -1,-1
        if (ex-x) > 0:
            dirx = 1
        elif(ex-x) == 0:
            dirx = 0
        if (ey-y) > 0:
            diry = 1
        elif(ey-y) == 0:
            diry = 0
        stx,sty =x+dirx,y+diry
        while(stx!=ex or sty!=ey):
            if self.grid[stx][sty] != '**':
                return False
            stx+=dirx
            sty+=diry
        return True

    
    def check(self):
        
        for x in range(8):
            for y in range(8):
                if self.grid[x][y] == 'BK':
                    self.bx,self.by = x,y
                if self.grid[x][y] == 'WK':
                    self.wx,self.wy = x,y
       
        for x in range(8):
            for y in range(8):
                if self.grid[x][y] != '**':
                    if (self.movabale(x,y,self.bx,self.by) and self.grid[x][y][0]=='W'):
                        print('Black check')

        for x in range(8):
            for y in range(8):
                if self.grid[x][y] != '**':
                    if (self.movabale(x,y,self.wx,self.wy) and self.grid[x][y][0]=='B'):
                        print('White check')  

    def checkmate(self):
        for x in [0,1,-1]:
            for y in [0,1,-1]:
                if self.wx+x in range(8) and self.wy+y in range(8) and self.grid[self.wx+x][self.wy+y]=='**' and self.check():
                    print(" white checkmate")
          
        for x in [0,1,-1]:
            for y in [0,1,-1]:
                if self.bx+x in range(8) and self.by+y in range(8) and self.grid[self.bx+x][self.by+y]=='**' and self.check():
                    print("black checkmate")     
    

    def print_grid(self):
        # for print the grid
        for i in self.grid:
            if  (self.coin == '**' or (self.turn==1 and (self.coin[0]=='B' or self.end_coin[0]=='W')) or (self.turn==0 and (self.coin[0]=='W' or self.end_coin[0]=='B'))) == False:
                print(i)
