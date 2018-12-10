class Solution(object):
  def summaryRanges(self, nums):
    """
    :type nums: List[int]
    :rtype: List[str]
    """

    def outputRange(start, end):
      if start == end:
        return str(start)
      return "{}->{}".format(start, end)

    if not nums:
      return []
    ans = []
    start = 0
    for i in range(0, len(nums) - 1):
      if nums[i] + 1 != nums[i + 1]:
        ans.append(outputRange(nums[start], nums[i]))
        start = i + 1
    ans.append(outputRange(nums[start], nums[-1]))
    return ans
