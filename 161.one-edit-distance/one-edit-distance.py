class Solution(object):
  def isOneEditDistance(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    if len(s) >= len(t):
      i = 0
      while i < len(t) and s[i] == t[i]:
        i += 1
      return s != t and (s[i + 1:] == t[i:] if len(s) != len(t) else s[i + 1:] == t[i + 1:])
    else:
      return self.isOneEditDistance(t, s)
