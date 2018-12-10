class Solution(object):
  def candy(self, ratings):
    """
    :type ratings: List[int]
    :rtype: int
    """
    n = len(ratings)
    left = [1] * n
    ans = 0
    for i in range(1, n):
      if ratings[i] > ratings[i - 1]:
        left[i] = left[i - 1] + 1
    ans = left[-1]
    for i in reversed(range(0, n - 1)):
      if ratings[i] > ratings[i + 1]:
        left[i] = max(left[i], left[i + 1] + 1)
      ans += left[i]
    return ans
