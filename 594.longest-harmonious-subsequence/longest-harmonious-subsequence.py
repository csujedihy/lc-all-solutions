class Solution(object):
  def findLHS(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    ans = 0
    d = collections.Counter(nums)
    for num in nums:
      if num + 1 in d:
        ans = max(ans, d[num] + d[num + 1])
    return ans
