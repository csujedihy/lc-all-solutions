class Solution(object):
  def countBattleships(self, board):
    """
    :type board: List[List[str]]
    :rtype: int
    """
    ans = 0
    for i in range(0, len(board)):
      for j in range(0, len(board[0])):
        if board[i][j] == "X" and (i == 0 or board[i - 1][j] != "X") and (j == 0 or board[i][j - 1] != "X"):
          ans += 1
    return ans
