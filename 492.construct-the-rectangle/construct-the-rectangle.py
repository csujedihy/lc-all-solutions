class Solution(object):
  def constructRectangle(self, area):
    """
    :type area: int
    :rtype: List[int]
    """
    root = int(area ** 0.5)
    while root > 0:
      if area % root == 0:
        return int(area / root), root
      root -= 1
