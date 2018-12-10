class Solution(object):
  def findSubstringInWraproundString(self, p):
    """
    :type p: str
    :rtype: int
    """
    d = {}
    cnt = 0
    for i in range(len(p)):
      if i > 0 and (ord(p[i]) - ord(p[i - 1]) == 1 or ord(p[i - 1]) - ord(p[i]) == 25):
        cnt += 1
      else:
        cnt = 1
      d[ord(p[i])] = max(d.get(ord(p[i]), 0), cnt)

    return sum(d.values())
