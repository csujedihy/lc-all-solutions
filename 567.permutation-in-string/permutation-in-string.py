class Solution(object):
  def checkInclusion(self, s1, s2):
    """
    :type s1: str
    :type s2: str
    :rtype: bool
    """
    d = {}
    n = len(s1)
    for c in s1:
      d[c] = d.get(c, 0) + 1
    window = {}
    for i, c in enumerate(s2):
      window[c] = window.get(c, 0) + 1
      if i >= len(s1):
        window[s2[i - n]] = window.get(s2[i - n], 0) - 1
        if window[s2[i - n]] == 0:
          del window[s2[i - n]]
      if window == d:
        return True
    return False
