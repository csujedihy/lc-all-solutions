class RandomizedCollection(object):
  def __init__(self):
    """
    Initialize your data structure here.
    """
    self.dOfd = collections.defaultdict(dict)
    self.d = collections.defaultdict(list)
    self.a = []

  def insert(self, val):
    """
    Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
    :type val: int
    :rtype: bool
    """
    self.d[val].append(len(self.a))
    self.dOfd[val][len(self.a)] = len(self.d[val]) - 1
    self.a.append(val)
    return len(self.d[val]) == 1

  def remove(self, val):
    """
    Removes a value from the collection. Returns true if the collection contained the specified element.
    :type val: int
    :rtype: bool
    """
    dd = self.dOfd
    a = self.a
    d = self.d
    if not d[val]:
      return False
    idx = d[val][-1]
    a[idx] = a[-1]
    idxInDForLast = dd[a[-1]][len(a) - 1]
    d[a[-1]][idxInDForLast] = idx
    dd[a[-1]][idx] = idxInDForLast

    # del dd[val][idx]
    del dd[a[-1]][len(a) - 1]
    d[val].pop()
    a.pop()
    return True

  def getRandom(self):
    """
    Get a random element from the collection.
    :rtype: int
    """
    return self.a[random.randrange(0, len(self.a))]

# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
