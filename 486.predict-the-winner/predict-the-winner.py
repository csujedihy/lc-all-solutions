class Solution(object):
  def PredictTheWinner(self, nums):
    """
    :type nums: List[int]
    :rtype: bool
    """

    def canWin(nums, start, end, visited, partSum, maxSum, order):
      # print "canWin order=", order
      if (start, end, partSum, order) in visited:
        return visited[start, end, partSum, order]
      if start > end:
        # print "order=", order, partSum, maxSum
        if order == 0:
          if partSum >= maxSum - partSum:
            return False
          return True
        else:
          if partSum >= maxSum - partSum:
            return True
          return False

      visited[start, end, partSum, order] = False
      if not canWin(nums, start + 1, end, visited, partSum - order * nums[start], maxSum, ~order):
        visited[start, end, partSum, order] = True
        # print "order=", order, "return True"
        return True
      if not canWin(nums, start, end - 1, visited, partSum - order * nums[end], maxSum, ~order):
        visited[start, end, partSum, order] = True
        # print "order=", order, "return True"
        return True
      return visited[start, end, partSum, order]

    return canWin(nums, 0, len(nums) - 1, {}, 0, sum(nums), -1)
