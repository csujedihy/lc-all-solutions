class Solution(object):
  def hIndex(self, citations):
    """
    :type citations: List[int]
    :rtype: int
    """
    if not citations:
      return 0
    n = len(citations)
    start, end = 0, n - 1
    while start < end:
      mid = start + (end - start) / 2
      if citations[mid] >= n - mid:
        end = mid
      else:
        start = mid + 1
    return n - start if citations[start] != 0 else 0
