class Solution(object):
  def getPermutation(self, n, k):
    """
    :type n: int
    :type k: int
    :rtype: str
    """
    visited = [0 for i in range(n)]
    fact = [math.factorial(n - i - 1) for i in range(n)]
    ans = ""
    k -= 1
    for i in range(n):
      t = k / fact[i]
      for j in range(n):
        if not visited[j]:
          if t == 0:
            break
          t -= 1
      ans += str(j + 1)
      k %= fact[i]
      visited[j] = 1
    return ans
