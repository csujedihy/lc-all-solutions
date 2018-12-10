class Solution(object):
  def isMatch(self, s, p):
    """
    :type s: str
    :type p: str
    :rtype: bool
    """
    i = j = 0
    lenS = len(s)
    lenP = len(p)
    lastMatchPos = 0
    lastStarPos = -1
    while i < len(s):
      if j < lenP and p[j] in (s[i], "?"):
        i += 1
        j += 1
      elif j < lenP and p[j] == "*":
        lastMatchPos = i
        lastStarPos = j
        j += 1
      elif lastStarPos > -1:
        i = lastMatchPos + 1
        lastMatchPos += 1
        j = lastStarPos + 1
      else:
        return False
    while j < lenP and p[j] == "*":
      j += 1
    return j == lenP
