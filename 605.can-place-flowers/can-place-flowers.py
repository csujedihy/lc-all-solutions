class Solution(object):
  def canPlaceFlowers(self, flowerbed, n):
    """
    :type flowerbed: List[int]
    :type n: int
    :rtype: bool
    """
    ans = 0
    cnt = 1
    for plot in flowerbed:
      if plot == 0:
        cnt += 1
      else:
        ans += abs(cnt - 1) / 2
        cnt = 0
    return ans + cnt / 2 >= n
