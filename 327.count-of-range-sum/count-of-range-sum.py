class Solution(object):
  def countRangeSum(self, nums, lower, upper):
    """
    :type nums: List[int]
    :type lower: int
    :type upper: int
    :rtype: int
    """

    def update(b, i, delta):
      while i < len(b):
        b[i] += delta
        i += (i & -i)

    def sumRange(b, i):
      ret = 0
      while i > 0:
        ret += b[i]
        i -= (i & -i)
      return ret

    ans = 0
    pres = [0] * (len(nums) + 1)
    b = [0] * (len(nums) + 2)

    for i in range(0, len(nums)):
      pres[i + 1] = pres[i] + nums[i]

    sortedPres = sorted(pres)

    for end in pres:
      count = sumRange(b, bisect.bisect_right(sortedPres, end - lower)) - sumRange(b, bisect.bisect_left(sortedPres,
                                                                                                         end - upper))
      ans += count
      update(b, bisect.bisect_left(sortedPres, end) + 1, 1)
    return ans
