class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ans = left = 0
        right = len(height) - 1
        leftWall = rightWall = float("-inf")
        while left <= right:
            if leftWall <= rightWall:
                ans += max(0, leftWall - height[left])
                leftWall = max(leftWall, height[left])
                left += 1
            else:
                ans += max(0, rightWall - height[right])
                rightWall = max(rightWall, height[right])
                right -= 1
        return ans