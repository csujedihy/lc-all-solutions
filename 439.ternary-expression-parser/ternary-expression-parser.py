class Solution(object):
  def parseTernary(self, expression):
    """
    :type expression: str
    :rtype: str
    """
    stack = []
    i = len(expression) - 1
    while i >= 0:
      if expression[i] not in ["?", ":"]:
        stack.append(expression[i])
      elif expression[i] == "?":
        i -= 1
        if expression[i] == "T":
          top = stack.pop()
          stack.pop()
          stack.append(top)
        elif expression[i] == "F":
          stack.pop()
      i -= 1
    return stack[0]
