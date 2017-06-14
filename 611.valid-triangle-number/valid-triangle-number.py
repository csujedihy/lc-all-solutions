class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        nums.sort()
        for i in xrange(2, len(nums)):
            start, end = 0, i - 1
            target = nums[i]
            while start < end:
                if nums[start] + nums[end] > target:
                    res += end - start
                    end -= 1
                else:
                    start += 1
        return res
                
            
                
        