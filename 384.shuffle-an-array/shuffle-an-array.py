class Solution(object):

  def __init__(self, nums):
    """

    :type nums: List[int]
    :type size: int
    """
    self.nums = nums
    self.reset = lambda: self.nums

  def shuffle(self):
    """
    Returns a random shuffling of the array.
    :rtype: List[int]
    """
    nums = self.nums + []
    for i in reversed(range(0, len(nums))):
      idx = random.randrange(0, i + 1)
      nums[i], nums[idx] = nums[idx], nums[i]
    return nums

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
