class Solution(object):
  def maximumGap(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) < 2:
      return 0
    a, b = min(nums), max(nums)
    if a == b:
      return 0
    ans = 0
    gap = int(math.ceil((b - a + 0.0) / (len(nums) - 1)))
    bucketMin = [None for _ in range(0, len(nums) + 1)]
    bucketMax = [None for _ in range(0, len(nums) + 1)]

    for num in nums:
      index = (num - a) / gap
      if bucketMin[index] is None:
        bucketMin[index] = num
      else:
        bucketMin[index] = min(bucketMin[index], num)
      if bucketMax[index] is None:
        bucketMax[index] = num
      else:
        bucketMax[index] = max(bucketMax[index], num)
    bucketMin = [b for b in bucketMin if b is not None]
    bucketMax = [b for b in bucketMax if b is not None]
    for i in range(0, len(bucketMin) - 1):
      ans = max(ans, bucketMin[i + 1] - bucketMax[i])
    return ans
