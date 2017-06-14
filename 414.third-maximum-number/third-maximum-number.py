class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        one = two = three = float("-inf")
        for i in xrange(0, len(nums)):
            if nums[i] in [one, two, three]:
                continue
            _one = one
            _two = two
            if nums[i] >= one:
                one = nums[i]
                two = _one
                three = _two
            elif nums[i] >= two:
                two = nums[i]
                three = _two
            elif nums[i] >= three:
                three = nums[i]
        return three if three != float("-inf") else one
            
            
        