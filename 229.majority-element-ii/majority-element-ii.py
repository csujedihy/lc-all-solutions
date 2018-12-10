class Solution(object):
  def majorityElement(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    if len(nums) == 0 or nums is None:
      return []
    c1, c2 = None, None
    n1, n2 = 0, 0
    for i in range(0, len(nums)):
      if c1 == nums[i]:
        n1 += 1
      elif c2 == nums[i]:
        n2 += 1
      elif n1 == 0:
        c1 = nums[i]
        n1 += 1
      elif n2 == 0:
        c2 = nums[i]
        n2 += 1
      else:
        n1, n2 = n1 - 1, n2 - 1

    print
    c1, c2

    ret = []
    size = len(nums)
    cn1 = 0
    cn2 = 0
    for i in range(0, len(nums)):
      if nums[i] == c1:
        cn1 += 1
      elif nums[i] == c2:
        cn2 += 1

    if cn1 >= size / 3 + 1:
      ret.append(c1)
    if cn2 >= size / 3 + 1:
      ret.append(c2)
    return ret
