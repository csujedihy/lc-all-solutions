class Solution(object):
  # brutal force TLE
  def _shortestPalindrome(self, s):
    """
    :type s: str
    :rtype: str
    """

    def isPal(cand):
      start, end = 0, len(cand) - 1
      while start < end:
        if cand[start] != cand[end]:
          return False
        start += 1
        end -= 1
      return True

    n = len(s)
    ans = s[::-1] + s
    ansLen = 2 * len(s)
    for i in reversed(range(0, len(s) + 1)):
      newPal = s[i:][::-1] + s
      if isPal(newPal) and n + len(s) - i < ansLen:
        ansLen = n + len(s) - i
        ans = newPal
    return ans

  def shortestPalindrome(self, s):
    r = s[::-1]
    for i in range(len(s) + 1):
      if s.startswith(r[i:]):
        return r[:i] + s
