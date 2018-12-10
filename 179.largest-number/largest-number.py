class Solution:
  # @param {integer[]} nums
  # @return {string}
  def largestNumber(self, nums):
    def cmpFunc(a, b):
      stra, strb = str(a), str(b)
      if stra + strb < strb + stra:
        return -1
      elif stra + strb > strb + stra:
        return 1
      else:
        return 0

    nums.sort(cmp=cmpFunc, reverse=True)
    return "".join(str(num) for num in nums) if sum(nums) != 0 else "0"
