class Solution(object):
  def leastBricks(self, wall):
    """
    :type wall: List[List[int]]
    :rtype: int
    """
    ans = len(wall)
    count = 0
    d = {}
    for w in wall:
      coverage = 0
      for brick in w[:-1]:
        coverage += brick
        d[coverage] = d.get(coverage, 0) + 1
        count = max(count, d.get(coverage, 0))
    return ans - count
