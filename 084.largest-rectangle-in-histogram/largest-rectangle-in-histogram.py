class Solution(object):
  def largestRectangleArea(self, height):
    """
    :type height: List[int]
    :rtype: int
    """
    if not height:
      return 0
    height.append(-1)
    stack = []
    ans = 0
    for i in range(0, len(height)):
      while stack and height[i] < height[stack[-1]]:
        h = height[stack.pop()]
        w = i - stack[-1] - 1 if stack else i
        ans = max(ans, h * w)
      stack.append(i)
    height.pop()
    return ans
