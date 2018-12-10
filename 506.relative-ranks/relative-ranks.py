class Solution(object):
  def findRelativeRanks(self, nums):
    """
    :type nums: List[int]
    :rtype: List[str]
    """
    ans = [""] * len(nums)
    scores = []
    for i, num in enumerate(nums):
      scores.append((num, i))
    scores.sort(reverse=True)
    rankTitles = ["Gold Medal", "Silver Medal", "Bronze Medal"]
    rank = 0
    for _, i in scores:
      if rank > 2:
        ans[i] = str(rank + 1)
      else:
        ans[i] = rankTitles[rank]
      rank += 1
    return ans
