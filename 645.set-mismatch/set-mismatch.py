class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = [-1, -1]
        diff = diffSquare = 0
        for i, num in enumerate(nums):
            diff += i + 1 - num
            diffSquare += (i + 1)**2 - num ** 2
        ans[1] = (diffSquare / diff + diff) / 2
        ans[0] = ans[1] - diff
        ans.sort()
        if diff > 0:
            return ans
        return ans[::-1]        
        
            