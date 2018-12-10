class Solution(object):
  def grayCode(self, n):
    """
    :type n: int
    :rtype: List[int]
    """
    if n < 1:
      return [0]
    ans = [0] * (2 ** n)
    ans[1] = 1
    mask = 0x01
    i = 1
    while i < n:
      mask <<= 1
      for j in range(0, 2 ** i):
        root = (2 ** i)
        ans[root + j] = ans[root - j - 1] | mask
      i += 1
    return ans
