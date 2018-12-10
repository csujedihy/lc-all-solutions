class Solution(object):
  def convertToTitle(self, n):
    """
    :type n: int
    :rtype: str
    """
    ans = ""
    while n > 0:
      y = n % 26
      if y == 0:
        char = "Z"
        n -= 26
      else:
        char = chr(ord("A") + y - 1)
      ans += char
      n = n / 26
    return ans[::-1]
