class Solution(object):
  def find132pattern(self, nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    ak = float("-inf")
    stack = []
    for num in reversed(nums):
      if ak > num:
        return True
      while stack and stack[-1] < num:
        ak = stack.pop()
      stack += num,
    return False
