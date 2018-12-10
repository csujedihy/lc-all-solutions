class Solution(object):

  def __init__(self, nums):
    """
    
    :type nums: List[int]
    :type numsSize: int
    """
    self.nums = nums

  def pick(self, target):
    """
    :type target: int
    :rtype: int
    """
    count = 0
    ans = -1
    for i in range(0, len(self.nums)):
      if self.nums[i] == target:
        count += 1
        if random.randrange(0, count) == 0:
          ans = i
    return ans

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
