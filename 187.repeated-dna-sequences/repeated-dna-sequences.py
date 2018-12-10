class Solution(object):
  def findRepeatedDnaSequences(self, s):
    """
    :type s: str
    :rtype: List[str]
    """
    d = {}
    ans = []
    for i in range(len(s) - 9):
      key = s[i:i + 10]
      if key in d:
        d[key] += 1
        if d[key] == 2:
          ans.append(key)
      else:
        d[key] = 1
    return ans
