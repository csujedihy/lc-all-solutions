class Solution(object):
  def checkSubarraySum(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    if k == 0:
      return "0,0" in ",".join([str(n) for n in nums])
    if len(nums) < 2:
      return False
    if len(nums) == 2:
      return sum(nums) % k == 0
    ppSum = 0
    subSum = nums[0] + nums[1]
    d = set([0])
    for i in range(2, len(nums)):
      ppSum = (ppSum + nums[i - 2]) % k
      d |= {ppSum}
      subSum = (subSum + nums[i]) % k
      if subSum % k in d:
        return True
    return False
