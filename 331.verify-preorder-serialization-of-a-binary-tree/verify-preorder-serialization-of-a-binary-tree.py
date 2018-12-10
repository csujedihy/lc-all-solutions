class Solution(object):
  def isValidSerialization(self, preorder):
    """
    :type preorder: str
    :rtype: bool
    """
    p = preorder.split(",")
    if len(p) == 1:
      if p[0] == "#":
        return True
      return False
    stack = [p[0]]
    for c in p[1:]:
      if len(stack) == 1 and stack[0] == "#":
        return False
      stack.append(c)
      while len(stack) > 2 and stack[-1] + stack[-2] == "##":
        stack.pop()
        stack.pop()
        stack.pop()
        stack.append("#")
    if len(stack) == 1 and stack[0] == "#":
      return True
    return False
