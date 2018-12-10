# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger(object):
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
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

class Solution(object):
  def deserialize(self, s):
    """
    :type s: str
    :rtype: NestedInteger
    """

    def parse(s, i):
      if s[i] == "[":
        i += 1
        ret = NestedInteger()
        while i < len(s):
          if s[i] == "]":
            return ret, i + 1
          elif s[i] in "[-0123456789":
            res, i = parse(s, i)
            ret.add(res)
          else:
            i += 1
      else:
        j = i
        while j < len(s) and s[j] in "-0123456789":
          j += 1
        return NestedInteger(int(s[i:j])), j

    res, _ = parse(s, 0)
    return res
