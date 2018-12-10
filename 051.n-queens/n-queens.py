class Solution(object):
  def solveNQueens(self, n):
    """
    :type n: int
    :rtype: List[List[str]]
    """
    ans = []

    def dfs(path, n, ans):
      if len(path) == n:
        ans.append(drawChess(path))
        return

      for i in range(n):
        if i not in path and isValidQueen(path, i):
          path.append(i)
          dfs(path, n, ans)
          path.pop()

    def isValidQueen(path, k):
      for i in range(len(path)):
        if abs(k - path[i]) == abs(len(path) - i):
          return False
      return True

    def drawChess(path):
      ret = []
      chess = [["."] * len(path) for _ in range(len(path))]
      for i in range(0, len(path)):
        chess[i][path[i]] = "Q"
      for chs in chess:
        ret.append("".join(chs))
      return ret

    dfs([], n, ans)
    return ans
