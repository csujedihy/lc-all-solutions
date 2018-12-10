# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution(object):
  def maxPoints(self, points):
    """
    :type points: List[Point]
    :rtype: int
    """

    def gcd(a, b):
      while b:
        a, b = b, a % b
      return a

    ans = 1
    d = {}
    points.sort(key=lambda p: (p.x, p.y))
    for i in range(0, len(points)):
      if i > 0 and (points[i].x, points[i].y) == (points[i - 1].x, points[i - 1].y):
        continue
      overlap = 1
      for j in range(i + 1, len(points)):
        x1, y1 = points[i].x, points[i].y
        x2, y2 = points[j].x, points[j].y
        ku, kd = y2 - y1, x2 - x1
        if (x1, y1) != (x2, y2):
          kg = gcd(ku, kd)
          ku /= kg
          kd /= kg
          d[(ku, kd, x1, y1)] = d.get((ku, kd, x1, y1), 0) + 1
        else:
          overlap += 1
          ans = max(ans, overlap)
        ans = max(ans, d.get((ku, kd, x1, y1), 0) + overlap)
    return min(ans, len(points))
