class Solution(object):
  def findMaximizedCapital(self, k, W, Profits, Capital):
    current = []
    future = sorted(zip(Capital, Profits))[::-1]
    for _ in range(k):
      while future and future[-1][0] <= W:
        heapq.heappush(current, -future.pop()[1])
      if current:
        W -= heapq.heappop(current)
    return W
