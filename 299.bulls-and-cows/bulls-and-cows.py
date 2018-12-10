from collections import Counter


class Solution(object):
  def getHint(self, secret, guess):
    """
    :type secret: str
    :type guess: str
    :rtype: str
    """
    a = b = 0
    ds = Counter()
    dg = Counter()
    for i in range(len(secret)):
      s = secret[i]
      g = guess[i]
      if secret[i] == guess[i]:
        a += 1
      else:
        ds[s] += 1
        dg[g] += 1
        if ds[g] > 0:
          b += 1
          dg[g] -= 1
          ds[g] -= 1
        if dg[s] > 0:
          b += 1
          ds[s] -= 1
          dg[s] -= 1
    return "{}A{}B".format(a, b)
