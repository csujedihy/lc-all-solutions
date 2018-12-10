class Solution(object):
  def findTheDifference(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    """
    sum1 = sum(map(ord, [c for c in s]))
    sum2 = sum(map(ord, [c for c in t]))
    return chr(sum2 - sum1)
