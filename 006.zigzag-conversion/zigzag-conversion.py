class Solution(object):
  def convert(self, s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    if numRows <= 1:
      return s
    n = len(s)
    ans = []
    step = 2 * numRows - 2
    for i in range(numRows):
      one = i
      two = -i
      while one < n or two < n:
        if 0 <= two < n and one != two and i != numRows - 1:
          ans.append(s[two])
        if one < n:
          ans.append(s[one])
        one += step
        two += step
    return "".join(ans)
