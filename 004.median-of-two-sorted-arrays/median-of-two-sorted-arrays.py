class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        def helper(k, nums1, nums2, start1, start2):
            if start1 >= len(nums1):
                return nums2[start2 + k - 1]
            if start2 >= len(nums2):
                return nums1[start1 + k - 1]
            if k == 1:
                return min(nums1[start1], nums2[start2])
            
            m1 = start1 + k / 2 - 1
            m2 = start2 + k / 2 - 1
            mid1 = float("inf") if m1 >= len(nums1) else nums1[m1]
            mid2 = float("inf") if m2 >= len(nums2) else nums2[m2]

            if mid1 < mid2:
                return helper(k - k / 2, nums1, nums2, m1 + 1, start2)
            else:
                return helper(k - k / 2, nums1, nums2, start1, m2 + 1)

        
        length = len(nums1) + len(nums2)
        k = length / 2
        if length % 2 == 0:
            return (helper(k, nums1, nums2, 0, 0) + helper(k + 1, nums1, nums2, 0, 0)) / 2.0
        else:
            return helper(k + 1, nums1, nums2, 0, 0)
