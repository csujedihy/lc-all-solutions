class Solution(object):
  def gameOfLife(self, board):
    """
    :type board: List[List[int]]
    :rtype: void Do not return anything, modify board in-place instead.
    """

    def helper(board, p, q):
      cnt = 0
      for i in range(p - 1, p + 2):
        for j in range(q - 1, q + 2):
          if i == p and j == q:
            continue
          if 0 <= i < len(board) and 0 <= j < len(board[0]) and board[i][j] & 1:
            cnt += 1
      if cnt == 3 or (board[p][q] == 1 and cnt == 2):
        board[p][q] |= 2

    for i in range(0, len(board)):
      for j in range(0, len(board[0])):
        helper(board, i, j)

    for i in range(0, len(board)):
      for j in range(0, len(board[0])):
        board[i][j] >>= 1
