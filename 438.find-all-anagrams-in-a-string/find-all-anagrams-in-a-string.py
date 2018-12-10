from collections import Counter


class Solution(object):
  def findAnagrams(self, s, p):
    """
    :type s: str
    :type p: str
    :rtype: List[int]
    """
    sCount = Counter(s[:len(p) - 1])
    pCount = Counter(p)
    ans = []

    for i in range(len(p) - 1, len(s)):
      sCount[s[i]] += 1
      if sCount == pCount:
        ans.append(i - len(p) + 1)
      sCount[s[i - len(p) + 1]] -= 1
      if sCount[s[i - len(p) + 1]] == 0:
        del sCount[s[i - len(p) + 1]]
    return ans
