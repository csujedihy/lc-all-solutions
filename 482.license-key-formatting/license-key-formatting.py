class Solution(object):
  def licenseKeyFormatting(self, S, K):
    """
    :type S: str
    :type K: int
    :rtype: str
    """
    s = S.split("-")
    s = "".join(s)
    n = len(s)
    start = n % K
    res = []
    if start != 0:
      res.append(s[:start].upper())
    for k in range(0, (len(s) - start) / K):
      res.append(s[start:start + K].upper())
      start += K
    return "-".join(res)
