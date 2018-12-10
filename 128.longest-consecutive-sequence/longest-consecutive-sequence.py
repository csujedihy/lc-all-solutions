class Solution(object):
  def longestConsecutive(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    ans = 0
    s = set(nums)
    for num in nums:
      if num in s:
        s.discard(num)
        cnt = 1
        right = num + 1
        left = num - 1
        while left in s:
          s.discard(left)
          cnt += 1
          left -= 1
        while right in s:
          s.discard(right)
          cnt += 1
          right += 1
        ans = max(ans, cnt)
    return ans
