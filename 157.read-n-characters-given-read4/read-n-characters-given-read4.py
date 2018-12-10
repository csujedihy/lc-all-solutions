# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
  def read(self, buf, n):
    """
    :type buf: Destination buffer (List[str])
    :type n: Maximum number of characters to read (int)
    :rtype: The number of characters read (int)
    """
    cnt = 0
    tmp = [""] * 4
    while cnt < n:
      r = read4(tmp)
      if r == 0:
        break
      for i in range(min(r, n - cnt)):
        buf[cnt] = tmp[i]
        cnt += 1
    return cnt
