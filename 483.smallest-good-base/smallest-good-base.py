import math


class Solution(object):
  def smallestGoodBase(self, n):
    """
    :type n: str
    :rtype: str
    """
    n = int(n)
    max_m = int(math.log(n, 2))  # Refer [7]
    for m in range(max_m, 1, -1):
      k = int(n ** m ** -1)
      if (k ** (m + 1) - 1) / (k - 1) == n:
        return str(k)
    return str(n - 1)
