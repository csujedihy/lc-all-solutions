import bisect


class Solution(object):
  def reversePairs(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    ans = 0
    bst = []
    for num in nums:
      right = 2 * num
      idx = bisect.bisect_right(bst, right)
      ans += len(bst) - idx
      bisect.insort(bst, num)
    return ans
