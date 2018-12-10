class Solution(object):
  def evalRPN(self, tokens):
    """
    :type tokens: List[str]
    :rtype: int
    """
    stack = []
    for token in tokens:
      if token in ["+", "-", "*", "/"]:
        b, a = stack.pop(), stack.pop()
        if token == "+":
          res = a + b
        if token == "-":
          res = a - b
        if token == "*":
          res = a * b
        if token == "/":
          res = int(float(a) / float(b))
        stack.append(res)
      else:
        stack.append(int(token))
    return stack.pop()
