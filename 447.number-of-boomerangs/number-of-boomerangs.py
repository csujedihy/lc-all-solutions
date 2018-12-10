class Solution(object):
  def numberOfBoomerangs(self, points):
    """
    :type points: List[List[int]]
    :rtype: int
    """
    # idea:
    # we compute the distance starting from any given point and we use a hashtable to count the number of the same distance obtained
    # once we finish counting distance for one point, we calculate the combinations = 1 * C^1_N * C^1_(N-1)
    ans = 0
    for p1 in points:
      d = {}
      for p2 in points:
        if p1 != p2:
          dist = (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2
          d[dist] = d.get(dist, 0) + 1
      for k in d:
        ans += d[k] * (d[k] - 1)
    return ans
