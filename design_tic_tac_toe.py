# https://leetcode.com/problems/design-tic-tac-toe/
class TicTacToe(object):

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.n = n
        self.diagonal_1 = [0]*2
        self.diagonal_2 = [0] *2
        self.rows = [[0] * n, [0] * n]
        self.cols = [[0] * n, [0] * n]

    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        if row == col:
            self.diagonal_1[player-1] += 1
        if col == self.n - 1 - row:
            self.diagonal_2[player-1] += 1
        self.rows[player-1][row] += 1
        self.cols[player-1][col] += 1
        
        if (self.rows[player-1][row]) == self.n or (self.cols[player-1][col]) == self.n or self.diagonal_1[player-1] == self.n or self.diagonal_2[player-1] == self.n:        
            return player
        else:
            return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)