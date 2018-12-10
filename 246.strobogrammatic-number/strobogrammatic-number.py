class Solution(object):
  def isStrobogrammatic(self, num):
    """
    :type num: str
    :rtype: bool
    """
    start, end, legal = 0, len(num) - 1, "01689"
    while start <= end:
      if "".join(sorted(num[start] + num[end])) not in ["00", "11", "88", "69"]:
        return False
      start += 1
      end -= 1
    return True
