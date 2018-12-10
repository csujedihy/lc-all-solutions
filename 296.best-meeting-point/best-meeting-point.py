class Solution(object):
  def minTotalDistance(self, grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    iList, jList, ppl = [], [], []
    for i in range(0, len(grid)):
      for j in range(0, len(grid[0])):
        if grid[i][j] == 1:
          ppl.append((i, j))
          iList.append(i)
          jList.append(j)
    jList.sort()
    m = (iList[len(iList) / 2], jList[len(jList) / 2])
    return sum(map(lambda p: abs(p[1] - m[1]) + abs(p[0] - m[0]), ppl))
