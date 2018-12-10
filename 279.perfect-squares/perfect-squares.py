class Solution(object):
  def numSquares(self, n):
    """
    :type n: int
    :rtype: int
    """
    squares = []
    j = 1
    while j * j <= n:
      squares.append(j * j)
      j += 1
    level = 0
    queue = [n]
    visited = [False] * (n + 1)
    while queue:
      level += 1
      temp = []
      for q in queue:
        for factor in squares:
          if q - factor == 0:
            return level
          if q - factor < 0:
            break
          if visited[q - factor]:
            continue
          temp.append(q - factor)
          visited[q - factor] = True
      queue = temp
    return level
