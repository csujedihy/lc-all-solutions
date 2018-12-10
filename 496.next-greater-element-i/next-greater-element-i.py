class Solution(object):
  def nextGreaterElement(self, findNums, nums):
    """
    :type findNums: List[int]
    :type nums: List[int]
    :rtype: List[int]
    """
    d = {}
    ans = [-1] * len(findNums)
    for i, num in enumerate(findNums):
      d[num] = i
    stack = []
    for num in nums:
      while stack and stack[-1] < num:
        top = stack.pop()
        if top in d:
          ans[d[top]] = num
      stack.append(num)
    return ans
