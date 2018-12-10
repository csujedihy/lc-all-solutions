class Solution(object):
  # while loop
  def smallestFactorization(self, a):
    """
    :type a: int
    :rtype: int
    """
    if a < 10:
      return a
    path = []
    k = 9
    while k > 1 and a > 1:
      if a % k == 0:
        path.append(str(k))
        a /= k
      else:
        k -= 1
    path.sort()
    if a > 9 or not path:
      return 0
    ans = int("".join(path))
    return ans if ans <= 0x7fffffff else 0

  # normal DFS
  def smallestFactorization(self, a):
    """
    :type a: int
    :rtype: int
    """
    if a <= 1:
      return a

    def dfs(num, path):
      if num == 1:
        self.ans = min(self.ans, int("".join(sorted(path))))
        return True
      for i in reversed(range(2, 10)):
        if num % i == 0:
          path.append(str(i))
          if dfs(num / i, path):
            return True
          path.pop()
      return False

    self.ans = float("inf")
    dfs(a, [])
    return self.ans if self.ans != float("inf") and self.ans <= 0x7fffffff else 0
