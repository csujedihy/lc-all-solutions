import collections


class Solution(object):
  def findRotateSteps(self, ring, key):
    """
    :type ring: str
    :type key: str
    :rtype: int
    """

    def dfs(ring, key, pointTo, d, length, cache):
      if (pointTo, key) in cache:
        return cache[pointTo, key]
      if not key:
        return 0
      minDist = float("inf")
      toChar = key[0]
      for i in d[toChar]:
        cost = min(length - abs(pointTo - i), abs(pointTo - i)) + 1
        cost += dfs(ring, key[1:], i, d, length, cache)
        minDist = min(minDist, cost)
      cache[pointTo, key] = minDist
      return minDist

    cache = {}
    d = collections.defaultdict(list)
    for i, c in enumerate(ring):
      d[c].append(i)
    length = len(ring)
    return dfs(ring, key, 0, d, length, cache)
