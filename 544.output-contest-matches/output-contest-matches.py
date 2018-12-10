class Solution(object):
  def findContestMatch(self, n):
    """
    :type n: int
    :rtype: str
    """

    def helper(schedule):
      if len(schedule) == 1:
        return schedule[0]
      m = []
      for i in range(len(schedule) / 2):
        m.append("({},{})".format(schedule[i], schedule[-i - 1]))
      return helper(m)

    return helper(map(str, range(1, n + 1)))
