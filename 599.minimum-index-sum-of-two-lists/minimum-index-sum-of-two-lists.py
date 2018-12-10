class Solution(object):
  def findRestaurant(self, list1, list2):
    """
    :type list1: List[str]
    :type list2: List[str]
    :rtype: List[str]
    """
    minSum = float("inf")
    ans = []
    d = {}
    for i, name in enumerate(list2):
      d[name] = i
    for i, name in enumerate(list1):
      idxSum = i + d.get(name, float("inf"))
      if idxSum == minSum:
        ans.append(name)
      if idxSum < minSum:
        ans = [name]
        minSum = idxSum
    return ans
