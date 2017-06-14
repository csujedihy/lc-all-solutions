class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        def valid(nums, target, m):
            count = 1
            total = 0
            for num in nums:
                total += num
                if total > target:
                    count += 1
                    total = num
                    if count > m:
                        return False
            return True
        
        
        start, end = max(nums), sum(nums)
        mid = 0
        while start <= end:
            mid = start + (end - start) / 2
            if valid(nums, mid, m):
                end = mid - 1
            else:
                start = mid + 1
                
        return start
            