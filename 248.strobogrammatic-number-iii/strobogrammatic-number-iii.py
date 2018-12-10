class Solution(object):
  def findStrobogrammatic(self, n):
    """
    :type n: int
    :rtype: List[str]
    """
    self.d = {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}

    def dfs(half, path, n):
      if len(path) == half:
        pathStr = "".join(path)
        if half * 2 == n:
          toAppend = pathStr + "".join([self.d[x] for x in pathStr[::-1]])
          toAppendInt = int(toAppend)
          if self.low <= toAppendInt <= self.high:
            self.count += 1
        else:
          for c in "018":
            toAppend = pathStr + c + "".join([self.d[x] for x in pathStr[::-1]])
            toAppendInt = int(toAppend)
            if self.low <= toAppendInt <= self.high:
              self.count += 1
        return

      for c in "01689":
        if c == "0" and len(path) == 0:
          continue
        path.append(c)
        dfs(half, path, n)
        path.pop()

    res = []
    dfs(n / 2, [], n)
    return res

  def strobogrammaticInRange(self, low, high):
    """
    :type low: str
    :type high: str
    :rtype: int
    """
    if int(low) > int(high):
      return 0
    self.count = 0
    self.low = int(low)
    self.high = int(high)
    for length in range(len(low), len(high) + 1):
      self.findStrobogrammatic(length)
    return self.count
