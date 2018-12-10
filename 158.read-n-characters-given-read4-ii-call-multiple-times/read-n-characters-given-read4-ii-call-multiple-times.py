# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):
from collections import deque


class Solution(object):
  def __init__(self):
    self.rBuf = deque([])

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
      for i in range(r):
        self.rBuf.append(tmp[i])
      for i in range(min(n - cnt, len(self.rBuf))):
        buf[cnt] = self.rBuf.popleft()
        cnt += 1
      if r == 0:
        break
    return cnt
