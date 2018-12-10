class UnionFind():
  def __init__(self, m, n):
    self.dad = [i for i in range(0, m * n)]
    self.rank = [0 for i in range(0, m * n)]
    self.m = m
    self.n = n

  def find(self, x):
    dad = self.dad
    if dad[x] != x:
      dad[x] = self.find(dad[x])
    return dad[x]

  def union(self, xy):
    dad = self.dad
    rank = self.rank
    x, y = map(self.find, xy)
    if x == y:
      return False
    if rank[x] > rank[y]:
      dad[y] = x
    else:
      dad[x] = y
      if rank[x] == rank[y]:
        rank[y] += 1
    return True


class Solution:
  # @param {list[list[str]]} board a 2D board containing 'X' and 'O'
  # @return nothing 
  def solve(self, board):
    # Write your code here
    if len(board) == 0:
      return
    regions = set([])
    n, m = len(board), len(board[0])
    uf = UnionFind(len(board[0]), len(board))
    directions = {"u": (-1, 0), "d": (1, 0), "l": (0, -1), "r": (0, 1)}
    for i in range(0, len(board)):
      for j in range(0, len(board[0])):
        if board[i][j] == 'X':
          continue
        for d in ["d", "r"]:
          di, dj = directions[d]
          newi, newj = i + di, j + dj
          if newi >= 0 and newi < len(board) and newj >= 0 and newj < len(board[0]):
            if board[newi][newj] == "O":
              uf.union((newi * m + newj, i * m + j))

    for i in range(0, len(board)):
      for j in [0, len(board[0]) - 1]:
        if board[i][j] == "O":
          regions.add(uf.find(i * m + j))

    for j in range(0, len(board[0])):
      for i in [0, len(board) - 1]:
        if board[i][j] == "O":
          regions.add(uf.find(i * m + j))

    for i in range(0, len(board)):
      for j in range(0, len(board[0])):
        if board[i][j] == "O" and uf.find(i * m + j) not in regions:
          board[i][j] = "X"
