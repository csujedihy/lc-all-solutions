class Solution(object):
  def shortestDistance(self, words, word1, word2):
    """
    :type words: List[str]
    :type word1: str
    :type word2: str
    :rtype: int
    """
    idx1 = idx2 = -1
    ans = len(words)
    for i in range(0, len(words)):
      word = words[i]
      if word in (word1, word2):
        if word == word1:
          idx1 = i
        elif word == word2:
          idx2 = i
        if idx1 != -1 and idx2 != -1:
          ans = min(ans, abs(idx2 - idx1))
    return ans
