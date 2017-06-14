class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tail = []
        for i in xrange(0, len(nums)):
            idx = bisect.bisect_right(tail, nums[i])
            if idx - 1 >= 0 and nums[i] == tail[idx - 1]:
                continue
            if idx == len(tail):
                tail.append(nums[i])
            else:
                tail[idx] = nums[i]
        return len(tail)