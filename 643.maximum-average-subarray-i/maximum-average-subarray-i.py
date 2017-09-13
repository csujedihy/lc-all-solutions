from collections import deque
class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        s = 0
        ans = float("-inf")
        queue = deque([])
        for num in nums:
            queue.append(num)
            s += num
            if len(queue) > k:
                s -= queue.popleft()
            if len(queue) == k:
                ans = max(ans, float(s) / k)
        return ans
                