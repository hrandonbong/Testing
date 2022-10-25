class TicTac:
    def __init__(self):
        self.board = [['-','-','-'],
                      ['-','-','-'],
                      ['-','-','-']]
        self.turn = 'X'
        self.winner = None

    def start(self):
        while True:
            print('It is your turn ', self.turn)
            i, j = list(map(int, input("Enter row and column numbers with a space in between: ").split()))
            while self.board[i][j] != '-':
                print('Invalid Spot')
                print('It is your turn ', self.turn)
                i, j = list(map(int, input("Enter row and column with a space in between: ").split()))

            self.board[i][j] = self.turn

            if self.check():
                print("We have a winner")
                print("Congratulations ", self.winner)
                break

            if self.turn == 'O':
                self.turn = 'X'
            else:
                self.turn = 'O'

            for k in self.board:
                print(k)
            print('\n')


    def check(self):
        for i in range(3):
            if self.board[i][0] != '-':
                if self.row(i) or self.diag():
                    return True

        for j in range(3):
            if self.board[0][j] != '-':
                if self.column(j) or self.diag():
                    return True

        return False

    def row(self, i):
        if self.board[i] == ['X','X','X']:
            self.winner = 'X'
            return True
        elif self.board[i] == ['O','O','O']:
            self.winner = 'O'
            return True
        return False

    def column(self, j):
        local_x = 3
        local_o = 3
        for i in range(3):
            if self.board[i][j] == 'X':
                local_x -= 1
            if self.board[i][j] == 'O':
                local_o -= 1

        if local_x == 0:
            self.winner = 'X'
        if local_o == 0:
            self.winner = 'O'

        return True if local_x == 0 or local_o == 0 else False

    def diag(self):
        x_count = 3
        o_count = 3

        # Left to right
        for i in range(3):
            if self.board[i][i] == 'X':
                x_count -= 1
            if self.board[i][i] == 'O':
                o_count -= 1

        if x_count == 0:
            self.winner = 'X'
        if o_count == 0:
            self.winner = 'O'
        if x_count==0 or o_count == 0:
            return True

        x_count = 3
        o_count = 3

        # Right to left
        for i in range(2, -1, -1):
            if self.board[2-i][i] == 'X':
                x_count -= 1
            if self.board[2-i][i] == 'O':
                o_count -= 1

        if x_count == 0:
            self.winner = 'X'
        if o_count == 0:
            self.winner = 'O'
        if x_count==0 or o_count == 0:
            return True
        return False

TicTac().start()