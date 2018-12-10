# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """
from collections import deque


class NestedIterator(object):

  def __init__(self, nestedList):
    """
    Initialize your data structure here.
    :type nestedList: List[NestedInteger]
    """
    self.stack = deque(nestedList[::-1])
    self.value = None

  def next(self):
    """
    :rtype: int
    """
    self.hasNext()
    ret = self.value
    self.value = None
    return ret

  def hasNext(self):
    """
    :rtype: bool
    """
    if self.value is not None:
      return True

    stack = self.stack
    while stack:
      top = stack.pop()
      if top.isInteger():
        self.value = top.getInteger()
        return True
      else:
        stack.extend(top.getList()[::-1])
    return False

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
