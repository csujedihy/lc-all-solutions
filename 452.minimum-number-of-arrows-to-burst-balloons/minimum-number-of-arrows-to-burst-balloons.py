class Solution(object):
  def findMinArrowShots(self, points):
    """
    :type points: List[List[int]]
    :rtype: int
    """
    ans = 0
    points.sort(key=lambda p: p[1])
    end = float("-inf")
    for s, e in points:
      if s > end:
        ans += 1
        end = e
    return ans
