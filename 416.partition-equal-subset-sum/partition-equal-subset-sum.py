class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = sum(nums)
        if s == 0:
            return True
        if s % 2 == 0:
            s, current = s / 2, 0
            for num in nums:
                current |= ((current or 1) << num) % (1 << (s + 1))
                if current >= 1 << s:
                    return True
        return False