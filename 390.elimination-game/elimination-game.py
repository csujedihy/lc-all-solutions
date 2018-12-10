class Solution(object):
  def lastRemaining(self, n):
    """
    :type n: int
    :rtype: int
    """
    count = n
    head = 1
    isFromLeft = True
    step = 1
    while count > 1:
      if isFromLeft or count % 2 == 1:
        head = head + step
      count /= 2
      step *= 2
      isFromLeft = not isFromLeft
    return head
