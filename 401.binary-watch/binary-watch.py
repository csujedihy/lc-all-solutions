class Solution(object):
  def readBinaryWatch(self, num):
    """
    :type num: int
    :rtype: List[str]
    """
    ans = []
    for i in range(0, 12):
      for j in range(0, 60):
        if (bin(i) + bin(j)).count("1") == num:
          ans.append("%d:%02d" % (i, j))
    return ans
