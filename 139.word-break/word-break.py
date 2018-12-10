class Solution(object):
  def wordBreak(self, s, wordDict):
    """
    :type s: str
    :type wordDict: Set[str]
    :rtype: bool
    """
    queue = [0]
    ls = len(s)
    lenList = [l for l in set(map(len, wordDict))]
    visited = [0 for _ in range(0, ls + 1)]
    while queue:
      start = queue.pop(0)
      for l in lenList:
        if s[start:start + l] in wordDict:
          if start + l == ls:
            return True
          if visited[start + l] == 0:
            queue.append(start + l)
            visited[start + l] = 1
    return False
