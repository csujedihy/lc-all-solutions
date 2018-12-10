from collections import deque


class Solution(object):
  def containsNearbyDuplicate(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    if not nums:
      return False
    if k == 0:
      return False
    k = k + 1
    k = min(k, len(nums))

    window = deque([])
    d = set()
    for i in range(0, k):
      if nums[i] in d:
        return True
      d |= {nums[i]}
      window.append(i)
    for i in range(k, len(nums)):
      d -= {nums[window.popleft()]}
      if nums[i] in d:
        return True
      d |= {nums[i]}
      window.append(i)
    return False
