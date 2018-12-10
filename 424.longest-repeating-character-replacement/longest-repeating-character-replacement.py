from collections import deque


class Solution(object):
  def characterReplacement(self, s, k):
    """
    :type s: str
    :type k: int
    :rtype: int
    """
    ans = 0
    d = {}
    start = 0
    maxCount = 0
    window = deque([])
    for end in range(0, len(s)):
      d[s[end]] = d.get(s[end], 0) + 1
      maxCount = max(maxCount, d[s[end]])
      if end - start + 1 - maxCount > k:
        d[s[start]] -= 1
        start += 1
      ans = max(ans, end - start + 1)
    return ans
