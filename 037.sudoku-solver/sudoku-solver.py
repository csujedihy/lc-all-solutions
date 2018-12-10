class Solution(object):
  def solveSudoku(self, board):
    """
    :type board: List[List[str]]
    :rtype: void Do not return anything, modify board in-place instead.
    """
    cacheBox = [[0] * len(board) for _ in range(len(board))]
    cacheRow = [[0] * len(board) for _ in range(len(board))]
    cacheCol = [[0] * len(board) for _ in range(len(board))]

    def helper(board, i, j, cacheRow, cacheCol, cacheBox):
      if board[i][j] == ".":
        for k in range(1, 10):
          if i < 0 or i >= len(board) or j < 0 or j >= len(board):
            continue
          ib = (i / 3) * 3 + j / 3
          if cacheRow[i][k - 1] == 1 or cacheCol[j][k - 1] == 1 or cacheBox[ib][k - 1] == 1:
            continue

          cacheRow[i][k - 1] = cacheCol[j][k - 1] = cacheBox[ib][k - 1] = 1
          board[i][j] = str(k)
          if i == j == len(board) - 1:
            return True
          if i + 1 < len(board):
            if helper(board, i + 1, j, cacheRow, cacheCol, cacheBox):
              return True
          elif j + 1 < len(board):
            if helper(board, 0, j + 1, cacheRow, cacheCol, cacheBox):
              return True
          board[i][j] = "."
          cacheRow[i][k - 1] = cacheCol[j][k - 1] = cacheBox[ib][k - 1] = 0
      else:
        if i == j == len(board) - 1:
          return True
        if i + 1 < len(board):
          if helper(board, i + 1, j, cacheRow, cacheCol, cacheBox):
            return True
        elif j + 1 < len(board):
          if helper(board, 0, j + 1, cacheRow, cacheCol, cacheBox):
            return True
      return False

    for i in range(len(board)):
      for j in range(len(board)):
        if board[i][j] != ".":
          ib = (i / 3) * 3 + j / 3
          k = int(board[i][j]) - 1
          cacheRow[i][k] = cacheCol[j][k] = cacheBox[ib][k] = 1
    print
    helper(board, 0, 0, cacheRow, cacheCol, cacheBox)
