class Solution(object):
  def compareVersion(self, version1, version2):
    """
    :type version1: str
    :type version2: str
    :rtype: int
    """
    v1 = version1.split(".")
    v2 = version2.split(".")
    i = 0
    while i < len(v1) and i < len(v2):
      v1Seg, v2Seg = int(v1[i]), int(v2[i])
      if v1Seg > v2Seg:
        return 1
      elif v1Seg < v2Seg:
        return -1
      else:
        i += 1
    if i < len(v1) and int("".join(v1[i:])) != 0:
      return 1
    if i < len(v2) and int("".join(v2[i:])) != 0:
      return -1
    return 0
