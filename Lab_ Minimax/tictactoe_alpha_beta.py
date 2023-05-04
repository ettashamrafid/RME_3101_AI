import math

class Tictactoe:
    def __init__(self):
        self.board=[['.','.','.'],
                    ['.','.','.'],
                    ['.','.','.']]
        
        self.current_player='X'

    def game_over(self):
        if self.winner()!=None:
            return True
        else:
            for row in range(3):
                for col in range(3):
                    if self.board[row][col]=='.':
                        return False
        return True

    def winner(self):
        for rows in self.board:
            if rows[0]==rows[1]==rows[2] != '.':
                return rows[0]
        for col in range(3):
            if self.board[0][col]==self.board[1][col]==self.board[2][col] != '.':
                return self.board[0][col]
        if self.board[0][0]==self.board[1][1]==self.board[2][2] !='.':
            return self.board[0][0]
        elif self.board[0][2]==self.board[1][1]==self.board[2][0] !='.':
            return self.board[1][1]
            
        return None
    
    def move(self,row,col):
        if self.board[row][col]!='.':
            print('Invalid Move')
        else:
            self.board[row][col]=self.current_player
            if self.current_player=='X':
                self.current_player='O'
            else:
                self.current_player='X'

    def print_board(self):
        for row in self.board:
            for col in row:
                print(col, end=' ')
            print()


class Ai:
    def __init__(self,game,turn):
        self.game=game
        self.turn=turn

    def avail_mov(self):
        check_board=self.game.board
        avail_move=[]
        for row in range(3):
            for col in range(3):
                if check_board[row][col]=='.':
                    avail_move.append((row,col))
        return avail_move
    

    def score(self,p1,alpha,beta):
        champ=self.game.winner()
        # print(champ)
        if self.game.game_over()==True:
            
            if champ=='X':
                return -1
            elif champ=='O':
                return 1
            else:
                return 0
        
        if p1=='O':
            best_score=-math.inf
            for i in self.avail_mov():
                self.game.board[i[0]][i[1]]=p1
                current_score=self.score('X',alpha,beta)
                self.game.board[i[0]][i[1]]='.'
                if current_score>best_score:
                    best_score=current_score
                if best_score>=beta:
                    return best_score
                alpha=max(alpha, best_score)
            return best_score
        

        if p1=='X':
            best_score=math.inf
            for i in self.avail_mov():
                self.game.board[i[0]][i[1]]=p1
                current_score=self.score('O',alpha,beta)
                self.game.board[i[0]][i[1]]='.'
                if current_score<best_score:
                    best_score=current_score
                if best_score<=alpha:
                    return best_score
                beta=min(beta,best_score)
            return best_score



    def best_move(self):
        best_mov=None
        best_score=-math.inf
        #print(self.avail_mov())
        for i in self.avail_mov():
            # print(self.turn)
            self.game.board[i[0]][i[1]]=self.turn
            current_score=self.score('X',-float('inf'),float('inf'))
            self.game.board[i[0]][i[1]]='.'
            # print(current_score)
            if current_score>best_score:
                best_score=current_score
                best_mov=i
        
        return best_mov





multiplayer=Tictactoe()
ai1=Ai(multiplayer,'O')
turn=0
while True:
    
    if turn %2==0:
        multiplayer.print_board()
        row=int(input("Enter Row: "))
        col=int(input("Enter Col: "))
    else:
        row,col=ai1.best_move()
    multiplayer.move(row,col)
    if multiplayer.game_over()==True:
        if multiplayer.winner()!=None:
            print('{} wins!'.format(multiplayer.winner()))
        else:
            print('Its a tie')
        break

    turn+=1