class Solution(object):
  def matrixReshape(self, nums, r, c):
    """
    :type nums: List[List[int]]
    :type r: int
    :type c: int
    :rtype: List[List[int]]
    """
    if r * c != len(nums) * len(nums[0]):
      return nums
    m = len(nums)
    n = len(nums[0])
    ans = [[0] * c for _ in range(r)]
    for i in range(r * c):
      ans[i / c][i % c] = nums[i / n][i % n]
    return ans
