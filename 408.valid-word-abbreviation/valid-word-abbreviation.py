class Solution(object):
  def validWordAbbreviation(self, dest, src):
    """
    :type word: str
    :type abbr: str
    :rtype: bool
    """
    start = j = 0
    digit = False
    for i in range(0, len(src)):
      if src[i].isdigit():
        if not digit:
          if src[i] == "0":
            return False
          start = i
          digit = True
      else:
        if digit:
          jump = int(src[start:i])
          digit = False
          j += jump
        if j >= len(dest) or src[i] != dest[j]:
          return False
        j += 1
      if i == len(src) - 1:
        if digit:
          jump = int(src[start:i + 1])
          digit = False
          j += jump
          if j != len(dest):
            return False
    return True
