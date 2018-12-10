class Solution(object):
  def merge(self, nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: void Do not return anything, modify nums1 in-place instead.
    """
    end = m + n - 1
    m -= 1
    n -= 1
    while end >= 0 and m >= 0 and n >= 0:
      if nums1[m] > nums2[n]:
        nums1[end] = nums1[m]
        m -= 1
      else:
        nums1[end] = nums2[n]
        n -= 1
      end -= 1

    while n >= 0:
      nums1[end] = nums2[n]
      end -= 1
      n -= 1
