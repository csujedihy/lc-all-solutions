from collections import Counter


class Solution(object):
  def frequencySort(self, s):
    """
    :type s: str
    :rtype: str
    """
    d = Counter(s)
    buf = {}
    for k, v in d.items():
      buf[v] = buf.get(v, "") + k * v
    ans = ""
    for i in reversed(range(0, len(s))):
      ans += buf.get(i, "")
    return ans
