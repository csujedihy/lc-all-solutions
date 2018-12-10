class Solution(object):
  def rotate(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    if len(nums) == 0 or k == 0:
      return

    def reverse(start, end, s):
      while start < end:
        s[start], s[end] = s[end], s[start]
        start += 1
        end -= 1

    n = len(nums) - 1
    k = k % len(nums)
    reverse(0, n - k, nums)
    reverse(n - k + 1, n, nums)
    reverse(0, n, nums)
