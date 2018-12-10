import string


class Solution(object):
  def isValid(self, code):
    """
    :type code: str
    :rtype: bool
    """

    def getTokenStartsAt(start):
      for i in range(start, len(code)):
        if code[i] == ">":
          break
      return code[start:i + 1]

    def isTagsMatched(left, right):
      return len(left) + 1 == len(right) and left[1:] == right[2:]

    def isClosedTag(tag):
      return tag[1] == "/"

    def isCDATATag(i):
      return code.startswith("<![CDATA[", i)

    def isTag(tag):
      if len(tag) < 3:
        return False
      if tag[-1] != ">":
        return False

      tag = tag[1:-1]
      if tag[0] == "/":
        tag = tag[1:]
      if not 1 <= len(tag) <= 9:
        return False
      for c in tag:
        if c not in string.ascii_uppercase:
          return False
      return True

    if code[0] != "<":
      return False
    tagLen = 0
    stack = []
    i = 0
    while i < len(code):
      if code[i] == "<":
        if isCDATATag(i):
          if not stack:
            return False
          while i < len(code) - 7 and not code.startswith("]]>", i):
            i += 1
          if code.startswith("]]>", i):
            i += 3
            continue
          else:
            return False
        else:
          token = getTokenStartsAt(i)
          if not isTag(token):
            return False
          if not isClosedTag(token):
            stack.append(token)
          else:
            if not stack:
              return False
            if isTagsMatched(stack[-1], token):
              stack.pop()
              if not stack and i + len(token) < len(code):
                return False
            else:
              return False
          i += len(token)
      else:
        i += 1
    return not stack
