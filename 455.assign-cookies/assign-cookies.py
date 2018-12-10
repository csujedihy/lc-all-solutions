from collections import Counter


class Solution(object):
  def findContentChildren(self, children, cookies):
    """
    :type g: List[int]
    :type s: List[int]
    :rtype: int
    """
    cookies.sort()
    children.sort()
    i = 0
    for cookie in cookies:
      if i >= len(children):
        break
      if children[i] <= cookie:
        i += 1
    return i
