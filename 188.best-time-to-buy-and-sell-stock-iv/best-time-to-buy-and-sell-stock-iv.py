import heapq
import random


class Solution(object):
  def findKthLargest(self, nums, k):
    """
    :type A: List[int]
    :type k: int
    :rtype: int
    """

    def quickselect(start, end, nums, k):
      if start == end:
        return nums[start]

      mid = partition(start, end, nums)

      if mid == k:
        return nums[mid]
      elif k > mid:
        return quickselect(mid + 1, end, nums, k)
      else:
        return quickselect(start, mid - 1, nums, k)

    def partition(start, end, nums):
      p = random.randrange(start, end + 1)
      pv = nums[p]
      nums[end], nums[p] = nums[p], nums[end]
      mid = start
      for i in range(start, end):
        if nums[i] >= pv:
          nums[i], nums[mid] = nums[mid], nums[i]
          mid += 1
      nums[mid], nums[end] = nums[end], nums[mid]
      return mid

    return quickselect(0, len(nums) - 1, nums, k - 1)

  def maxProfit(self, k, prices):
    """
    :type k: int
    :type prices: List[int]
    :rtype: int
    """
    if not prices:
      return 0
    stack = []
    heap = []
    v = p = 0
    n = len(prices)
    ans = 0
    while p < n:
      v = p
      while v < n - 1 and prices[v] >= prices[v + 1]:
        v += 1
      p = v + 1
      while p < n and prices[p] > prices[p - 1]:
        p += 1
      while stack and prices[stack[-1][0]] > prices[v]:
        _v, _p = stack.pop()
        heap.append(prices[_p - 1] - prices[_v])
      while stack and prices[stack[-1][1] - 1] < prices[p - 1]:
        heap.append(prices[stack[-1][1] - 1] - prices[v])
        v, _ = stack.pop()
      stack.append((v, p))

    heap += [prices[p - 1] - prices[v] for v, p in stack]
    if len(heap) < k:
      return sum(heap)
    self.findKthLargest(heap, k)
    return sum(heap[:k])
