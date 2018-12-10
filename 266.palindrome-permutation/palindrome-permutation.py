class Solution(object):
  def canPermutePalindrome(self, s):
    """
    :type s: str
    :rtype: bool
    """
    evenCount = 0
    oddCount = 0
    d = {}
    for c in s:
      d[c] = d.get(c, 0) + 1
    for k in d:
      if d[k] % 2 == 1:
        oddCount += 1
      else:
        evenCount += 1

    if len(s) % 2 == 1:
      if oddCount == 1:
        return True
    else:
      if oddCount == 0:
        return True
    return False
