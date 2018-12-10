class Solution(object):
  def minAbbreviation(self, target, dictionary):
    """
    :type target: str
    :type dictionary: List[str]
    :rtype: str
    """

    def dfs(w, start, res):
      res.append(w)
      for i in range(start, len(w)):
        for l in reversed(range(1, len(w) - i + 1)):
          dfs(w[:i] + [str(l)] + w[i + l:], i + 2, res)

    def match(src, dest):
      i = 0
      for c in src:
        if c.isdigit():
          jump = int(c)
          i += jump
        else:
          if c != dest[i]:
            return False
          i += 1
      return True

    if not dictionary:
      return str(len(target))
    wordLen = len(target)
    res = []
    dfs(list(target), 0, res)
    res.sort(key=lambda x: len(x))
    dictionary = filter(lambda s: len(s) == wordLen, dictionary)

    for w in res:
      allMiss = True
      for d in dictionary:
        if match(w, d):
          allMiss = False
          break
      if allMiss:
        return "".join(w)
    return None
