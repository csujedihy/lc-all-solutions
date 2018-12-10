class Solution(object):
  def isScramble(self, s1, s2):
    """
    :type s1: str
    :type s2: str
    :rtype: bool
    """
    n = len(s1)
    m = len(s2)
    if sorted(s1) != sorted(s2):
      return False

    if n < 4 or s1 == s2:
      return True

    for i in range(1, n):
      if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
        return True
      if self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i]):
        return True
    return False
