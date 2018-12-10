class Solution(object):
  def shortestWordDistance(self, words, word1, word2):
    """
    :type words: List[str]
    :type word1: str
    :type word2: str
    :rtype: int
    """
    ans = float("inf")
    idx1 = idx2 = -1
    for i in range(0, len(words)):
      word = words[i]
      if word in (word1, word2):
        if word == word1:
          idx1 = i
          if idx2 != -1 and idx1 != idx2:
            ans = min(ans, abs(idx2 - idx1))
        if word == word2:
          idx2 = i
          if idx1 != -1 and idx1 != idx2:
            ans = min(ans, abs(idx2 - idx1))
    return ans
