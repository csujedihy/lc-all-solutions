class TicTacToe(object):
  def __init__(self, n):
    self.rows = [0] * n
    self.cols = [0] * n
    self.diag = self.antiDiag = 0
    self.n = n

    def move(row, col, player):
      delta = 3 - player * 2
      self.rows[row] += delta
      self.cols[col] += delta
      self.diag += row == col and delta
      self.antiDiag += row + col == self.n - 1 and delta
      if delta * self.n in [self.rows[row], self.cols[col], self.diag, self.antiDiag]:
        return player
      return 0

    self.move = move

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
