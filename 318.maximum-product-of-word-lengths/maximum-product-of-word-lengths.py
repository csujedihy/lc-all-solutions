class Solution(object):
  def maxProduct(self, words):
    """
    :type words: List[str]
    :rtype: int
    """
    bitmap = [0] * len(words)
    mask = 0x01
    ans = 0
    for i in range(0, len(words)):
      word = words[i]
      for c in word:
        bitmap[i] |= (mask << (ord(c) - ord('a')))
    for i in range(0, len(words)):
      for j in range(0, i):
        if bitmap[i] & bitmap[j] == 0:
          ans = max(ans, len(words[i]) * len(words[j]))

    return ans
