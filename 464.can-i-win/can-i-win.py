class Solution(object):
  def canIWin(self, maxChoosableInteger, desiredTotal):
    """
    :type maxChoosableInteger: int
    :type desiredTotal: int
    :rtype: bool
    """

    def helper(pool, target, visited):
      if pool in visited:
        return visited[pool]
      if target <= 0:
        return False
      if pool >= self.maxPool:
        return True

      mask = 0x01
      for i in range(0, maxChoosableInteger):
        if pool & mask == 0:
          newPool = pool | mask
          if helper(newPool, target - (i + 1), visited) == False:
            visited[pool] = True
            return True
        mask = mask << 1
      visited[pool] = False
      return False

    if (1 + maxChoosableInteger) * (maxChoosableInteger / 2) < desiredTotal:
      return False

    if desiredTotal == 0:
      return True
    self.maxPool = 0
    mask = 1
    for i in range(0, maxChoosableInteger):
      self.maxPool |= mask
      mask = mask << 1
    pool = 0
    visited = {}
    return helper(pool, desiredTotal, visited)
