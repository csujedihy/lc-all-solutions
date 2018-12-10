# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
  def findCelebrity(self, n):
    """
    :type n: int
    :rtype: int
    """
    cand = 0
    for i in range(1, n):
      if knows(cand, i):
        cand = i
    for i in range(n):
      if i != cand and knows(cand, i) or not knows(i, cand):
        return -1
    return cand
