class Solution(object):
  # naive pre-order traversal on denary tree
  def _findKthNumber(self, n, k):
    """
    :type n: int
    :type k: int
    :rtype: int
    """

    def dfs(cur, n):
      if self.k == 0:
        return cur
      self.k -= 1
      if cur == 0:
        for i in range(1, 10):
          if i > n:
            break
          ret = dfs(i, n)
          if ret:
            return ret
      else:
        for i in range(0, 10):
          if cur * 10 + i > n:
            break
          ret = dfs(cur * 10 + i, n)
          if ret:
            return ret

    self.k = k
    return dfs(0, n)

  # optimized solution
  def findKthNumber(self, n, k):
    def getGap(n, ans):
      gap = 0
      start = ans
      end = start + 1
      while start <= n:
        gap += max(0, min(n + 1, end) - start)
        start *= 10
        end *= 10
      return gap

    ans = 1
    k -= 1
    while k > 0:
      gap = getGap(n, ans)
      if gap <= k:
        ans += 1
        k -= gap
      else:
        ans *= 10
        k -= 1
    return ans
