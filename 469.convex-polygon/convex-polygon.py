class Solution(object):
  def isConvex(self, points):
    """
    :type points: List[List[int]]
    :rtype: bool
    """
    calcDir = lambda x, y, z: (y[0] - x[0]) * (z[1] - x[1]) - (y[1] - x[1]) * (z[0] - x[0])
    pre = None
    for i in range(0, len(points) - 2):
      x = points[i]
      y = points[i + 1]
      z = points[i + 2]
      c = calcDir(x, y, z)
      if c == 0:
        continue
      if pre is None:
        pre = c
      if pre * c < 0:
        return False
      pre = c
    if pre * calcDir(points[-1], points[0], points[1]) < 0:
      return False
    if pre * calcDir(points[-2], points[-1], points[0]) < 0:
      return False
    return True
