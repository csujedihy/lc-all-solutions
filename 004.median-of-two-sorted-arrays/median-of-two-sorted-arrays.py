class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        def helper(nums1, nums2, start, end, n):
            pass
        
        m = len(nums1)
        n = len(nums2)
        half = (m + n) / 2
        if m + n % 2 == 1:
            return helper(nums1, nums2, start, end, half)
        else:
            ans = helper(nums1, nums2, start, end, half - 1)
            ans += helper(nums1, nums2, start, end, half)
            return ans / 2.0
            
            
