class Solution(object):
  def findRadius(self, houses, heaters):
    """
    :type houses: List[int]
    :type heaters: List[int]
    :rtype: int
    """
    minDist = 0
    heaters.sort()
    for house in sorted(houses):
      idx = bisect.bisect_left(heaters, house)
      dist = float("inf")
      if idx > 0:
        dist = min(dist, abs(house - heaters[idx - 1]))
      if idx < len(heaters) - 1:
        dist = min(dist, abs(house - heaters[idx + 1]))
      if idx < len(heaters):
        dist = min(dist, abs(house - heaters[idx]))
      minDist = max(minDist, dist)
    return minDist
