class Solution(object):
  def getFactors(self, n):
    """
    :type n: int
    :rtype: List[List[int]]
    """
    res = []
    self.dfsHelper(n, res, [], 2)
    return res[1:]

  def dfsHelper(self, n, res, path, start):
    if len(path) > 1 and path[-2] > path[-1]:
      return

    if n == 1:
      res.append(path + [])
      return

    path.append(n)
    self.dfsHelper(n / n, res, path, n)
    path.pop()

    for i in range(start, int(n ** 0.5) + 1):
      if n % i == 0:
        path.append(i)
        self.dfsHelper(n / i, res, path, i)
        path.pop()
