class Solution(object):
  def wordPattern(self, pattern, str):
    """
    :type pattern: str
    :type str: str
    :rtype: bool
    """
    str = str.split()
    a = zip(pattern, str)
    print
    a
    return len(pattern) == len(str) and len(set(a)) == len(set(pattern)) == len(set(str))
