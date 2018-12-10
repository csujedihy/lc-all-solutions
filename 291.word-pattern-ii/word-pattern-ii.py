class Solution(object):
  def wordPatternMatch(self, pattern, str):
    """
    :type pattern: str
    :type str: str
    :rtype: bool
    """

    def dfs(p, s, pathp, paths, visited):
      if len(p) == len(s) == 0:
        return True
      if len(p) == 0 or len(p) > len(s):
        return False
      for i in range(0, len(s)):
        pathp.append(p[0])
        paths.append(s[:i + 1])
        if len(pathp) == len(paths) and len(set(paths)) == len(set(pathp)) == len(set(zip(paths, pathp))):
          if dfs(p[1:], s[i + 1:], pathp, paths, visited):
            return True
        pathp.pop()
        paths.pop()
      return False

    return dfs(pattern, str, [], [], {})
