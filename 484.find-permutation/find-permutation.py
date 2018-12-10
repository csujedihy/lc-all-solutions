class Solution(object):
  def findPermutation(self, s):
    """
    :type s: str
    :rtype: List[int]
    """
    ans = range(1, len(s) + 2)
    cnt = 0
    for i in range(len(s)):
      if s[i] == "D":
        cnt += 1
      else:
        ans[i - cnt:i + 1] = ans[i - cnt:i + 1][::-1]
        cnt = 0
    if s[-1] == "D":
      ans[len(s) - cnt:len(s) + 1] = ans[len(s) - cnt:len(s) + 1][::-1]
    return ans
