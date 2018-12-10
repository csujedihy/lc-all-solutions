class Solution(object):
  def lexicalOrder(self, n):
    """
    :type n: int
    :rtype: List[int]
    """
    ans = [0] * n
    self.cnt = 0
    self.dfs(ans, n, 0)
    return ans

  def dfs(self, ans, n, pre):
    if self.cnt == n or pre > n:
      return
    if pre * 10 > n:
      return
    for i in range(0, 10):
      cur = pre * 10 + i
      if cur == 0:
        continue
      if self.cnt == n or cur > n:
        return
      ans[self.cnt] = cur
      self.cnt += 1
      self.dfs(ans, n, cur)
