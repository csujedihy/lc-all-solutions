class Solution(object):
  def maxRotateFunction(self, A):
    """
    :type A: List[int]
    :rtype: int
    """
    if not A:
      return 0

    sumA = sum(A)
    fk = 0
    n = len(A)
    for i, num in enumerate(A):
      fk += i * num
    idx = n - 1
    ans = float("-inf")
    for _ in range(n):
      fk += sumA - n * A[idx]
      ans = max(ans, fk)
      idx -= 1
    return ans
