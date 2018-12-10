class Solution(object):
  def firstUniqChar(self, s):
    """
    :type s: str
    :rtype: int
    """
    letters = [0] * 26
    for c in s:
      ci = ord(c) - ord('a')
      letters[ci] += 1
    for i in range(0, len(s)):
      ci = ord(s[i]) - ord('a')
      if letters[ci] == 1:
        return i
    return -1
