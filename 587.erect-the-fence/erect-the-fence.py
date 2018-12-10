# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution(object):
  def outerTrees(self, points):
    """
    :type points: List[Point]
    :rtype: List[Point]
    """
    if len(points) == 1:
      return points

    def direction(p, q, r):
      return ((p.x - r.x) * (q.y - r.y) - (p.y - r.y) * (q.x - r.x))

    points.sort(key=lambda x: (x.x, x.y))
    upper = []
    lower = []
    for point in points:
      while len(lower) >= 2 and direction(lower[-2], lower[-1], point) < 0:
        lower.pop()
      lower.append(point)

    for point in reversed(points):
      while len(upper) >= 2 and direction(upper[-2], upper[-1], point) < 0:
        upper.pop()
      upper.append(point)

    return list(set(upper[1:] + lower[1:]))
