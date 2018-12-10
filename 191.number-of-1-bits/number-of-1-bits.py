class Solution(object):
  def hammingWeight(self, n):
    """
    :type n: int
    :rtype: int
    """
    ans = 0
    while n > 0:
      n -= (n & -n)
      ans += 1
    return ans
