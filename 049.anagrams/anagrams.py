class Solution(object):
  def groupAnagrams(self, strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """

    def hash(count):
      p1, p2 = 2903, 29947
      ret = 0
      for c in count:
        ret = ret * p1 + c
        p1 *= p2
      return ret

    d = {}

    for str in strs:
      count = [0] * 26
      for c in str:
        count[ord(c) - ord('a')] += 1
      key = hash(count)
      if key not in d:
        d[key] = [str]
      else:
        d[key].append(str)
    return [d[k] for k in d]
