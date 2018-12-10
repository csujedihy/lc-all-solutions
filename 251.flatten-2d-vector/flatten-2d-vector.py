class Vector2D(object):

  def __init__(self, vec2d):
    """
    Initialize your data structure here.
    :type vec2d: List[List[int]]
    """
    self.x = self.y = 0
    self.m = vec2d

  def next(self):
    """
    :rtype: int
    """
    self.y += 1
    return self.m[self.x][self.y - 1]

  def hasNext(self):
    """
    :rtype: bool
    """
    m = self.m
    while self.x < len(m) and self.y >= len(m[self.x]):
      self.x += 1
      self.y = 0
    return self.x < len(m)

# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())
