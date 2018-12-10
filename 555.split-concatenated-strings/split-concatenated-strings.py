class Solution(object):
  def splitLoopedString(self, strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    ans = ""
    for i in range(len(strs)):
      strs[i] = max(strs[i], strs[i][::-1])

    for i, word in enumerate(strs):
      for start in [word, word[::-1]]:
        for cut in range(len(start)):
          ans = max(ans, start[cut:] + "".join(strs[i + 1:] + strs[:i]) + start[:cut])

    return ans
