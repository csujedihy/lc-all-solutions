class Solution(object):
  def lengthOfLongestSubstringKDistinct(self, s, k):
    """
    :type s: str
    :type k: int
    :rtype: int
    """
    j = 0
    ans = 0
    dict = {}
    for i in range(len(s)):
      dict[s[i]] = dict.get(s[i], 0) + 1
      while j <= i and len(dict) > k:
        dict[s[j]] -= 1
        if dict[s[j]] == 0:
          del dict[s[j]]
        j += 1
      ans = max(ans, i - j + 1)
    return ans
