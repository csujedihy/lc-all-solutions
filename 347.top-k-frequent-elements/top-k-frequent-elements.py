class Solution(object):
  def topKFrequent(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    d = {}
    res = []
    ans = []
    buckets = [[] for _ in range(len(nums) + 1)]

    for num in nums:
      d[num] = d.get(num, 0) + 1

    for key in d:
      res.append((d[key], key))

    for t in res:
      freq, key = t
      buckets[freq].append(key)

    buckets.reverse()

    for item in buckets:
      if item and k > 0:
        while item and k > 0:
          ans.append(item.pop())
          k -= 1
        if k == 0:
          return ans

    return ans
