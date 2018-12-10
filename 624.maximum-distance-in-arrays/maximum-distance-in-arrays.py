class Solution(object):
  # subarray sum
  def _maxDistance(self, arrays):
    """
    :type arrays: List[List[int]]
    :rtype: int
    """
    n = len(arrays)
    minArray, maxArray = [], []
    for i in range(n):
      minArray.append(arrays[i][0])
      maxArray.append(arrays[i][-1])
    lMax = [maxArray[0]] * n
    rMax = [maxArray[-1]] * n
    ans = float("-inf")
    for i in range(1, n):
      lMax[i] = max(lMax[i - 1], maxArray[i])
    for i in reversed(range(0, n - 1)):
      rMax[i] = max(rMax[i + 1], maxArray[i])
    for i in range(n):
      if 0 < i < n - 1:
        ans = max(ans, abs(max(lMax[i - 1], rMax[i + 1]) - minArray[i]))
      elif i == 0:
        ans = max(ans, abs(rMax[i + 1] - minArray[i]))
      else:
        ans = max(ans, abs(lMax[i - 1] - minArray[i]))
    return ans

  # one pass
  def maxDistance(self, arrays):
    n = len(arrays)
    minNum = arrays[0][0]
    maxNum = arrays[0][-1]
    ans = float("-inf")
    for i in range(1, n):
      head = arrays[i][0]
      tail = arrays[i][-1]
      ans = max(ans, abs(tail - minNum), abs(head - maxNum))
      minNum = min(head, minNum)
      maxNum = max(tail, maxNum)
    return ans
