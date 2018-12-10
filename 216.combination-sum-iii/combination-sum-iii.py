class Solution(object):
  def combinationSum3(self, k, n):
    """
    :type k: int
    :type n: int
    :rtype: List[List[int]]
    """

    def dfs(k, start, path, subsum, res, visited):
      if len(path) == k and subsum == 0:
        res.append(path + [])
        return
      if len(path) >= k or subsum <= 0:
        return

      for i in range(start, 10):
        if visited[i] == 0:
          visited[i] = 1
          path.append(i)
          dfs(k, i + 1, path, subsum - i, res, visited)
          visited[i] = 0
          path.pop()

    visited = [0] * 10
    res = []
    dfs(k, 1, [], n, res, visited)
    return res
