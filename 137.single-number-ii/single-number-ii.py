class Solution(object):
  def singleNumber(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    def singleNumberK(nums, k):
      ret = 0
      count = [0] * 32
      for i in range(0, 32):
        for num in nums:
          if num & (1 << i):
            count[i] += 1
        if count[i] % 3 != 0:
          ret |= 1 << i
      if ret > 0x7fffffff:
        ret -= 0x100000000
      return ret

    return singleNumberK(nums, 3)
