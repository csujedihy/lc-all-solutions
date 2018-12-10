class Solution(object):
  def findDuplicate(self, paths):
    """
    :type paths: List[str]
    :rtype: List[List[str]]
    """
    d = collections.defaultdict(list)
    for path in paths:
      raw = path.split(" ")
      dirPath = raw[0]
      for data in raw[1:]:
        name, sign = data.split("(")
        d[sign].append(dirPath + "/" + name)
    return filter(lambda x: len(x) > 1, d.values())
