class Solution(object):
  def findLUSlength(self, strs):
    """
    :type strs: List[str]
    :rtype: int
    """

    def findLUSlength(a, b):
      return max(len(a), len(b)) if a != b else -1

    def isSubsequence(s, t):
      d = collections.defaultdict(list)
      for i, c in enumerate(t):
        d[c].append(i)
      start = 0
      for c in s:
        idx = bisect.bisect_left(d[c], start)
        if len(d[c]) == 0 or idx >= len(d[c]):
          return False
        start = d[c][idx] + 1
      return True

    ans = -1
    strs.sort(key=len, reverse=True)
    for i in range(len(strs)):
      flag = True
      for j in range(len(strs)):
        if i != j and (findLUSlength(strs[i], strs[j]) == -1 or isSubsequence(strs[i], strs[j])):
          flag = False
          break
      if flag:
        return len(strs[i])
    return -1
