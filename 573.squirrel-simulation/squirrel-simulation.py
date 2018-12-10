class Solution(object):
  def minDistance(self, height, width, tree, squirrel, nuts):
    """
    :type height: int
    :type width: int
    :type tree: List[int]
    :type squirrel: List[int]
    :type nuts: List[List[int]]
    :rtype: int
    """

    def dist(s, t):
      x1, y1 = s
      x2, y2 = t
      return abs(x1 - x2) + abs(y1 - y2)

    ans = 0
    for nut in nuts:
      ans += 2 * dist(tree, nut)

    ret = float("inf")
    for nut in nuts:
      ret = min(ret, ans - dist(nut, tree) + dist(nut, squirrel))
    return ret
