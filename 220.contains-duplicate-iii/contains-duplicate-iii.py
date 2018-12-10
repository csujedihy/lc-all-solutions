import bisect


class Solution(object):
  def containsNearbyAlmostDuplicate(self, nums, k, t):
    """
    :type nums: List[int]
    :type k: int
    :type t: int
    :rtype: bool
    """
    if k == 0:
      return False
    bst = []
    if k < 0 or t < 0:
      return False
    for i, num in enumerate(nums):
      idx = bisect.bisect_left(bst, num)
      if idx < len(bst) and abs(bst[idx] - num) <= t:
        return True
      if idx > 0 and abs(bst[idx - 1] - num) <= t:
        return True
      if len(bst) >= k:
        del bst[bisect.bisect_left(bst, nums[i - k])]
      bisect.insort(bst, num)
    return False
