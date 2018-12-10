class Solution(object):
  def checkRecord(self, s):
    """
    :type s: str
    :rtype: bool
    """
    a = l = 0
    for c in s:
      if c == "L":
        l += 1
      elif c == "A":
        a += 1
        l = 0
      else:
        l = 0
      if a > 1 or l > 2:
        return False
    return True
