class Solution(object):
  def magicalString(self, n):
    """
    :type n: int
    :rtype: int
    """
    s = "122"
    p = 2
    while len(s) < n:
      s += str((3 - int(s[-1]))) * int(s[p])
      p += 1
    return s[:n].count("1")
