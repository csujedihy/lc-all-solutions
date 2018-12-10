class Solution(object):
  def maxSlidingWindow(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    if k == 0:
      return []
    ans = [0 for _ in range(len(nums) - k + 1)]
    stack = collections.deque([])
    for i in range(0, k):
      while stack and nums[stack[-1]] < nums[i]:
        stack.pop()
      stack.append(i)
    ans[0] = nums[stack[0]]
    idx = 0
    for i in range(k, len(nums)):
      idx += 1
      if stack and stack[0] == i - k:
        stack.popleft()
      while stack and nums[stack[-1]] < nums[i]:
        stack.pop()
      stack.append(i)
      ans[idx] = nums[stack[0]]

    return ans
