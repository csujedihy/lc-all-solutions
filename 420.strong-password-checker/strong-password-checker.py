class Solution(object):
  def strongPasswordChecker(self, s):
    """
    :type s: str
    :rtype: int
    """
    complexBal = 3
    if any(c in string.lowercase for c in s):
      complexBal -= 1
    if any(c in string.uppercase for c in s):
      complexBal -= 1
    if any(c.isdigit() for c in s):
      complexBal -= 1

    one = 0
    two = 0
    p = 2
    replace = 0
    while p < len(s):
      if s[p] == s[p - 1] == s[p - 2]:
        length = 2
        while p < len(s) and s[p] == s[p - 1]:
          p += 1
          length += 1
        replace += length / 3
        if length % 3 == 0:
          one += 1
        if length % 3 == 1:
          two += 1
      else:
        p += 1

    if len(s) < 6:
      return max(complexBal, 6 - len(s))
    elif len(s) <= 20:
      return max(complexBal, replace)
    else:
      redundant = len(s) - 20
      replace -= min(redundant, one)
      replace -= min(max(redundant - one, 0), two * 2) / 2
      replace -= max(redundant - one - two * 2, 0) / 3
      return redundant + max(complexBal, replace)
