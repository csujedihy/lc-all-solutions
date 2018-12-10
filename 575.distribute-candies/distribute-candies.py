class Solution(object):
  def distributeCandies(self, candies):
    """
    :type candies: List[int]
    :rtype: int
    """
    return min(len(candies) / 2, len(set(candies)))
