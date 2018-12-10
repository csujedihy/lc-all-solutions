nums = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine",
        10: "ten"}
feature = {0: "z", 1: "o", 2: "w", 3: "r", 4: "u", 5: "v", 6: "x", 7: "s", 8: "g", 9: "i", 10: "t"}


class Solution(object):
  def originalDigits(self, s):
    """
    :type s: str
    :rtype: str
    """
    global nums, feature
    ans = []
    count = {}
    for c in s:
      count[c] = count.get(c, 0) + 1
    for num in [0, 2, 4, 6, 8, 1, 3, 7, 5, 10, 9]:
      featureNum = count.get(feature[num], 0)
      if featureNum > 0:
        ans += [str(num)] * featureNum
        word = nums[num]
        for c in word:
          count[c] -= featureNum
    ans.sort()
    return "".join(ans)
