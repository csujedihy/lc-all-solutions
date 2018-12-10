class Solution(object):
  def countArrangement(self, N):
    """
    :type N: int
    :rtype: int
    """

    def dfs(pos, unused):
      if len(unused) == 0:
        return 1
      ret = 0
      for num in list(unused):
        if pos % num == 0 or num % pos == 0:
          unused -= {num}
          ret += dfs(pos + 1, unused)
          unused |= {num}
      return ret

    return dfs(1, set([i for i in range(1, N + 1)]))
