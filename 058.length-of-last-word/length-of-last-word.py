class Solution(object):
  def lengthOfLastWord(self, s):
    """
    :type s: str
    :rtype: int
    """
    if len(s) == 0:
      return 0
    s = s.split()
    if len(s) > 0:
      return len(s[-1])
    return 0
