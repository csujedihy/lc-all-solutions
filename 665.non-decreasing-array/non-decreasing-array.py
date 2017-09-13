class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        flag = False
        pre = float("-inf")
        for i in range(len(nums) - 1):
            if nums[i] < pre:
                if nums[i + 1] >= nums[i - 1]:
                    nums[i] = nums[i + 1]
                else:
                    nums[i - 1] = nums[i]
                flag = True
                break
            pre = nums[i]
        if not flag and len(nums) > 1 and nums[-1] < nums[-2]:
            nums[-1] = nums[-2]
        pre = float("-inf")
        for num in nums:
            if num < pre:
                return False
            pre = num
        return True