class Solution(object):
  def generateAbbreviations(self, word):
    """
    :type word: str
    :rtype: List[str]
    """

    def dfs(w, start, res):
      res.append(w)
      for i in range(start, len(w)):
        for l in range(1, len(w) - i + 1):
          lstr = str(l)
          llen = len(lstr)
          dfs(w[:i] + lstr + w[i + l:], i + 2 + llen - 1, res)

    res = []
    dfs(word, 0, res)
    return res
