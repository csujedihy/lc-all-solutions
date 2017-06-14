class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r = 0, len(height) - 1
        ans = 0
        while l < r:
            ans = max((r - l) * min(height[l], height[r]), ans)
            if height[l] >= height[r]:
                r -= 1
            else:
                l += 1
        return ans