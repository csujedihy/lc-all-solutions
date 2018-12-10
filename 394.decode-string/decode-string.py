class Solution(object):
  def decodeString(self, s):
    """
    :type s: str
    :rtype: str
    """
    num = ""
    stack = [["", 1]]
    for c in s:
      if c in "0123456789":
        num += c
      elif c == "[":
        stack.append(["", int(num)])
        num = ""
      elif c == "]":
        ss, k = stack.pop()
        stack[-1][0] += ss * k
      else:
        stack[-1][0] += c
    return stack[-1][0]
