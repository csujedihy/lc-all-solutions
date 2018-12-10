class Solution(object):
  def intersection(self, nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    d = {}
    ans = []
    for num in nums1:
      d[num] = d.get(num, 0) + 1

    for num in nums2:
      if num in d:
        ans.append(num)
        del d[num]
    return ans
