class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findRange(left):
            l, r = 0, len(nums) - 1
            m = 0
            while l <= r:
                m = l + (r - l) // 2
                if nums[m] < target:
                    l = m + 1
                elif nums[m] > target:
                    r = m - 1
                elif left and m > 0 and nums[m - 1] == nums[m]:
                    r = m - 1
                elif not left and m + 1 < len(nums) and nums[m + 1] == nums[m]:
                    l = m + 1
                else:
                    return m
            if m < len(nums) and nums[m] == target:
                return m
            else:
                return -1
        return [findRange(True), findRange(False)]
