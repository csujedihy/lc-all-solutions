class RandomizedSet(object):
  def __init__(self):
    """
    Initialize your data structure here.
    """
    self.d = {}
    self.a = []

  def insert(self, val):
    """
    Inserts a value to the set. Returns true if the set did not already contain the specified element.
    :type val: int
    :rtype: bool
    """
    if val in self.d:
      return False
    self.a.append(val)
    self.d[val] = len(self.a) - 1
    return True

  def remove(self, val):
    """
    Removes a value from the set. Returns true if the set contained the specified element.
    :type val: int
    :rtype: bool
    """
    if val not in self.d:
      return False
    index = self.d[val]
    self.a[index] = self.a[-1]
    self.d[self.a[-1]] = index
    self.a.pop()
    del self.d[val]
    return True

  def getRandom(self):
    """
    Get a random element from the set.
    :rtype: int
    """
    return self.a[random.randrange(0, len(self.a))]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
