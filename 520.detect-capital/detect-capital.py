import string


class Solution(object):
  def detectCapitalUse(self, word):
    """
    :type word: str
    :rtype: bool
    """
    ud = set(string.uppercase)
    ld = set(string.lowercase)
    n = len(word)
    cap = 0
    for c in word:
      if c in ud:
        cap += 1
    if cap == n:
      return True
    if cap == 1 and word[0] in ud:
      return True
    return False if cap > 0 else True
