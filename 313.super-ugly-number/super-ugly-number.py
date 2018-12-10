import heapq


class Solution(object):
  def nthSuperUglyNumber(self, n, primes):
    """
    :type n: int
    :type primes: List[int]
    :rtype: int
    """
    dp = [0] * (n + 1)
    dp[1] = 1
    heap = []
    indexes = [1] * len(primes)
    for i in range(0, len(primes)):
      heapq.heappush(heap, (dp[indexes[i]] * primes[i], i))

    for i in range(2, n + 1):
      minV = heap[0][0]
      dp[i] = minV
      while heap[0][0] == minV:
        value, xi = heapq.heappop(heap)
        indexes[xi] += 1
        heapq.heappush(heap, (dp[indexes[xi]] * primes[xi], xi))
    return dp[-1]
