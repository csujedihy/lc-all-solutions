class Solution(object):
  def calculate(self, s):
    """
    :type s: str
    :rtype: int
    """
    s = "(" + s + ")"
    stack = []
    _stack = []
    i = 0
    while i < len(s):
      if s[i] == " ":
        i += 1
      elif s[i] == "(":
        _stack.append(len(stack))
        i += 1
      elif s[i] == ")":
        start = _stack.pop()
        j = start
        a = stack[j]
        while j + 2 < len(stack):
          ops = stack[j + 1]
          if ops == "+":
            a = a + stack[j + 2]
          elif ops == "-":
            a = a - stack[j + 2]
          else:
            return "invalid"
          j += 2
        k = len(stack) - start
        while k > 0:
          stack.pop()
          k -= 1
        stack.append(a)
        i += 1
      elif s[i] in "+-":
        stack.append(s[i])
        i += 1
      else:
        start = i
        while i < len(s) and s[i] not in "-+() ":
          i += 1
        num = int(s[start:i])
        stack.append(num)
    return stack[0]
