import bisect


class Solution(object):
  def countSmaller(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    ans = []
    bst = []
    for num in reversed(nums):
      idx = bisect.bisect_left(bst, num)
      ans.append(idx)
      bisect.insort(bst, num)
    return ans[::-1]
