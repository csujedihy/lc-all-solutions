class StringIterator(object):

  def __init__(self, compressedString):
    """
    :type compressedString: str
    """
    self.data = compressedString
    self.idx = -1
    self.decodeNext()

  def decodeNext(self):
    self.idx += 1
    if self.idx + 1 < len(self.data):
      self.cur = self.data[self.idx]
      end = self.idx + 1
      while end < len(self.data) and self.data[end].isdigit():
        end += 1
      print
      end
      self.num = int(self.data[self.idx + 1:end])
      self.idx = end - 1

  def next(self):
    """
    :rtype: str
    """
    if self.hasNext():
      ret = self.cur
      self.num -= 1
      if self.num <= 0:
        self.decodeNext()
      return ret
    return " "

  def hasNext(self):
    """
    :rtype: bool
    """
    return self.idx < len(self.data) and self.num > 0

# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
