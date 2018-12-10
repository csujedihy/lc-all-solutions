import collections


class Solution(object):
  def findLongestWord(self, s, d):
    """
    :type s: str
    :type d: List[str]
    :rtype: str
    """
    d.sort(key=lambda x: (-len(x), x))

    def isSubseq(word, s):
      i = 0
      for c in s:
        if c == word[i]:
          i += 1
        if i == len(word):
          return True
      return False

    for word in d:
      if isSubseq(word, s):
        return word
    return ""
